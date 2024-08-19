<p align="center">
<img src="https://huggingface.co/datasets/MakiAi/IconAssets/resolve/main/github-app-sandbox2.png" width="60%">
<br>
<h1 align="center">github-app-sandbox</h1>
<h2 align="center">
  ～ Craft, Test, and Launch Your Apps in a Safe Space ～
<br>
  <img alt="PyPI - Version" src="https://img.shields.io/pypi/v/github-app-sandbox">
<img alt="PyPI - Format" src="https://img.shields.io/pypi/format/github-app-sandbox">
<img alt="PyPI - Implementation" src="https://img.shields.io/pypi/implementation/github-app-sandbox">
<img alt="PyPI - Status" src="https://img.shields.io/pypi/status/github-app-sandbox">
<img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dd/github-app-sandbox">
<img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dw/github-app-sandbox">
<a href="https://github.com/Sunwood-ai-labs/github-app-sandbox" title="Go to GitHub repo"><img src="https://img.shields.io/static/v1?label=github-app-sandbox&message=Sunwood-ai-labs&color=blue&logo=github"></a>
<img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/Sunwood-ai-labs/github-app-sandbox">
<a href="https://github.com/Sunwood-ai-labs/github-app-sandbox"><img alt="forks - Sunwood-ai-labs" src="https://img.shields.io/github/forks/github-app-sandbox/Sunwood-ai-labs?style=social"></a>
<a href="https://github.com/Sunwood-ai-labs/github-app-sandbox"><img alt="GitHub Last Commit" src="https://img.shields.io/github/last-commit/Sunwood-ai-labs/github-app-sandbox"></a>
<a href="https://github.com/Sunwood-ai-labs/github-app-sandbox"><img alt="GitHub Top Language" src="https://img.shields.io/github/languages/top/Sunwood-ai-labs/github-app-sandbox"></a>
<img alt="GitHub Release" src="https://img.shields.io/github/v/release/Sunwood-ai-labs/github-app-sandbox?color=red">
<img alt="GitHub Tag" src="https://img.shields.io/github/v/tag/Sunwood-ai-labs/github-app-sandbox?sort=semver&color=orange">
<img alt="GitHub Actions Workflow Status" src="https://img.shields.io/github/actions/workflow/status/Sunwood-ai-labs/github-app-sandbox/publish-to-pypi.yml">
<br>
<p align="center">
  <a href="https://hamaruki.com/"><b>[🌐 Website]</b></a> •
  <a href="https://github.com/Sunwood-ai-labs"><b>[🐱 GitHub]</b></a>
  <a href="https://x.com/hAru_mAki_ch"><b>[🐦 Twitter]</b></a> •
  <a href="https://hamaruki.com/"><b>[🍀 Official Blog]</b></a>

<a href="https://github.com/Sunwood-ai-labs/github-app-sandbox/blob/main/README.md"><img src="https://img.shields.io/badge/ドキュメント-日本語-white.svg" alt="JA doc"/></a>
<a href="https://github.com/Sunwood-ai-labs/github-app-sandbox/blob/main/docs/README.en.md"><img src="https://img.shields.io/badge/english-document-white.svg" alt="EN doc"></a>
  
</p>

</h2>




</p>

>[!IMPORTANT]
>このリポジトリのリリースノートやREADME、コミットメッセージの9割近くは[claude.ai](https://claude.ai/)や[ChatGPT4](https://chatgpt.com/)を活用した[AIRA](https://github.com/Sunwood-ai-labs/AIRA), [SourceSage](https://github.com/Sunwood-ai-labs/SourceSage), [Gaiah](https://github.com/Sunwood-ai-labs/Gaiah), [HarmonAI_II](https://github.com/Sunwood-ai-labs/HarmonAI_II)で生成しています。

## 🌟 はじめに

このリポジトリは、GitHub App 開発用のサンドボックスです。GitHub App の開発、テスト、改善を本番環境に影響を与えることなく安全に行うための環境を提供します。

## 🚀 サンドボックスプロジェクト

### 📬 [s01_github_pr_issue_greeter](./sandbox/s01_github_pr_issue_greeter)

新しいプルリクエストやIssueが作成されたときに自動的に応答するボットです。詳細は[こちら](./sandbox/s01_github_pr_issue_greeter/README.md)をご覧ください。

## 🎥 デモ

https://github.com/user-attachments/assets/7ce109ec-3913-491f-9566-f488dd31e689


## 🚀 はじめ方

1. **リポジトリのクローン**:
   ```
   git clone https://github.com/Sunwood-ai-labs/github-app-sandbox.git
   cd github-app-sandbox
   ```

2. **依存関係のインストール**:
   ```
   pip install -r requirements.txt
   ```

3. **環境設定**:
   - `.env.example`ファイルを`.env`にコピーし、必要な情報を入力します。
   ```
   cp .env.example .env
   ```

4. **GitHub Appの作成**:
   - GitHubの[Developer Settings](https://github.com/settings/developers)で新しいGitHub Appを作成します。
   - 必要な権限を設定し、Webhook URLを指定します。
   - 生成された秘密鍵をダウンロードし、安全な場所に保存します。

5. **サンドボックスの実行**:
   - 各サンドボックスプロジェクトのREADMEに従って、アプリケーションを実行します。

詳細な手順については、各サンドボックスプロジェクトのREADMEをご参照ください。


## 📝 更新情報

- [🎉 v0.2.0 リリース](https://github.com/Sunwood-ai-labs/github-app-sandbox/releases/tag/v0.2.0) 🟢 ：最小構成のgithub app pythonの[s01_github_pr_issue_greeter](./sandbox/s01_github_pr_issue_greeter)を作成
- [🎉 v0.1.0 リリース](https://github.com/Sunwood-ai-labs/github-app-sandbox/releases/tag/v0.1.0) 🟢 ：リポジトリの初期化・自動リリースノート作成機能の付与

## 🤝 コントリビューション

私たちは、コミュニティからの貢献を歓迎します！以下の方法で貢献できます：

1. **イシューの報告**: バグを見つけた場合や新機能のアイデアがある場合は、GitHubのIssueを開いてください。

2. **プルリクエストの提出**: コードの改善や新機能の追加を行った場合は、プルリクエストを送ってください。

3. **ドキュメントの改善**: READMEや他のドキュメントの改善案がある場合は、プルリクエストを送ってください。

4. **使用例の共有**: このサンドボックスを使用して開発したGitHub Appがある場合は、ぜひ共有してください。

コントリビューションの際は、以下のガイドラインに従ってください：

- コミットメッセージは明確で簡潔にしてください。
- 大きな変更を加える前に、まずIssueを開いて議論してください。

## 📄 ライセンス

このプロジェクトは[MITライセンス](LICENSE)の下で公開されています。

## 🙏 謝辞

- このプロジェクトは、[Anthropic](https://www.anthropic.com)の[Claude AI](https://www.anthropic.com)を活用して開発されました。
- [GitHub](https://github.com)には、素晴らしいプラットフォームとAPIを提供していただき感謝いたします。
- このプロジェクトの開発に貢献してくださったすべての[コントリビューター](https://github.com/Sunwood-ai-labs/github-app-sandbox/graphs/contributors)の皆様に感謝いたします。
- [PyGithub](https://github.com/PyGithub/PyGithub)、[Flask](https://flask.palletsprojects.com/)、[python-dotenv](https://github.com/theskumar/python-dotenv)など、このプロジェクトで使用されているすべてのオープンソースライブラリの作者とメンテナーの皆様に感謝いたします。

皆様のサポートとフィードバックに心から感謝いたします。このプロジェクトをより良いものにするために、引き続きご協力をお願いいたします。

