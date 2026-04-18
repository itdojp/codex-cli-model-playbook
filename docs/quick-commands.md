# Quick commands

Last reviewed: 2026-04-18 JST

## Purpose

This document provides a compact command reference for the main profiles in this playbook.

## Software development

### Default development session
```bash
codex -p software_dev
```

### Deep implementation session
```bash
codex -p software_dev_deep_impl
```

### Fast localized fix session
```bash
codex -p software_dev_fastfix
```

### Read-only investigation session
```bash
codex -p readonly
```

### Unattended long-running software task
```bash
codex exec -p autonomous_unattended "<task>"
```

## Technical writing

### Default technical authoring session
```bash
codex -p tech_book
```

### Broad consistency and terminology sweep
```bash
codex -p tech_book_bulk
```

### Read-only technical review session
```bash
codex -p tech_book_review
```

## Runtime compatibility check

### Check a single model
```bash
codex exec -m gpt-5.4 --skip-git-repo-check "Reply with OK only."
```

### Check the main candidate set
```bash
python3 scripts/check_codex_model_support.py \
  --models gpt-5.4 gpt-5.4-mini gpt-5.3-codex gpt-5.3-codex-spark gpt-5.2 \
  --summary-only --output notes/model-support.json
```

## Practical recommendation

If you are starting from zero, the minimal set to remember is:

- `codex -p software_dev`
- `codex -p software_dev_deep_impl`
- `codex -p software_dev_fastfix`
- `codex -p tech_book`
- `codex -p tech_book_review`
