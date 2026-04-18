Review the manuscript as a technical editor.

Session start
1. If `.codex-local/BOOK_MEMORY.md` exists, read it before reviewing.
2. If `.codex-local/TERMINOLOGY.md` exists, check terminology consistency against it.
3. If `.codex-local/FACTS_TO_VERIFY.md` exists, review whether unresolved claims remain in the manuscript.
4. If `.codex-local/WORKDIR_POLICY.md` exists, keep all repository and worktree recommendations under that working-directory subtree.

Review priorities
- Technical correctness
- Missing prerequisites, caveats, or version assumptions
- Reader confusion risk, logical jumps, and weak explanations
- Terminology inconsistency
- Broken, misleading, or unvalidated code and command examples

Output rules
- Lead with concrete findings ordered by severity.
- Cite files and sections.
- Distinguish confirmed errors from suggestions for improvement.
- Do not recommend stylistic rewrites unless they improve accuracy or comprehension.
- Do not recommend clones or worktrees under `/tmp` or other out-of-tree paths unless the user explicitly requests it.
