import os
import json
import sys
import re

def load_config():
    """Load configuration from config.json."""
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(script_dir, 'config.json')
        
        # Get the latest version information
        default_config = get_default_config()
        latest_version = default_config.get("version")
        
        # Load existing config
        config = None
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                if config_path.endswith('.json'):
                    config = json.load(f)
        
        if not config:
            config = default_config
        else:
            # Update version in config to match the latest version
            config["version"] = latest_version
            
            # Save the updated config with the correct version
            try:
                with open(config_path, 'w') as f:
                    json.dump(config, f, indent=4)
            except Exception:
                pass
                
        return config
    except Exception as e:
        print(f"Error loading config: {e}")
        return None

def get_default_config():
    """Get default configuration settings."""
    # Try to get version from environment or .version file
    version = "1.0.0"  # Default fallback version
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Check for .version file
    version_file = os.path.join(script_dir, '.version')
    if os.path.exists(version_file):
        try:
            with open(version_file, 'r') as f:
                version = f.read().strip()
        except Exception:
            pass
    
    # Check executable name for version info
    try:
        executable_path = os.path.basename(sys.executable)
        if 'CursorFocus_' in executable_path:
            version_match = re.search(r'CursorFocus_(\d+\.\d+\.\d+)', executable_path)
            if version_match:
                version = version_match.group(1)
    except Exception:
        pass
                
    return {
        "version": version,
        "project_path": "",
        "update_interval": 60,
        "max_depth": 3,
        "output_directory": ".me",
        "file_paths": {
            "focus": ".me/Focus.md",
            "me": ".me/Me.md",
            "rules": ".me/Rules.md"
        },
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
        ],
        "binary_extensions": [
            ".png", ".jpg", ".jpeg", ".gif", ".ico", ".pdf", ".exe", ".bin"
        ],
        "file_length_standards": {
            ".py": 400,    # Python
            ".js": 300,    # JavaScript
            ".ts": 300,    # TypeScript
            ".tsx": 300,   # TypeScript/React
            ".kt": 300,    # Kotlin
            ".php": 400,   # PHP
            ".swift": 400, # Swift
            ".cpp": 500,   # C++
            ".c": 500,     # C
            ".h": 300,     # C/C++ Header
            ".hpp": 300,   # C++ Header
            ".cs": 400,    # C#
            ".csx": 400,   # C# Script
            "default": 300
        }
    }

def save_config(config):
    """Save configuration to config.json file.
    
    Args:
        config (dict): The configuration dictionary to save
    """
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(script_dir, 'config.json')
        
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=4)
        return True
    except Exception as e:
        print(f"Error saving config: {e}")
        return False

# Load configuration once at module level
_config = load_config()

# Binary file extensions that should be ignored
BINARY_EXTENSIONS = set(_config.get('binary_extensions', []))

# Documentation and text files that shouldn't be analyzed for functions
NON_CODE_EXTENSIONS = {
    '.md', '.txt', '.log', '.json', '.yml', '.toml', '.ini', '.cfg',
    '.conf', '.config', '.markdown', '.rst', '.rdoc', '.csv', '.tsv'
}

# Extensions that should be analyzed for code
CODE_EXTENSIONS = {
    '.py',    # Python
    '.js',    # JavaScript
    '.ts',    # TypeScript
    '.tsx',   # TypeScript/React
    '.kt',    # Kotlin
    '.php',   # PHP
    '.swift', # Swift
    '.cpp',   # C++
    '.c',     # C
    '.h',     # C/C++ Header
    '.hpp',   # C++ Header
    '.cs',    # C#
    '.csx',   # C# Script
}

# Regex patterns for function detection
FUNCTION_PATTERNS = {
    # Python
    'python_function': r'def\s+([a-zA-Z_]\w*)\s*\(',
    'python_class': r'class\s+([a-zA-Z_]\w*)\s*[:\(]',
    
    # JavaScript/TypeScript
    'js_function': r'(?:^|\s+)(?:function\s+([a-zA-Z_]\w*)|(?:const|let|var)\s+([a-zA-Z_]\w*)\s*=\s*(?:async\s*)?function)',
    'js_arrow': r'(?:^|\s+)(?:const|let|var)\s+([a-zA-Z_]\w*)\s*=\s*(?:async\s*)?(?:\([^)]*\)|[^=])\s*=>',
    'js_method': r'\b([a-zA-Z_]\w*)\s*:\s*(?:async\s*)?function',
    'js_class_method': r'(?:^|\s+)(?:async\s+)?([a-zA-Z_]\w*)\s*\([^)]*\)\s*{',
    
    # PHP
    'php_function': r'(?:public\s+|private\s+|protected\s+)?function\s+([a-zA-Z_]\w*)\s*\(',
    
    # C/C++
    'cpp_function': r'(?:virtual\s+)?(?:static\s+)?(?:inline\s+)?(?:const\s+)?(?:\w+(?:::\w+)*\s+)?([a-zA-Z_]\w*)\s*\([^)]*\)(?:\s*const)?(?:\s*noexcept)?(?:\s*override)?(?:\s*final)?(?:\s*=\s*0)?(?:\s*=\s*default)?(?:\s*=\s*delete)?(?:{|;)',
    
    # C#
    'csharp_method': r'(?:public|private|protected|internal|static|virtual|override|abstract|sealed|async)\s+(?:\w+(?:<[^>]+>)?)\s+([a-zA-Z_]\w*)\s*\([^)]*\)',
    
    # Kotlin
    'kotlin_function': r'(?:fun\s+)?([a-zA-Z_]\w*)\s*(?:<[^>]+>)?\s*\([^)]*\)(?:\s*:\s*[^{]+)?\s*{',
    
    # Swift
    'swift_function': r'(?:func\s+)([a-zA-Z_]\w*)\s*(?:<[^>]+>)?\s*\([^)]*\)(?:\s*->\s*[^{]+)?\s*{'
}

# Keywords that should not be treated as function names
IGNORED_KEYWORDS = {
    'if', 'switch', 'while', 'for', 'catch', 'finally', 'else', 'return',
    'break', 'continue', 'case', 'default', 'to', 'from', 'import', 'as',
    'try', 'except', 'raise', 'with', 'async', 'await', 'yield', 'assert',
    'pass', 'del', 'print', 'in', 'is', 'not', 'and', 'or', 'lambda',
    'global', 'nonlocal', 'class', 'def'
}

# Names of files and directories that should be ignored
IGNORED_NAMES = set(_config.get('ignored_directories', []))

FILE_LENGTH_STANDARDS = _config.get('file_length_standards', {})

def get_file_length_limit(file_path):
    """Get the recommended line limit for a given file type."""
    ext = os.path.splitext(file_path)[1].lower()
    return FILE_LENGTH_STANDARDS.get(ext, FILE_LENGTH_STANDARDS.get('default', 300)) 