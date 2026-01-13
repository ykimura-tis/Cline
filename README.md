python -m venv .venv
chmod a+x .venv/bin/activate
source .venv/bin/activate
pip install -e .\[dev\]

---
curl -LsSf https://astral.sh/uv/install.sh | sh
# On Windows.
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
rm -rf .venv venv
uv venv
source .venv/bin/activate
uv lock
uv sync --extra dev
uv lock --upgrade

uv run pytest

===
export CONFIG_BUCKET=config                                         
export CONFIG_KEY=key                                               
pytest -vv test/common/test_config.py
pytest -vv test/myapp/test_app.py

===

get_user.pyのPythonコードをもっと良くしてください。
def get_user(id):
   return db.fetch(id)

.clinerules
- 既存コードを尊重する
- 既存コードの振る舞い（入力・出力・例外）を変えない

- 改善を行う
- 不要なリファクタリングを行わない	- 仕様追加を行わない


Clineは**「やっていいこと」より「やってはいけないこと」**を明確にすると安定します。
悪い例	きれいなコードを書くこと
良い例	- 不要なリファクタリングを行わない	 - 可読性を最優先する

👉 1プロンプト = 1責務 を厳守
✔ Clineは「実装・調査・下書き」に使う
✔ 設計・判断・責任は人間が持つ
✔ 小さく依頼し、頻繁にレビュー
✔ VS Code設定で品質を担保


# ---- 最重要 ----
- 既存コードの振る舞い（入力・出力・例外）を変えない
- 指示されていないファイルは変更しない
# ---- 判断ルール ----
- 不明点がある場合は仮定を明示し、実装は提案に留める
# ---- 改善の範囲 ----
- 可読性向上のみを目的とする
- 仕様追加・大規模リファクタは禁止
# ---- 説明 ----
- 変更理由を必ず説明する


===
このPythonコードを改善してください。
def calc_price(price, tax):
   return price + price * tax


推奨 .clinerules テンプレート（Python向け）
# ===============================
# Cline Project Rules
# ===============================

# ---- 基本方針 ----
- あなたはこのプロジェクトのPython開発アシスタントである
- 既存コードの振る舞いを変えてはならない
- 変更が必要な場合は必ず理由と影響範囲を説明すること

# ---- コード品質 ----
- PythonはPEP8に従うこと
- 可読性を最優先し、過度な最適化は行わない
- 明示的で分かりやすいコードを書くこと

# ---- 型・ドキュメント ----
- 可能な限り型ヒント（typing）を付与する
- public関数・クラスにはdocstringを記述する
- docstringはGoogle styleまたは簡潔な形式でよい

# ---- 変更ルール ----
- 指示されていないファイルは変更しない
- 不要なリファクタリングを行わない
- 既存のインターフェース（関数シグネチャ、戻り値）を壊さない

# ---- 不明点の扱い ----
- 要件が曖昧な場合は仮定を明示する
- 勝手な仕様追加を行わない

# ---- テスト ----
- 実装変更を行った場合はテスト追加・修正を提案する
- pytestを前提とする

# ---- セーフティ ----
- 破壊的操作（rm, DB削除, 本番設定変更）は行わない
- セキュリティ上問題がある実装は警告する


====

AIレビュー用プロンプト（固定化）

以下の変更についてAIレビューを行ってください。

観点:
- 既存コードの振る舞いを変えていないか
- 指示されていないファイルを変更していないか
- 不要なリファクタリングが含まれていないか
- 可読性・保守性に問題がないか
- 変更理由は妥当か

問題点があれば指摘し、
修正案があれば提案してください。


