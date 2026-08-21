-- Markdown tables require a literal pipe inside a code span to be written  \|
-- GitHub renders that as  |  ; pandoc keeps the backslash literal inside `code`,
-- so the PDF showed  \|V_us\|²  instead of  |V_us|² .
--
-- This filter runs on the PARSED AST — after the table structure has already been
-- resolved from the unescaped pipes — so stripping the backslash here is safe and
-- cannot corrupt columns. 64 occurrences across the paper and companion.
--
-- Note for future edits: the pattern must be a literal backslash followed by a
-- pipe, which in Lua source is written "\\|". Writing "\|" is an invalid escape
-- sequence and pandoc aborts with exit 83.

function Code(el)
  el.text = el.text:gsub("\\|", "|")
  return el
end
