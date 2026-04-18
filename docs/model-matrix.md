# Codex CLI model matrix

Last reviewed: 2026-04-18 JST

## Purpose

This document organizes the practical characteristics of the Codex CLI model lineup and converts them into operational guidance.

## Design principle

When selecting a model, evaluate it on four axes:

1. **orchestration quality**
   - suitable for planning, integration, review, and long-context judgment
2. **coding specialization**
   - suitable for implementation, diff generation, test-fix loops, and tool-heavy workflows
3. **speed and cost**
   - suitable for high-volume subagents or repeated short tasks
4. **account runtime support**
   - actually executable for the current account

## Model matrix

| Model | Official positioning | Practical role | Main strength | Main caution |
| --- | --- | --- | --- | --- |
| `gpt-5.4` | Frontier model for agentic, coding, and professional workflows | Parent/orchestrator | Best overall reasoning and long-context integration | Highest cost among current defaults |
| `gpt-5.4-mini` | Strongest mini model for coding, computer use, and subagents | Bulk subagent / editorial sweep | Good balance of speed, quality, and cost | Not ideal for final complex judgment |
| `gpt-5.3-codex` | Codex-optimized agentic coding model | Main implementation worker | Strong coding specialization and tool-heavy execution | Less ideal than `gpt-5.4` for top-level orchestration |
| `gpt-5.3-codex-spark` | Ultra-fast coding model | Speed-first low-risk fixes | Very fast short-cycle execution | Avoid for ambiguous or architecture-heavy tasks |
| `gpt-5.2` | Previous frontier model for professional work | Long-running unattended mixed workflows | Good long-running professional workflow coverage | Lower ceiling than `gpt-5.4` |
| `gpt-5.2-codex` | Long-horizon coding model | Theoretically suitable for deep coding | Strong official positioning for long-horizon coding | Runtime support may be unavailable by account |
| `gpt-5.1-codex-max` | Long-running Codex-oriented model | Fallback comparison candidate | Long-running coding orientation | Older generation and may be unavailable |
| `gpt-5.1-codex-mini` | Smaller, cheaper Codex model | Low-cost fallback | Cheap and fast | Lower capability and may be unavailable |

## Recommended usage by workload

### 1. Software architecture and implementation
- Parent: `gpt-5.4`
- Deep worker: `gpt-5.3-codex`
- Fast worker: `gpt-5.3-codex-spark`
- Long unattended run: `gpt-5.2`

### 2. Technical book writing
- Main authoring: `gpt-5.4`
- Structural/editorial sweep: `gpt-5.4-mini`
- Code sample execution and correction: `gpt-5.3-codex`

### 3. High-volume subagent operation
- Discovery, fact checks, lightweight editorial passes: `gpt-5.4-mini`
- Mechanical coding repairs: `gpt-5.3-codex-spark`

## Interpretation note

OpenAI docs describe **official capability positioning**.
Actual `codex exec` availability is controlled separately by account entitlement.
Therefore, operational design should always apply this sequence:

1. read official characteristics
2. test runtime support in the current account
3. assign profiles only to supported models

## Sources

- OpenAI Models overview: https://developers.openai.com/api/docs/models
- GPT-5.4: https://developers.openai.com/api/docs/models/gpt-5.4
- GPT-5.4 mini: https://developers.openai.com/api/docs/models/gpt-5.4-mini
- GPT-5.3-Codex: https://developers.openai.com/api/docs/models/gpt-5.3-codex
- GPT-5.2: https://developers.openai.com/api/docs/models/gpt-5.2
- GPT-5.2-Codex: https://developers.openai.com/api/docs/models/gpt-5.2-codex
- GPT-5.1-Codex-Max: https://developers.openai.com/api/docs/models/gpt-5.1-codex-max
- GPT-5.1-Codex-mini: https://developers.openai.com/api/docs/models/gpt-5.1-codex-mini
