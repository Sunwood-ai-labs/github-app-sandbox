import os
from github import Github, GithubIntegration
from loguru import logger

class GithubBot:
    def __init__(self):
        logger.info("GithubBotの初期化を開始します")
        self.setup_logger()
        self.setup_github_integration()
        logger.success("GithubBotの初期化が完了しました")

    def setup_logger(self):
        logger.info("ログ設定を構成中...")
        logger.add("github_bot.log", rotation="500 MB", encoding="utf-8")
        logger.success("ログ設定が完了しました")

    def setup_github_integration(self):
        logger.info("GitHub統合の設定を開始します")
        
        logger.info("環境変数を読み込んでいます")
        app_id = os.getenv('GITHUB_APP_ID')
        private_key_path = os.getenv('GITHUB_PRIVATE_KEY')

        if not app_id:
            logger.error("GITHUB_APP_ID環境変数が設定されていません")
            raise ValueError("GITHUB_APP_ID環境変数が設定されていません。")
        else:
            logger.info("GITHUB_APP_IDを正常に読み込みました")

        if not private_key_path:
            logger.error("GITHUB_PRIVATE_KEY環境変数が設定されていません")
            raise ValueError("GITHUB_PRIVATE_KEY環境変数が設定されていません。")
        else:
            logger.info(f"GITHUB_PRIVATE_KEYのパスを正常に読み込みました: {private_key_path}")

        # 秘密鍵をファイルから読み込む
        try:
            with open(private_key_path, 'r') as key_file:
                private_key = key_file.read()
            logger.info("秘密鍵をファイルから正常に読み込みました")
        except FileNotFoundError:
            logger.error(f"秘密鍵ファイルが見つかりません: {private_key_path}")
            raise
        except IOError as e:
            logger.error(f"秘密鍵ファイルの読み込み中にエラーが発生しました: {str(e)}")
            raise

        logger.info("GitHubインテグレーションを初期化中...")
        try:
            self.git_integration = GithubIntegration(app_id, private_key)
            logger.success("GitHubインテグレーションの初期化に成功しました")
        except Exception as e:
            logger.error(f"GitHubインテグレーションの設定中にエラーが発生しました: {str(e)}")
            raise
        
    def process_event(self, payload):
        logger.info("Webhookを受信しました")

        if not (('pull_request' in payload and payload.get('action') == 'opened') or
                ('issue' in payload and payload.get('action') == 'opened')):
            logger.warning("PRまたはIssueの作成イベントではありません。無視します。")
            return {"status": "無視されました"}

        owner = payload['repository']['owner']['login']
        repo_name = payload['repository']['name']
        logger.info(f"{owner}/{repo_name}のイベントを処理しています")

        logger.info("GitHubリポジトリへの接続を確立中...")
        git_connection = self.get_git_connection(owner, repo_name)
        repo = git_connection.get_repo(f"{owner}/{repo_name}")
        logger.success("GitHubリポジトリへの接続が確立されました")

        if 'pull_request' in payload:
            issue = repo.get_issue(number=payload['pull_request']['number'])
            comment_text = "🌟PRをありがとうございます！できるだけ早くレビューいたします。"
            logger.info(f"PR #{issue.number} にコメントを追加します")
        else:
            issue = repo.get_issue(number=payload['issue']['number'])
            comment_text = "🌟新しいIssueをありがとうございます！できるだけ早く対応いたします。"
            logger.info(f"Issue #{issue.number} にコメントを追加します")

        issue.create_comment(comment_text)
        logger.success("コメントの作成に成功しました")

        return {"status": "成功"}

    def get_git_connection(self, owner, repo_name):
        logger.info(f"{owner}/{repo_name} のGitHubインスタンスを取得中...")
        connection = Github(
            login_or_token=self.git_integration.get_access_token(
                self.git_integration.get_installation(owner, repo_name).id
            ).token
        )
        logger.success(f"{owner}/{repo_name} のGitHubインスタンスの取得に成功しました")
        return connection
