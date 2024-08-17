![](../../docs/usage/usage_01.png)


# 📬 GitHub PR Issue Greeter

このプロジェクトは、GitHubリポジトリに新しいプルリクエスト（PR）やIssueが作成されたときに自動的に応答するボットです。

## 🌟 機能

- 🔔 新しいPRが作成されたときに自動的にコメントを付けます。
- 📝 新しいIssueが作成されたときに自動的にコメントを付けます。
- 📊 ログ機能により、ボットの動作を追跡できます。

## 🛠️ セットアップ

1. このリポジトリをクローンします。

2. 必要な依存関係をインストールします：

   ```
   pip install flask PyGithub loguru python-dotenv
   ```

3. [smee.io](https://smee.io/)にアクセスし、新しいWebhook Proxy URLを取得します。

4. `.env.example`ファイルを`.env`にコピーし、必要な情報を入力します：

   ```
   cp .env.example .env
   ```

   `.env`ファイルの内容：
   ```
   GITHUB_APP_ID=your_app_id_here
   GITHUB_PRIVATE_KEY_PATH=path_to_your_private_key.pem
   ```

5. GitHubアプリケーションを作成し、必要な権限を設定します。
   - Webhook URLには、手順3で取得したsmee.ioのURLを設定します。

6. 証明書（PEMファイル）をダウンロードし、`GITHUB_PRIVATE_KEY_PATH`で指定したパスに配置します。

## 🚀 使用方法

1. smeeクライアントを起動して、Webhookをローカルサーバーにフォワードします：

   ```
   smee -u https://smee.io/your_unique_url --port 5000
   ```

2. 別のターミナルウィンドウで、Flaskアプリケーションを起動します：

   ```
   python app.py
   ```

3. GitHubリポジトリで新しいPRやIssueを作成し、ボットの動作を確認します。

## 🔧 開発環境

- Python 3.10
- 必要なライブラリ: Flask, PyGithub, loguru, python-dotenv
- smee-client (npm経由でインストール: `npm install --global smee-client`)

## 🎨 カスタマイズ

- `bot`関数内のロジックを変更することで、PRやIssueへの応答をカスタマイズできます。
- ログの設定は`logger.add()`の呼び出しで変更できます。

## 🤝 コントリビューション

プルリクエストや新機能の提案を歓迎します。大きな変更を加える前に、まずIssueを開いて議論してください。

## 📄 ライセンス

[MITライセンス](LICENSE)

## 📞 連絡先

質問や提案がある場合は、Issueを開いてください。
