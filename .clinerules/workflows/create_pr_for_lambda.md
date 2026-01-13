# Workflow: create_pr_for_lambda

## 概要
このWorkflowは、Git差分（git diff）を入力として、
AWS Lambda（Python）向けの GitHub Pull Request を作成するための
タイトルおよび本文を生成する。

対象:
- 2人チーム
- Python / AWS Lambda
- main ブランチ向け PR

---

## 前提条件
- 差分は `git diff main...HEAD` の結果を使用する
- 差分は要約せず全文を入力する
- Lambda関数は handler を持つ前提とする

---

## 入力
- git_diff  
  `git diff main...HEAD` の出力全文

---

## 手順

### Step 1: 差分の目的を分析する

以下の git_diff を読み取り、変更の目的と背景を整理してください。

観点:
- なぜこの変更が必要か
- 解決している問題
- 新規追加か既存修正か

入力:
{{git_diff}}

出力:
- 変更目的の要約（箇条書き）

---

### Step 2: AWS Lambda への影響範囲を抽出する

Step 1 の結果と git_diff を元に、
AWS Lambda への影響を以下の形式で整理してください。

各項目は「◯ / × / 要確認」で回答してください。

- handler関数の変更
- 環境変数の追加・変更
- IAM権限への影響
- Event（API Gateway / SQS 等）の互換性
- コールドスタートへの影響
- 実行時間・メモリへの影響

---

### Step 3: Pull Request タイトルを生成する

これまでの分析結果を元に、
GitHub Pull Request のタイトルを1行で生成してください。

ルール:
- 動詞から始める
- Lambdaの責務が分かること
- 50文字以内
- 英語で記述する

例:
- Fix error handling in user registration Lambda
- Add retry logic to SQS consumer Lambda

---

### Step 4: Pull Request 本文を生成する

以下のフォーマットで、
GitHub Pull Request 本文を Markdown 形式で生成してください。

概要
（変更の目的を1〜2行で）
変更内容
・主な変更点を箇条書き
・ファイル名が分かれば含める
Lambda影響範囲
・handler変更: ◯ / × / 要確認
・環境変数: ◯ / × / 要確認
・IAM権限: ◯ / × / 要確認
・Event互換性: ◯ / × / 要確認
・パフォーマンス影響: ◯ / × / 要確認
テスト内容
・実施したテスト内容
・自動 / 手動 の別
補足
・レビュアーが注意すべき点


---

## 出力
- Pull Request タイトル
- Pull Request 本文（Markdown）

