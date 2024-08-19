## github-app-sandbox

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
>Nearly 90% of the release notes, README, and commit messages in this repository are generated using [claude.ai](https://claude.ai/), [ChatGPT4](https://chatgpt.com/), and our AI tools: [AIRA](https://github.com/Sunwood-ai-labs/AIRA), [SourceSage](https://github.com/Sunwood-ai-labs/SourceSage), [Gaiah](https://github.com/Sunwood-ai-labs/Gaiah), and [HarmonAI_II](https://github.com/Sunwood-ai-labs/HarmonAI_II).

## 🌟 Getting Started

This repository provides a sandbox for GitHub App development. It offers an environment to safely develop, test, and improve your GitHub Apps without affecting your production environment.

## 🚀 Sandbox Projects

### 📬 [s01_github_pr_issue_greeter](./sandbox/s01_github_pr_issue_greeter)

This is a minimal GitHub App sample implemented in Python. It provides basic functionality to automatically respond when a new pull request or issue is created. This is ideal for understanding the basic structure and operation of GitHub Apps. For details, see [here](./sandbox/s01_github_pr_issue_greeter/README.md).

### 📮 [s02_simple_event_responder](./sandbox/s02_simple_event_responder)

This is a more advanced GitHub App sample created using FastAPI and Docker. It responds to various GitHub events with customizable responses. It is suitable for learning how to implement event filtering and conditional actions. For details, see [here](./sandbox/s02_simple_event_responder/README.md).

## 🎥 Demo

https://github.com/user-attachments/assets/7ce109ec-3913-491f-9566-f488dd31e689

## 🚀 Getting Started

1. **Clone the repository**:
   ```
   git clone https://github.com/Sunwood-ai-labs/github-app-sandbox.git
   cd github-app-sandbox
   ```

2. **Install Docker**:
   - Install Docker from the [official Docker website](https://www.docker.com/get-started).

3. **Set up the environment**:
   - Copy the `.env.example` file to `.env` and fill in the required information.
   ```
   cp .env.example .env
   ```

4. **Create a GitHub App**:
   - Create a new GitHub App in your GitHub's [Developer Settings](https://github.com/settings/developers).
   - Set the necessary permissions and specify the Webhook URL.
   - Download the generated private key and store it in a secure location.

5. **Run the sandbox**:
   - Build and run the application using Docker according to the README of each sandbox project.

For detailed instructions, refer to the README of each sandbox project.

## 📝 Update Information

- [🎉 v0.3.1 Released](https://github.com/Sunwood-ai-labs/github-app-sandbox/releases/tag/v0.3.1) 🟢 : Added [s02_simple_event_responder](./sandbox/s02_simple_event_responder), clarified the use of FastAPI and Docker, updated the English README, added a use case image, and added documentation badges.
- [🎉 v0.2.0 Released](https://github.com/Sunwood-ai-labs/github-app-sandbox/releases/tag/v0.2.0) 🟢 : Created a minimal GitHub App sample in Python, [s01_github_pr_issue_greeter](./sandbox/s01_github_pr_issue_greeter).
- [🎉 v0.1.0 Released](https://github.com/Sunwood-ai-labs/github-app-sandbox/releases/tag/v0.1.0) 🟢 : Initial repository setup and added automatic release notes creation functionality.

## 🤝 Contributions

We welcome contributions from the community! You can contribute in the following ways:

1. **Report issues**: If you find a bug or have an idea for a new feature, please open an issue on GitHub.

2. **Submit pull requests**: If you've made improvements to the code or added new features, please submit a pull request.

3. **Improve the documentation**: If you have suggestions for improving the README or other documentation, please submit a pull request.

4. **Share your use cases**: If you have developed a GitHub App using this sandbox, please share it with us!

When contributing, please follow these guidelines:

- Keep your commit messages clear and concise.
- Open an issue to discuss major changes before making them.

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 🙏 Acknowledgements

- This project was developed using [Claude AI](https://www.anthropic.com) from [Anthropic](https://www.anthropic.com).
- We are grateful to [GitHub](https://github.com) for providing a fantastic platform and API.
- We would like to thank all the [contributors](https://github.com/Sunwood-ai-labs/github-app-sandbox/graphs/contributors) who have contributed to the development of this project.
- Thanks to the authors and maintainers of all the open source libraries used in this project, such as [PyGithub](https://github.com/PyGithub/PyGithub), [Flask](https://flask.palletsprojects.com/), and [python-dotenv](https://github.com/theskumar/python-dotenv).

We sincerely appreciate your support and feedback. We will continue to work together to make this project better.