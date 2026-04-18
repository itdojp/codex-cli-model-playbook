# Profile design for Codex CLI

## Objective

Design profiles around **work roles**, not around model names alone.

The stable approach is:
- decide the role first
- choose the lightest model that satisfies the role
- validate that the account can actually execute it

## Recommended profile architecture

### Software engineering

| Profile | Model | Intended role |
| --- | --- | --- |
| `software_dev` | `gpt-5.4` | default parent/orchestrator |
| `software_dev_unattended` | `gpt-5.4` | unattended parent with high but not maximal effort |
| `software_dev_deep_impl` | `gpt-5.3-codex` | deep code-heavy implementation |
| `software_dev_longrun` | `gpt-5.2` | long-running mixed workflow |
| `software_dev_fastfix` | `gpt-5.3-codex-spark` | fast localized fixes |
| `autopilot` | `gpt-5.3-codex` | implementation/test loop |
| `readonly` | `gpt-5.4` | high-confidence investigation |

### Technical book authoring

| Profile | Model | Intended role |
| --- | --- | --- |
| `tech_book` | `gpt-5.4` | chapter authoring and major revision |
| `tech_book_bulk` | `gpt-5.4-mini` | high-volume terminology and consistency sweep |
| `tech_book_review` | `gpt-5.4` | read-only technical review |

## Recommended subagent architecture

| Subagent | Model | Role |
| --- | --- | --- |
| `explorer` | `gpt-5.4-mini` | read-only codebase mapping |
| `docs_researcher` | `gpt-5.4-mini` | official docs lookup |
| `fact_checker` | `gpt-5.4-mini` | bounded verification |
| `citation_checker` | `gpt-5.4-mini` | source verification |
| `log_analyzer` | `gpt-5.4-mini` | noisy log compression |
| `worker` | `gpt-5.3-codex` | normal implementation |
| `deep_coder` | `gpt-5.3-codex` | deep single-track implementation |
| `fast_worker` | `gpt-5.3-codex-spark` | speed-first mechanical fixes |
| `test_runner` | `gpt-5.3-codex` | targeted verification |
| `reviewer` | `gpt-5.4` | final correctness review |
| `security_reviewer` | `gpt-5.4` | security review |
| `writer` | `gpt-5.4` | manuscript drafting |
| `editor` | `gpt-5.4` | editorial review |
| `outline_designer` | `gpt-5.4` | chapter structure planning |

## Why this design is robust

### 1. The parent stays stronger than the workers
The parent must plan, prioritize, integrate evidence, and decide escalation.
That role benefits most from `gpt-5.4`.

### 2. Implementation uses coding-specialized models
Worker profiles are optimized for code edits, test loops, and CLI-driven repair.
That role maps naturally to `gpt-5.3-codex`.

### 3. Speed-first tasks are isolated
Low-risk repetitive tasks should use a dedicated fast profile.
This avoids burning high-end model budget on trivial work.

### 4. Technical writing is not treated as coding
Book work is mainly about structure, explanation quality, terminology, and correctness.
That remains a `gpt-5.4` strength, with `gpt-5.4-mini` reserved for high-volume editorial passes.

## Operational rules

1. Do not assign unsupported models to active default profiles.
2. Validate each new model with `codex exec -m <model>` before operational adoption.
3. Keep explicit documentation for why each profile exists.
4. Separate orchestration, implementation, and fast-fix roles.
5. Re-review profile mapping whenever model entitlements change.
