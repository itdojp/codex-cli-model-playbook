# Model availability and actual usage status

Last reviewed: 2026-04-18 JST
Codex CLI version assumed: 0.121.0

## Purpose

This document separates three different concepts that are often conflated:

1. models visible in the Codex picker
2. models documented by OpenAI
3. models actually assigned in this playbook

## Model set seen in the local picker

The following model identifiers were visible in the local Codex CLI model picker at review time:

- `gpt-5.4`
- `gpt-5.2-codex`
- `gpt-5.1-codex-max`
- `gpt-5.4-mini`
- `gpt-5.3-codex`
- `gpt-5.3-codex-spark`
- `gpt-5.2`
- `gpt-5.1-codex-mini`

## Models actually used in this playbook

### Assigned to active profiles
- `gpt-5.4`
- `gpt-5.4-mini`
- `gpt-5.3-codex`
- `gpt-5.3-codex-spark`
- `gpt-5.2`

### Not assigned to active profiles
- `gpt-5.2-codex`
- `gpt-5.1-codex-max`
- `gpt-5.1-codex-mini`

## Why some picker models are not used

Because the current account-level runtime check rejected them.
A model can be visible in the picker but still fail at runtime for the current account.

## Runtime support example in the reviewed environment

Supported:
- `gpt-5.4`
- `gpt-5.4-mini`
- `gpt-5.3-codex`
- `gpt-5.3-codex-spark`
- `gpt-5.2`

Rejected at runtime:
- `gpt-5.2-codex`
- `gpt-5.1-codex-max`
- `gpt-5.1-codex-mini`

Representative error:

```text
The '<model>' model is not supported when using Codex with a ChatGPT account.
```

## Operational interpretation

### `gpt-5.4`
Used as the orchestration and top-level reasoning model.

### `gpt-5.4-mini`
Used for lighter, higher-volume work such as broad editorial passes or read-only subagents.

### `gpt-5.3-codex`
Used as the main coding-specialized implementation model.

### `gpt-5.3-codex-spark`
Used only for fast low-risk tasks.

### `gpt-5.2`
Used for long-running unattended workflows where runtime/cost balance matters.

## Source of truth for the checked result

- Human-readable summary: this document
- Machine-readable sample: `examples/model-support.20260418.example.json`
- Reproducible command: `scripts/check_codex_model_support.py`
