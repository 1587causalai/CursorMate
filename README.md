# CursorFocus

A lightweight tool that maintains a focused view of your project structure and environment. CursorFocus automatically tracks your project files, functions, and environment variables, updating every 60 seconds to keep you informed of changes.

Check out our [SHOWCASE.md](SHOWCASE.md) for detailed examples and real-world use cases!


## Discord

Join our Discord server to discuss features, ask questions: [Discord](https://discord.gg/7MjqwynP)

## Features

- 🔄 Real-time project structure tracking
- 📝 Automatic file and function documentation
- 🌳 Hierarchical directory visualization
- 📏 File length standards and alerts
- 🎯 Project-specific information detection
- 🔍 Smart project type detection (Chrome Extension, Node.js, Python)
- 🧩 Modular and extensible design
- 🎛️ Automatic .cursorrules generation and project adaptation

## Quick Start

1. Clone CursorFocus into your project:
   ```bash
   git clone https://github.com/RenjiYuusei/CursorFocus.git
   ```

2. Make the run script executable:
   ```bash
   chmod +x CursorFocus/run.sh
   ```

3. Start CursorFocus:
   ```bash
   ./CursorFocus/run.sh
   ```

That's it! CursorFocus will automatically:
- Create necessary configuration
- Install dependencies
- Start monitoring your project
- Generate Focus.md documentation

## Multi-Project Support

CursorFocus can monitor multiple projects simultaneously. There are two ways to set this up:

### 1. Automatic Project Detection

Run CursorFocus with the scan option to automatically detect projects:
```bash
python3 CursorFocus/setup.py --scan /path/to/projects/directory
```

This will:
- Scan the directory for supported project types
- List all detected projects
- Let you choose which projects to monitor

### 2. Manual Configuration

Edit `config.json` to add multiple projects:
```json
{
    "projects": [
        {
            "name": "Project 1",
            "project_path": "/path/to/project1",
            "type": "node_js",
            "watch": true
        },
        {
            "name": "Project 2",
            "project_path": "/path/to/project2",
            "type": "chrome_extension",
            "watch": true
        }
    ]
}
```

Each project can have its own:
- Custom update interval
- Ignored patterns
- File length standards
- Project-specific rules

### Project Types Supported:
- Chrome Extensions (detected by manifest.json)
- Node.js Projects (detected by package.json)
- Python Projects (detected by setup.py or pyproject.toml)
- React Applications (detected by src/App.js)
- Generic Projects (basic structure)

## Alternative Setup Methods

### Manual Setup

If you prefer to set up manually:

1. Install dependencies (Python 3.6+ required):
   ```bash
   cd CursorFocus
   pip install -r requirements.txt
   ```

2. Create/edit config.json (optional)
3. Run the script:
   ```bash
   python3 focus.py
   ```

## Generated Files

CursorFocus automatically generates and maintains three key files:

1. **Focus.md**: Project documentation and analysis
   - Project overview and structure
   - File descriptions and metrics
   - Function documentation
   
2. **.cursorrules**: Project-specific Cursor settings
   - Automatically generated based on project type
   - Customized for your project's structure
   - Updates as your project evolves
   


## Setup

1. Clone or copy the CursorFocus directory to your project:
   ```bash
   git clone https://github.com/RenjiYuusei/CursorFocus.git CursorFocus
   ```

2. Install dependencies (Python 3.6+ required):
   ```bash
   cd CursorFocus
   pip install -r requirements.txt
   ```

3. Run the script:
   ```bash
   python3 focus.py
   ```

## Automatic Startup (macOS)

To have CursorFocus start automatically when you log in:

1. Create a LaunchAgent configuration:
   ```bash
   mkdir -p ~/Library/LaunchAgents
   ```

2. Create the file `~/Library/LaunchAgents/com.cursorfocus.plist` with:
   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
   <dict>
       <key>Label</key>
       <string>com.cursorfocus</string>
       <key>ProgramArguments</key>
       <array>
           <string>/usr/local/bin/python3</string>
           <string>/path/to/your/CursorFocus/focus.py</string>
       </array>
       <key>RunAtLoad</key>
       <true/>
       <key>StandardOutPath</key>
       <string>/tmp/cursorfocus.log</string>
       <key>StandardErrorPath</key>
       <string>/tmp/cursorfocus.err</string>
       <key>KeepAlive</key>
       <true/>
   </dict>
   </plist>
   ```
   
   Replace `/path/to/your/CursorFocus/focus.py` with the actual path to your focus.py file.

3. Load the LaunchAgent:
   ```bash
   launchctl load ~/Library/LaunchAgents/com.cursorfocus.plist
   ```

4. To stop the automatic startup:
   ```bash
   launchctl unload ~/Library/LaunchAgents/com.cursorfocus.plist
   ```

## Output

CursorFocus generates a `Focus.md` file in your project root with:

1. Project Overview
   - Project name and description
   - Key features and version
   - Project type detection

2. Project Structure
   - Directory hierarchy
   - File descriptions
   - Function listings with detailed descriptions
   - File type detection
   - File length alerts based on language standards

3. Code Analysis
   - Key function identification
   - Detailed function descriptions
   - File length standards compliance

## Configuration

Edit `config.json` to customize:

```json
{
    "project_path": "",
    "update_interval": 60,
    "max_depth": 3,
    "ignored_directories": [
        "__pycache__",
        "node_modules",
        "venv",
        ".git",
        ".idea",
        ".vscode",
        "dist",
        "build",
        "coverage"
    ],
    "ignored_files": [
        ".DS_Store",
        "Thumbs.db",
        "*.pyc",
        "*.pyo",
        "package-lock.json",
        "yarn.lock"
    ]
}
```

## File Length Standards

CursorFocus includes built-in file length standards for different file types:

- JavaScript/TypeScript:
  - Regular files: 300 lines
  - React components (.jsx/.tsx): 250 lines

- Python files: 400 lines

- Style files:
  - CSS/SCSS/LESS/SASS: 400 lines

- Template files:
  - HTML: 300 lines
  - Vue/Svelte components: 250 lines

- Configuration files:
  - JSON/YAML/TOML: 100 lines

- Documentation files:
  - Markdown/RST: 500 lines

The tool will alert you when files exceed these recommended limits.

## Project Structure

```
CursorFocus/
├── focus.py           # Main entry point
├── analyzers.py       # File and code analysis
├── config.py          # Configuration management
├── content_generator.py # Focus file generation
├── project_detector.py # Project type detection
├── config.json        # User configuration
└── requirements.txt   # Dependencies
```

## Supported Project Types

CursorFocus automatically detects and provides specialized information for:

- Chrome Extensions (manifest.json)
- Node.js Projects (package.json)
- Python Projects (setup.py, pyproject.toml)
- Generic Projects (basic structure)


## Contributing

Contributions are welcome! Please feel free to submit pull requests or create issues for bugs and feature requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 