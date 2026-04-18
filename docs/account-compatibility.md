# Account compatibility and runtime support

## Why this matters

The Codex picker can display models that are not actually executable for the current account.
Operationally, this means you must distinguish between:

- **documented availability**
- **picker visibility**
- **runtime support for your account**

## Required check

Use a real command:

```bash
codex exec -m gpt-5.4 --skip-git-repo-check "Reply with OK only."
```

Repeat it for every candidate model you want to assign to an active profile.

## Reusable checker script

This repository includes:

```bash
python3 scripts/check_codex_model_support.py \
  --models gpt-5.4 gpt-5.4-mini gpt-5.3-codex gpt-5.3-codex-spark gpt-5.2 \
  --summary-only --output notes/model-support.json
```

## Interpreting the result

### Supported
The command returns `OK` and exits successfully.

### Unsupported by the current account
The command may return an error such as:

```text
The '<model>' model is not supported when using Codex with a ChatGPT account.
```

In that case:
- do not bind the model to an active default profile
- record it in documentation as officially exposed but currently unusable

## Example decision rule

1. If `gpt-5.4` works, use it for orchestration.
2. If `gpt-5.3-codex` works, use it for implementation.
3. If `gpt-5.3-codex-spark` works, use it for fast fixes.
4. If `gpt-5.2` works, use it for long-running unattended runs.
5. If `gpt-5.2-codex` does not work, do not assign it even if the docs recommend it.

## Recommended documentation pattern

Every public write-up should include:
- validation date
- Codex CLI version
- account context, if relevant
- which models were officially documented
- which models actually ran in your environment
