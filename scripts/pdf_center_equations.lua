-- Centre display equations.
--
-- This paper writes display equations as a BLOCKQUOTE containing a code span:
--     > `Λ_residual ~ H²`  (R-119),
-- Pandoc renders that as an indented quotation, left-aligned. Conventionally a
-- display equation is centred, so this filter promotes qualifying blockquotes to
-- a centred paragraph.
--
-- THE DISCRIMINATOR, arrived at by measurement — two earlier attempts were wrong
-- in instructive ways, so both are recorded here to stop them being reintroduced.
--
--   Attempt 1: require code spans to be >= 40% of the visible text.
--   Wrong: this paper habitually annotates its equations inline —
--       > `sin²θ_W = 3/8` at the unification scale, (R-082)
--   The annotation is prose, so the share fell under the bar and a genuine
--   equation was left indented. ~30 equations were missed this way.
--
--   Attempt 2: reject anything containing bold, on the theory that bold marks
--   emphatic prose. Wrong in the other direction: the paper's most important
--   equations are bold code spans —
--       > **`c_meta⁻² · ∂²_{τ_5} Ψ = (∂_1² + ∂_2² + ∂_3² + ∂_4²) Ψ`**
--   so the rule rejected exactly the equations most deserving of display.
--
-- What actually separates the two populations is whether a CODE SPAN is present
-- at all, counted THROUGH any bold/italic wrapper. Genuine prose blockquotes in
-- this corpus are bold sentences with no code span; equations always carry one.
-- The share floor survives only as a weak guard against centring a paragraph that
-- merely mentions one symbol, and the length cap does the rest.

local stringify = pandoc.utils.stringify

local CODE_SHARE_MIN = 0.18   -- weak guard only; see attempt 1 above
local MAX_LEN        = 240    -- longer than this is a paragraph, not an equation

-- Count code spans anywhere in the inline tree, including inside Strong/Emph/Link.
local function code_content(inlines)
  local n, chars = 0, 0
  local function walk(list)
    for _, el in ipairs(list) do
      if el.t == "Code" then
        n = n + 1
        chars = chars + #el.text
      elseif el.content and type(el.content) == "table" then
        walk(el.content)
      end
    end
  end
  walk(inlines)
  return n, chars
end

function BlockQuote(el)
  -- Only single-paragraph quotes are candidates; a multi-block quote is prose.
  if #el.content ~= 1 or el.content[1].t ~= "Para" then
    return nil
  end

  local para = el.content[1]
  local n_code, code_chars = code_content(para.content)
  local total = #stringify(para)

  if n_code < 1 then return nil end          -- no symbol at all ⇒ prose
  if total == 0 or total > MAX_LEN then return nil end
  if (code_chars / total) < CODE_SHARE_MIN then return nil end

  -- Qualifies: emit a centred paragraph instead of an indented quotation.
  return {
    pandoc.RawBlock("latex", "\\begin{center}"),
    para,
    pandoc.RawBlock("latex", "\\end{center}"),
  }
end
