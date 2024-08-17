import os
from flask import Flask, request
from github import Github, GithubIntegration
from loguru import logger
from dotenv import load_dotenv

# ロガーの設定
logger.add("github_bot.log", rotation="500 MB", encoding="utf-8")

app = Flask(__name__)

# .envファイルから環境変数を読み込む
load_dotenv()
app_id = os.getenv('GITHUB_APP_ID')
cert_path = os.getenv('GITHUB_PRIVATE_KEY_PATH')

# 証明書の読み込み
logger.info("ボットの証明書を読み込んでいます")
try:
    with open(cert_path, 'r') as cert_file:
        app_key = cert_file.read()
except FileNotFoundError:
    logger.error(f"証明書ファイルが見つかりません: {cert_path}")
    raise
except IOError:
    logger.error(f"証明書ファイルの読み込みに失敗しました: {cert_path}")
    raise

# GitHub integrationインスタンスの作成
logger.info("GitHub integrationインスタンスを作成しています")
git_integration = GithubIntegration(
    app_id,
    app_key,
)

@app.route("/", methods=['POST'])
def bot():
    logger.info("Webhookを受信しました")
    payload = request.json

    # GitHub PR作成イベントまたはIssue作成イベントのチェック
    if not (('pull_request' in payload and payload.get('action') == 'opened') or
            ('issue' in payload and payload.get('action') == 'opened')):
        logger.warning("PRまたはIssueの作成イベントではありません。無視します")
        return "ok"

    owner = payload['repository']['owner']['login']
    repo_name = payload['repository']['name']
    logger.info(f"{owner}/{repo_name}のイベントを処理しています")

    # botとしてのGit接続の取得
    logger.info("ボットとしてGit接続を取得しています")
    git_connection = Github(
        login_or_token=git_integration.get_access_token(
            git_integration.get_installation(owner, repo_name).id
        ).token
    )
    repo = git_connection.get_repo(f"{owner}/{repo_name}")

    if 'pull_request' in payload:
        issue = repo.get_issue(number=payload['pull_request']['number'])
        comment_text = "PRをありがとうございます！頑張ってレビューします。"
    else:
        issue = repo.get_issue(number=payload['issue']['number'])
        comment_text = "新しいIssueをありがとうございます！できるだけ早く対応します。"

    logger.info(f"Issue #{issue.number}を取得しました")

    # コメントを作成
    logger.info("コメントを作成しています")
    issue.create_comment(comment_text)
    logger.success("コメントの作成に成功しました")

    return "ok"

if __name__ == "__main__":
    logger.info("Flaskサーバーを起動しています")
    app.run(debug=True, port=5000)
