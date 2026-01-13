## Brief overview
Guidelines for how Cline should interact with the user and handle communication during this project.

## Communication style
- 日本語で応答すること。  
- 簡潔に、余計な前置きや締めくくりのフレーズは使用しない。  
- 必要に応じて、根拠や影響範囲を簡潔に説明する。  
- 不明点がある場合は **要件を明示した質問** を `ask_followup_question` ツールで行う。

## Development workflow
- 変更は必ず **ツール使用後にユーザーの確認** を得てから次のステップへ進む。  
- 変更が必要な場合は、**理由と影響範囲** を必ずコメントで示す。  
- タスク進捗は `task_progress` パラメータで常に更新する。

## Coding best practices (補足)
- 既存の `.clinerules/project-rule.md` に記載されている PEP8、型ヒント、docstring ルールを引き続き遵守する。  
- 新規ルールは既存ルールと矛盾しないようにする。

## Other guidelines
- ユーザーが指示しない限り、**ファイルやコードの振る舞いを変更しない**。  
- 変更が必要な場合は必ず **変更理由と影響範囲を明示** すること。  
- テストは `pytest` を前提とし、変更があればテスト追加・修正の提案を行う。
