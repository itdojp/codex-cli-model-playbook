# Profile catalog

Last reviewed: 2026-04-18 JST

## Purpose

This document explains the actual purpose-specific profiles used in the playbook.
It complements `docs/profile-design.md` by making the operational profile set explicit.

## Software development profiles

### `software_dev`
- Model: `gpt-5.4`
- Role: default interactive software engineering parent/orchestrator
- Use when:
  - you need planning, integration, review, and implementation in one session
  - the task is important enough that overall reasoning quality matters more than raw speed

### `software_dev_unattended`
- Model: `gpt-5.4`
- Role: unattended software development parent
- Use when:
  - you still want `gpt-5.4` as the top-level controller
  - the task may run longer without direct user interaction

### `software_dev_deep_impl`
- Model: `gpt-5.3-codex`
- Role: deep code-heavy implementation session
- Use when:
  - the work is mainly implementation, debugging, or repeated code/test cycles
  - a coding-specialized model is more important than top-level orchestration quality

### `software_dev_longrun`
- Model: `gpt-5.2`
- Role: long-running mixed professional workflow
- Use when:
  - the task is long-running and cost/runtime balance matters
  - the workflow mixes coding, reasoning, and operational execution

### `software_dev_fastfix`
- Model: `gpt-5.3-codex-spark`
- Role: speed-first low-risk repair session
- Use when:
  - the task is a small fix, mechanical edit, localized CI issue, or lint cleanup
- Avoid when:
  - architecture or requirement interpretation is involved

### `autopilot`
- Model: `gpt-5.3-codex`
- Role: coding-specialized implementation/test loop
- Use when:
  - you want the standard implementation loop with a Codex-oriented model

### `readonly`
- Model: `gpt-5.4`
- Role: high-confidence read-only investigation
- Use when:
  - you need strong investigation quality without file edits

## Technical writing profiles

### `tech_book`
- Model: `gpt-5.4`
- Role: primary technical book authoring
- Use when:
  - drafting or revising chapters
  - deciding explanation order and pedagogical structure

### `tech_book_bulk`
- Model: `gpt-5.4-mini`
- Role: high-volume editorial and consistency pass
- Use when:
  - checking terminology consistency
  - sweeping multiple sections for style or structure drift
  - performing broad but lower-risk content review

### `tech_book_review`
- Model: `gpt-5.4`
- Role: read-only technical manuscript review
- Use when:
  - you want correctness and comprehension review without editing the text directly

## Compatibility aliases

### `autonomous`
- Model: `gpt-5.4`
- Role: backward-compatible alias for the software-development parent profile

### `autonomous_unattended`
- Model: `gpt-5.2`
- Role: dedicated unattended long-running automation profile

### `book-review`
- Model: `gpt-5.4`
- Role: backward-compatible alias for technical manuscript review

## Practical recommendation

If you want a small and stable public profile set, you can present only these as the core set:

- `software_dev`
- `software_dev_deep_impl`
- `software_dev_fastfix`
- `tech_book`
- `tech_book_bulk`
- `tech_book_review`

Then keep `autonomous`, `autonomous_unattended`, and `book-review` as compatibility aliases.
