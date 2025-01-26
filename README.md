## [All rights belong to RenjiYuusei please do not steal the source code or modify the source code without the author's consent. Please respect the author](https://github.com/RenjiYuusei/CursorMate)

## CursorMate

A lightweight tool that maintains a focused view of your project structure and environment. CursorMate automatically tracks your project files, functions, and environment variables, updating every 60 seconds to keep you informed of changes.

Check out our [SHOWCASE.md](SHOWCASE.md) for detailed examples and real-world use cases!

## Discord

Join our Discord server to discuss features, ask questions: [Discord](https://discord.gg/N6FBdRZ8sw)

## Features

- 🧠 Personal-specific context and query
- 🤖 AI-powered **personalized context** generation
- 🔄 Real-time project structure tracking
- 📝 Automatic contextual documentation
- 🌳 Hierarchical directory visualization
- 🎯 Project-specific adaptation
- 🔍 Thinking evolution tracking

## Installation
```
irm https://raw.githubusercontent.com/RenjiYuusei/CursorMate/refs/heads/main/install.ps1 | iex
```

这条命令通过PowerShell直接从GitHub下载并立即执行CursorMate的安装脚本（`irm`下载脚本，`iex`执行内容），实现一键安装，但需注意直接运行远程代码的安全风险。

## Requirements

- Python 3.10+
- Gemini API Key (required for AI-powered features)

## API Key Setup

Before running CursorMate, you need to set up your Gemini API key:

1. Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

2. Set up the environment variable:

   For Windows:

   ```bash
   set GEMINI_API_KEY=your_api_key_here
   ```

   For Mac/Linux:

   ```bash
   export GEMINI_API_KEY=your_api_key_here
   ```

   To make it permanent:

   - Windows: Add to system environment variables
   - Mac/Linux: Add to `~/.bashrc`, `~/.zshrc`, or equivalent shell config file

   Extra: Set manual environment variable
   Create a file called `.env` in the root of the project and add the following:
   ```bash
   GEMINI_API_KEY=your_api_key_here
   ```


## Multi-Project Support

CursorMate can monitor multiple projects simultaneously. There are two ways to set this up:


### Manual Setup

If you prefer to set up manually:

1. Install dependencies (Python 3.10+ required):

   ```bash
   cd CursorMate
   pip install -r requirements.txt
   ```

2. Run the setup script:
   ```bash
   python setup.py --p path/to/your/project
   ```

3. Run the script:
   ```bash
   python focus.py
   ```

## Generated Files

CursorMate automatically generates and maintains three key files:

1. **Focus.md**: Project documentation and analysis
   - Project overview and structure
   - File descriptions and metrics
   - Function documentation
2. **Rules.md**: Project-specific Cursor settings
   - 是 .cursorrules 文件的候选内容
   - Automatically generated based on project type
   - Customized for your project's structure
   - Updates as your project evolves
3. **Me.md**: Personal information, 基本框架是:
   - 个人简历信息
   - 12个正在做的项目信息
   - 个人的认知内核

These three files are generated in the `.me` directory by default.


## License

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details.
