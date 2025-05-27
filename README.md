# CursorFocus

CursorFocus is a tool that automatically analyzes software codebases to generate dynamic context files (`Focus.md`, `.cursorrules`) specifically designed to enhance the code comprehension and code generation capabilities of the Cursor AI IDE.

> 真正的灵魂拷问是我为什么不直接让它生成呢？意思是说我在这个开发环境中使用一个提示词直接让他生成这两个文件就行了？

## 项目结构
- `test_api.py` - 测试 Gemini API
- `patterns_analyzer.py` - 分析代码模式
- `me_generator.py` - 生成 Me.md 文件
- `rules_watcher.py` - 监控规则文件
- `setup.py` - 设置项目
- `config.py` - 配置管理
- `focus.py` - 创建和监控上下文文件
- `analyzers.py` - 分析文件内容
- `rules_generator.py` - 创建 .cursorrules 文件
- `content_generator.py` - 创建 Focus.md 文件
- `project_detector.py` - 检测项目类型
- `cli.py` - 主命令行界面
- `ui.py` - 用户界面组件
- `core.py` - 核心应用功能
- `config.py` - 配置管理
- `focus.py` - 创建和监控上下文文件
- `analyzers.py` - 分析文件内容
- `rules_generator.py` - 创建 .cursorrules 文件
- `content_generator.py` - 创建 Focus.md 文件
- `project_detector.py` - 检测项目类型

## Main Features

- **Automatic Analysis**: Identify and analyze software projects
- **Context Optimization**: Generate `.cursorrules` and `Focus.md` files to optimize context for AI
- **Real-time Monitoring**: Track project changes and update context files
- **Google Gemini AI Integration**: Use AI to generate high-quality project context
- **Modern Interface**: Intuitive and user-friendly command-line interface

## Installation
[Install here](https://github.com/RenjiYuusei/CursorFocus/releases)

### Requirements

- Python 3.8 or higher
- Google Gemini API Key (obtained from [Google AI Studio](https://makersuite.google.com/app/apikey))

### Install from source

1. Clone repository:
```
git clone https://github.com/yourusername/cursorfocus.git
cd cursorfocus
```

2. Install the dependencies:
```
pip install -r requirements.txt
```

3. Run the application:
```
python cli.py
```

## Usage

### Setting up the project

1. From the main menu, select the "Setup new project" option

2. Enter the path to the project folder

3. Enter the project name (or leave it blank to use the folder name)

4. Add the Gemini Google API key when prompted

5. Optionally configure advanced options (update interval, scan depth)

### Scanning projects

1. Select the "Scan for projects" option from the main menu

2. Enter the folder path to scan for projects

3. Select the projects you want to add to the configuration

### Monitoring projects

1. Select the "Start monitoring" option from main menu

2. Select the projects you want to monitor

3. Optionally enable automatic updates when changes are made

4. Press Ctrl+C to stop monitoring

### Batch update

1. Select the "Batch update" option from the main menu

2. Select the projects you want to update

3. Wait for the update to complete

## Using the command line

CursorFocus also supports command line parameters for automated tasks:

```
usage: cli.py [-h] [--setup SETUP] [--monitor] [--scan SCAN] [--update] [--list]
[--batch-update] [--headless]

CursorFocus - Automatically analyze and create context for Cursor AI IDE

optional arguments:

-h, --help show this help message and exit
--setup SETUP, -s SETUP
Setup a project with the given path
--monitor, -m Start monitoring configured projects
--scan SCAN Scan directory for projects
--update, -u Check for updates
--list, -l List configured projects
--batch-update, -b Batch update all projects
--headless Run in headless mode without interactive prompts

```

### Generated Files

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

## Project structure

- `cli.py` - Main command line interface
- `ui.py` - User interface components
- `core.py` - Core application functionality
- `config.py` - Configuration management
- `focus.py` - Creating and monitoring context files
- `analyzers.py` - Analyzing file content
- `rules_generator.py` - Creating .cursorrules files
- `content_generator.py` - Creating Focus.md files
- `project_detector.py` - Detecting project types

## Contribute

Contributing to the project is always welcome! Please create an issue or pull request on the GitHub repository.

## License

This project is distributed under the GPL-3.0 License.