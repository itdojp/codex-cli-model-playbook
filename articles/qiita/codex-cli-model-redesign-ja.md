# Codex CLI のモデル設計を見直した話: GPT-5.4 を親、Codex 系を実装役に分離する

> この記事は公開用リポジトリの補足記事です。サンプル設定、互換性チェックスクリプト、subagent 定義は以下の GitHub リポジトリに置く想定です。  
> `https://github.com/itdojp/codex-cli-model-playbook`

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

本稿では、Codex CLI のモデル運用を再設計した内容を整理します。

## 結論

私の現時点の推奨は次の通りです。

### ソフトウェア開発
- 親エージェント: `gpt-5.4`
- 深い実装: `gpt-5.3-codex`
- 高速な小修正: `gpt-5.3-codex-spark`
- 長時間無人実行: `gpt-5.2`

### 技術書執筆
- 主担当: `gpt-5.4`
- 大量の整合性確認・用語揃え: `gpt-5.4-mini`
- コード例の修正: `gpt-5.3-codex`

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

## Picker に出ても使えないモデルがある

ここが今回の重要点でした。

OpenAI 公式 docs 上では `gpt-5.2-codex` や `gpt-5.1-codex-max` も確認できます。しかし、実際に `codex exec` で試すと、アカウントによっては実行できません。

例えば、以下のように実確認します。

```bash
codex exec -m gpt-5.4 --skip-git-repo-check "Reply with OK only."
codex exec -m gpt-5.3-codex --skip-git-repo-check "Reply with OK only."
codex exec -m gpt-5.2-codex --skip-git-repo-check "Reply with OK only."
```

この差分を吸収するために、公開リポジトリには互換性チェックスクリプトを入れました。

## 公開リポジトリに入れたもの

- モデル特性の整理表
- プロファイル設計ドキュメント
- アカウント互換性チェック手順
- `config.sample.toml`
- `deep_coder`, `fast_worker` のサンプル subagent 定義
- `scripts/check_codex_model_support.py`

単なる説明記事ではなく、再利用できる運用キットとして公開する方針です。

## 今後の運用ルール

- モデルは「表示されるか」ではなく「実行できるか」で採用する
- 親と子で役割を分ける
- 高速小修正専用の profile を分ける
- 新しいモデルが出たら、まず `codex exec` で動作確認する

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
