![](../../docs/usage/usage_02.png)

このプロジェクトは、GitHubリポジトリに新しいプルリクエスト（PR）やIssueが作成されたときに自動的に応答するボットです。

## 🌟 機能

- 🔔 新しいPRが作成されたときに自動的にコメントを付けます。
- 📝 新しいIssueが作成されたときに自動的にコメントを付けます。
- 📊 ログ機能により、ボットの動作を追跡できます。
- 🐳 Dockerを使用して簡単にデプロイとスケーリングが可能です。

## 🛠️ セットアップ

1. このリポジトリをクローンします。

2. `.env.example`ファイルを`.env`にコピーし、必要な情報を入力します：

   ```
   cp .env.example .env
   ```

   `.env`ファイルの内容：
   ```
   GITHUB_APP_ID=あなたのアプリIDをここに
   GITHUB_PRIVATE_KEY=あなたの秘密鍵をここに
   ```

3. GitHubアプリケーションを作成し、必要な権限を設定します。
   - Webhook URLには、ngrokなどのサービスを使用してローカルサーバーを公開することができます。

4. GitHubアプリケーションの秘密鍵をダウンロードし、その内容を`.env`ファイルの`GITHUB_PRIVATE_KEY`変数に貼り付けます。

## 🚀 使用方法

1. Dockerコンテナをビルドして実行します：

   ```
   docker-compose up --build
   ```

2. FastAPIアプリケーションが`http://localhost:8000`で利用可能になります。

3. GitHubアプリのWebhookを、公開されたエンドポイントに設定します。

4. GitHubリポジトリで新しいPRやIssueを作成して、ボットの動作を確認します。


## 🔧 開発環境

- Python 3.9
- FastAPI
- Docker と Docker Compose
- 必要なライブラリ: PyGithub, python-dotenv, loguru, pytest

## 🎨 カスタマイズ

- `github_bot.py`ファイルを変更して、ボットのPRやIssueへの応答をカスタマイズできます。
- `GithubBot`クラスの`setup_logger`メソッドでログ設定を調整できます。

## 🤝 コントリビューション

プルリクエストや新機能の提案を歓迎します。大きな変更を加える前に、まずIssueを開いて議論してください。

## 📄 ライセンス

[MITライセンス](LICENSE)

## 📞 連絡先

質問や提案がある場合は、Issueを開いてください。
