# Codex CLI のモデル設計を見直した話: GPT-5.4 を親、Codex 系を実装役に分離する

> 本稿は、公開用リポジトリ `https://github.com/itdojp/codex-cli-model-playbook` を前提に、運用設計の考え方を解説するための日本語記事原稿です。

## この記事で分かること

- Codex CLI のモデルを「親」「実装」「高速修正」「長時間無人実行」「技術書執筆」でどう分けるか
- picker に表示されるモデルと、実際に使うべきモデルをどう切り分けるか
- その判断を再利用可能なドキュメントや設定サンプルに落とす方法

## 前提

本稿の前提は次の通りです。

- Codex CLI: `0.121.0`
- 確認日: `2026-04-18 JST`
- OpenAI 公式 docs を参照している
- 実際の採用可否は `codex exec` による runtime check を優先している

## はじめに

Codex CLI のモデル選択画面を見ると、以下のように複数の候補が並びます。

- `gpt-5.4`
- `gpt-5.2-codex`
- `gpt-5.1-codex-max`
- `gpt-5.4-mini`
- `gpt-5.3-codex`
- `gpt-5.3-codex-spark`
- `gpt-5.2`
- `gpt-5.1-codex-mini`

ただ、実運用で重要なのは「一覧にあること」ではなく、次の 3 点です。

1. それぞれが何に向くのか
2. 親エージェントと子エージェントをどう分けるか
3. 自分のアカウントで本当に実行できるか

## 結論

現時点の推奨は次の通りです。

### ソフトウェア開発
- 親エージェント: `gpt-5.4`
- 深い実装: `gpt-5.3-codex`
- 高速な小修正: `gpt-5.3-codex-spark`
- 長時間無人実行: `gpt-5.2`

### 技術書執筆
- 主担当: `gpt-5.4`
- 大量の整合性確認・用語揃え: `gpt-5.4-mini`
- コード例の修正: `gpt-5.3-codex`

## 再設計前に起きていた問題

モデル一覧だけを見ると、すべてが同じレイヤーの選択肢に見えます。しかし実際には、必要な役割は異なります。

- 親として全体計画を扱う役割
- 実装を継続的に進める役割
- lint や局所 CI のような高速修正役
- 長時間の unattended run を回す役割
- 技術書の説明構造を組み立てる役割

この役割分離をしないと、重いモデルを雑務に使ったり、逆に軽いモデルに設計判断をさせたりして、運用品質が不安定になります。

## なぜ `gpt-5.4` を親にするのか

OpenAI の公式 docs では、`gpt-5.4` は agentic / coding / professional workflows 向けの frontier model とされています。

実務上も、親エージェントには以下の役割が必要です。

- 全体計画
- 文脈保持
- 複数 subagent の結果統合
- 難所での最終判断

この役割は、実装専任のモデルより `gpt-5.4` の方が安定します。

## なぜ実装役を Codex 系に分けるのか

一方で、実装や test-fix loop は別の性質を持ちます。

- コード差分の生成
- CLI ツールとの往復
- テスト修正の反復
- ローカルな変更の収束

この層では、Codex 最適化モデルの方が自然です。

そのため、親は `gpt-5.4`、実装役は `gpt-5.3-codex` という分離が実務上扱いやすくなりました。

## picker に出ても使えないモデルがある

ここが今回の重要点でした。

OpenAI 公式 docs 上では `gpt-5.2-codex` や `gpt-5.1-codex-max` も確認できます。しかし、実際に `codex exec` で試すと、アカウントによっては実行できません。

例えば、以下のように実確認します。

```bash
codex exec -m gpt-5.4 --skip-git-repo-check "Reply with OK only."
codex exec -m gpt-5.3-codex --skip-git-repo-check "Reply with OK only."
codex exec -m gpt-5.2-codex --skip-git-repo-check "Reply with OK only."
```

つまり、判断手順は次の順番にすべきです。

1. OpenAI docs でモデル特性を確認する
2. `codex exec` で runtime support を確認する
3. 実行できるモデルだけを profile に割り当てる

## 実際に使っている profile 構成

| 用途 | profile | model |
| --- | --- | --- |
| 通常のソフトウェア開発 | `software_dev` | `gpt-5.4` |
| 深い実装 | `software_dev_deep_impl` | `gpt-5.3-codex` |
| 高速修正 | `software_dev_fastfix` | `gpt-5.3-codex-spark` |
| 長時間無人実行 | `autonomous_unattended` | `gpt-5.2` |
| 技術書執筆 | `tech_book` | `gpt-5.4` |
| 大量の整合性確認 | `tech_book_bulk` | `gpt-5.4-mini` |
| 技術書レビュー | `tech_book_review` | `gpt-5.4` |

## 起動コマンドの実例

### ソフトウェア開発
```bash
codex -p software_dev
codex -p software_dev_deep_impl
codex -p software_dev_fastfix
codex exec -p autonomous_unattended "<task>"
```

### 技術書執筆
```bash
codex -p tech_book
codex -p tech_book_bulk
codex -p tech_book_review
```

## 公開リポジトリに入れたもの

- モデル特性の整理表
- プロファイル設計ドキュメント
- 用途別 profile カタログ
- picker 表示モデルと実運用モデルの差分整理
- アカウント互換性チェック手順
- `config.sample.toml`
- `deep_coder`, `fast_worker` のサンプル subagent 定義
- ソフトウェア開発用・技術書執筆用・技術書レビュー用の instruction examples
- `scripts/check_codex_model_support.py`

単なる説明記事ではなく、再利用できる運用キットとして公開する方針です。

## 今後の運用ルール

- モデルは「表示されるか」ではなく「実行できるか」で採用する
- 親と子で役割を分ける
- 高速小修正専用の profile を分ける
- 新しいモデルが出たら、まず `codex exec` で動作確認する
- profile と instruction file はセットで管理する

## まとめ

Codex CLI のモデル設計では、モデル名そのものよりも次の切り分けが重要です。

- 司令塔か
- 実装役か
- 高速雑務役か
- 長時間無人運転か
- 執筆主担当か

そして、OpenAI docs の情報に加えて、**自分のアカウントで本当に走るか** を検証してから profile に反映するのが、安全な運用だと考えています。

公開リポジトリ:
- `https://github.com/itdojp/codex-cli-model-playbook`

公式 docs:
- https://developers.openai.com/api/docs/models
- https://developers.openai.com/api/docs/models/gpt-5.4
- https://developers.openai.com/api/docs/models/gpt-5.4-mini
- https://developers.openai.com/api/docs/models/gpt-5.3-codex
- https://developers.openai.com/api/docs/models/gpt-5.2
