-- Give table columns width in proportion to how much text they actually carry.
--
-- THE PROBLEM. Every table in the corpus uses a uniform separator row (|---|---|),
-- which carries no width information, so pandoc falls back to equal-width columns.
-- In the §E.3 falsifier table that means the "#" column — whose widest cell is the
-- two characters "16" — gets exactly as much page as "What it kills", whose cells
-- run to 60+ characters. The wide columns then wrap to many lines while the narrow
-- ones sit nearly empty, which is what makes those tables tall and hard to read.
--
-- THE MEASURE. Per column, take the MEAN cell length (header included), damped by
-- an exponent < 1 so the widest:narrowest ratio does not become extreme. Mean, not
-- max: one outlier cell should not seize the page, and the mean tracks the typical
-- wrapping burden.
--
-- THE FLOOR, and why it is CODE-ONLY. A column must be wide enough for the widest
-- thing in it that cannot be broken. Prose can hyphenate and wrap, so a long
-- English word needs no floor — but a snake_case identifier in a code span has no
-- break opportunity at all, and if the column is narrower than the identifier it
-- does not wrap, it runs straight over the boundary and collides with the next
-- column's text. That actually happened: `koide_modus_tollens_consistency` (31
-- chars) overprinted the Origin column. So the floor is computed from the longest
-- token inside Code spans only. Measuring longest token over ALL text instead
-- over-subscribes badly — on the 7-column falsifier table the floors then summed
-- to 1.27 of the line, which is unsatisfiable.
--
-- THE ALLOCATION. Floors are honoured first; whatever line is left is shared among
-- the columns in proportion to their damped means, and no column is ever pushed
-- below its own floor. If the floors alone over-subscribe the line (a table of many
-- columns each holding a long identifier), every column is scaled proportionally
-- rather than some being starved — some identifier will then wrap mid-token, which
-- is the lesser evil and is at least uniform.
--
-- An earlier version squeezed the *unfloored* columns to absorb the whole overrun,
-- which drove "Current bound" and "TWT prediction" to 3-5% of the line and wrapped
-- them one character per line. Keep the water-filling below; do not replace it with
-- a single normalisation pass.

local stringify = pandoc.utils.stringify

local DAMP  = 0.62   -- exponent on the mean length; < 1 compresses extremes
local MIN_W = 0.045  -- no column narrower than 4.5% of the text block
local MAX_W = 0.40   -- no column wider than 40%

-- Width of one monospace character as a fraction of the text block, measured from
-- the rendered output (Consolas at Scale=0.86, 10pt, 2.1cm margins ≈ 92 chars across).
local MONO_CHAR_FRAC = 0.0112

local function utf8len(s)
  return (utf8 and utf8.len(s)) or #s
end

-- Longest unbreakable run inside CODE spans only (prose wraps; code does not).
local function longest_code_token(cell)
  local best = 0
  local function walk(blocks)
    for _, b in ipairs(blocks) do
      if b.t == "Code" or b.t == "CodeBlock" then
        for tok in b.text:gmatch("%S+") do
          local n = utf8len(tok)
          if n and n > best then best = n end
        end
      end
      if b.content and type(b.content) == "table" then walk(b.content) end
      if b.c and type(b.c) == "table" then walk(b.c) end
    end
  end
  walk(cell.contents or cell.content or {})
  return best
end

local function collect(rows, lens, counts, floors, ncol)
  for _, row in ipairs(rows) do
    local ci = 0
    for _, cell in ipairs(row.cells) do
      ci = ci + 1
      if ci <= ncol then
        lens[ci] = lens[ci] + utf8len(stringify(cell))
        counts[ci] = counts[ci] + 1
        local t = longest_code_token(cell)
        if t > floors[ci] then floors[ci] = t end
      end
    end
  end
end

function Table(tbl)
  local ncol = #tbl.colspecs
  if ncol < 2 then return nil end

  local lens, counts, tok = {}, {}, {}
  for i = 1, ncol do lens[i], counts[i], tok[i] = 0, 0, 0 end

  collect(tbl.head.rows, lens, counts, tok, ncol)
  for _, body in ipairs(tbl.bodies) do
    collect(body.body, lens, counts, tok, ncol)
  end

  -- desired share from damped mean length
  local want, sum = {}, 0
  for i = 1, ncol do
    local mean = (counts[i] > 0) and (lens[i] / counts[i]) or 1
    if mean < 1 then mean = 1 end
    want[i] = mean ^ DAMP
    sum = sum + want[i]
  end
  if sum <= 0 then return nil end
  for i = 1, ncol do want[i] = want[i] / sum end

  -- floors: code-token width, bounded by MIN_W below and MAX_W above
  local floor, floor_sum = {}, 0
  for i = 1, ncol do
    local f = tok[i] * MONO_CHAR_FRAC
    if f < MIN_W then f = MIN_W end
    if f > MAX_W then f = MAX_W end
    floor[i] = f
    floor_sum = floor_sum + f
  end

  local w = {}
  if floor_sum >= 1.0 then
    -- Over-subscribed: share proportionally to the floors themselves. Uniform
    -- compromise beats starving whichever columns happened not to be floored.
    for i = 1, ncol do w[i] = floor[i] / floor_sum end
  else
    for i = 1, ncol do
      w[i] = math.max(want[i], floor[i])
      if w[i] > MAX_W then w[i] = MAX_W end
    end
    -- water-fill: remove any overrun from SLACK ABOVE THE FLOORS only, so no
    -- column is pushed under its floor
    for _ = 1, 12 do
      local total = 0
      for i = 1, ncol do total = total + w[i] end
      local excess = total - 1.0
      if math.abs(excess) < 0.001 then break end
      if excess > 0 then
        local slack = 0
        for i = 1, ncol do slack = slack + (w[i] - floor[i]) end
        if slack <= 1e-6 then break end
        local keep = math.max(0, (slack - excess) / slack)
        for i = 1, ncol do w[i] = floor[i] + (w[i] - floor[i]) * keep end
      else
        -- under-subscribed: hand the remainder out by desired share
        local deficit = -excess
        for i = 1, ncol do w[i] = w[i] + deficit * want[i] end
      end
    end
  end

  for i = 1, ncol do
    tbl.colspecs[i] = { tbl.colspecs[i][1], w[i] }
  end
  return tbl
end
