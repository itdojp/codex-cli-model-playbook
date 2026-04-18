# Codex CLI Model Playbook

A reusable playbook for designing Codex CLI model roles, profile mappings, and account-level compatibility checks.

Repository URL: https://github.com/itdojp/codex-cli-model-playbook

日本語要約:
- Codex CLI のモデル選定を「親エージェント」「実装エージェント」「高速修正」「長時間無人実行」「技術書執筆」に分けて設計するための公開用資料です。
- OpenAI 公式 docs のモデル特性と、実際の `codex exec` によるアカウント別の実行可否を切り分けて扱います。
- GitHub 公開用のドキュメント、サンプル設定、Qiita 記事草案、モデル互換性チェック用スクリプトを含みます。

## Why this repository exists

Codex CLI users often face two problems:

1. The model picker shows multiple candidate models, but their practical roles are unclear.
2. A model that appears in the picker is not always executable for the current account.

This repository addresses both issues by separating:

- **official model characteristics** from OpenAI docs
- **runtime compatibility** verified with `codex exec`
- **operational profile design** for real workflows

## Contents

- `docs/model-matrix.md`
  - Characteristics of each Codex CLI model and recommended usage.
- `docs/profile-design.md`
  - Recommended profile architecture for software engineering and technical book authoring.
- `docs/account-compatibility.md`
  - How to test what the current account can actually execute.
- `docs/publishing-plan.md`
  - How to publish this as a GitHub repository and turn it into a Qiita article.
- `docs/repository-metadata.md`
  - Suggested repository name, description, and topic tags.
- `examples/config.sample.toml`
  - Sample Codex configuration based on the documented design.
- `examples/agents/`
  - Sample subagent definitions.
- `scripts/check_codex_model_support.py`
  - Runtime support checker for the current Codex account.
- `articles/qiita/codex-cli-model-redesign-ja.md`
  - Draft Qiita article in Japanese.

## Better public release strategy

Use a two-layer publication model:

1. **GitHub repository** for durable reusable assets
   - sample config
   - agent definitions
   - checker scripts
   - versioned docs
2. **Qiita article** for narrative explanation and discovery
   - motivation
   - design rationale
   - lessons learned
   - link back to the repository

This is more reusable than publishing only an article.

## Recommended operating model

### Software development
- Parent/orchestrator: `gpt-5.4`
- Deep implementation: `gpt-5.3-codex`
- Fast small fixes: `gpt-5.3-codex-spark`
- Long unattended execution: `gpt-5.2`

### Technical book authoring
- Main authoring: `gpt-5.4`
- Bulk consistency/editorial sweep: `gpt-5.4-mini`
- Code sample verification: `gpt-5.3-codex`

## Important principle

Do not rely only on what the picker shows.
Always verify the target model with a real command such as:

```bash
codex exec -m gpt-5.4 --skip-git-repo-check "Reply with OK only."
```

## Quick start

### 1. Check runtime support in your account

```bash
python3 scripts/check_codex_model_support.py \
  --models gpt-5.4 gpt-5.4-mini gpt-5.3-codex gpt-5.3-codex-spark gpt-5.2 \
  --summary-only --output notes/model-support.json
```

### 2. Start from the sample config

```bash
cp examples/config.sample.toml ~/.codex/config.toml
```

Then customize paths, approval policy, and project trust settings.

### 3. Read the design docs

Start with:
- `docs/model-matrix.md`
- `docs/profile-design.md`

## Basis

This repository assumes:
- Codex CLI 0.121.0 or later
- OpenAI model documentation checked on 2026-04-18 JST
- The actual executable model set can differ by account entitlement

See the source links in each document.
