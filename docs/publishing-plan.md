# Publishing plan

## Current public repository

- https://github.com/itdojp/codex-cli-model-playbook

## Goal

Publish this playbook in two forms:

1. a reusable GitHub repository
2. a Japanese article that explains the design and links to the repository

## Better publication strategy

Instead of publishing only a narrative article, publish a **small operational kit**:

- docs that explain the model strategy
- a sample config
- reusable agent examples
- a runtime compatibility checker
- a Japanese article draft that points back to the repository

This makes the work maintainable and reusable.

## GitHub repository checklist

1. Review the repository name.
   - recommended: `codex-cli-model-playbook`
2. Confirm whether the repository should be public or private.
3. Review the sample config and replace local paths with placeholders.
4. Decide the license.
5. Push the repository.
6. Add screenshots or command captures if needed.

## Japanese article checklist

1. Replace placeholder repository URL.
2. Replace placeholder command output if you want to show real screenshots.
3. Add a short section on what changed after the redesign.
4. Add links to official OpenAI docs.
5. Link to the repository for templates and scripts, without hard-coding a publication platform into repo file names.

## Suggested article structure

1. Why the model picker alone is not enough
2. How to separate model roles
3. How to verify account-level runtime support
4. Actual profile mapping used in practice
5. Public repository and reusable assets

## Files prepared in this repository

- `README.md`
- `docs/model-matrix.md`
- `docs/profile-design.md`
- `docs/account-compatibility.md`
- `examples/config.sample.toml`
- `examples/agents/*.toml`
- `scripts/check_codex_model_support.py`
- `LICENSE`
- `articles/ja/codex-cli-model-redesign-ja.md`
