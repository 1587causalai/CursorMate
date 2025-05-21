# Project Rules

## Project Information
- **Version**: 1.0.0
- **Last Updated**: January 27, 2025 at 01:06 AM
- **Name**: CursorMate
- **Language**: markdown
- **Framework**: none
- **Type**: application

## Project Description
This project is designed to enhance code development by automatically analyzing project structures, generating coding rules, and providing personalized project summaries. It leverages AI to create customized rules for Cursor IDE and monitors project changes in real-time, offering developers a more focused and efficient workflow with tailored project insights and documentation. The system also includes an auto-updater to keep the tool current, making it a comprehensive solution for project management and code analysis.

## AI Behavior Rules

### Code Generation Style
#### Preferred Patterns
- Use snake_case for variables and functions (e.g., `file_path`, `check_for_updates`).
- Use PascalCase for classes (e.g., `AutoUpdater`, `RulesGenerator`).
- Use a consistent indentation of 4 spaces.
- Keep lines within a reasonable length (around 100 characters) to improve readability.
- Use type hints for function arguments and return values.
- Use f-strings for string formatting.
- Use docstrings to document the purpose of functions, classes, and modules.
- Use blank lines to separate logical blocks of code and improve readability.
- Use descriptive variable names.
- Use list comprehensions where appropriate.
- Use explicit imports rather than wildcard imports.

#### Patterns to Avoid
- CamelCase for variables or functions.
- Inconsistent indentation.
- Long lines of code.
- Missing type hints.
- String concatenation instead of f-strings.
- Missing docstrings.
- Overly complex code structures.
- Unclear variable names.
- Wildcard imports (e.g., `from module import *`).

### Error Handling
#### Preferred Patterns
- Use `try...except` blocks to catch potential errors.
- Log errors using the `logging` module.
- Return `None` or `False` to indicate failure.
- Provide informative error messages.
- Use specific exception types where appropriate (e.g., `FileNotFoundError`, `requests.exceptions.RequestException`).
- Catch general `Exception` in top-level functions to prevent crashes, and log the exception.

#### Patterns to Avoid
- Bare `except` statements.
- Ignoring errors without logging them.
- Returning generic error messages.
- Raising exceptions without a proper catch.

### Performance
#### Preferred Patterns
- Use sets for membership testing (e.g., `if ext in CODE_EXTENSIONS:`).
- Use list comprehensions for generating lists.
- Avoid unnecessary file reads and writes.
- Cache results where appropriate.
- Use `os.path.join` for path construction.
- Use `os.path.exists` to check for file existence before attempting to open or process.
- Use `os.scandir` for efficient directory traversal.
- Use `set` for faster lookups.
- Process large files line by line, rather than reading the entire file into memory, if possible.

#### Patterns to Avoid
- Inefficient loops.
- Unnecessary file operations.
- Reading large files into memory without line-by-line processing.
- Redundant calculations.
- String concatenation within loops.

### Module Organization
#### Structure
- The project is organized into multiple Python modules.
- Each module has a specific responsibility.
- Configuration is centralized in the `config.py` file.
- The `setup.py` is used to configure the project and manage project settings.
- The `focus.py` is the main entry point for the application, responsible for setting up the project environment and monitoring project changes.
- The project uses a mix of procedural and object-oriented programming styles.

#### Dependencies
- `auto_updater.py` depends on `os`, `requests`, `json`, `shutil`, `datetime`, `logging`, `typing`, `tempfile`, `zipfile`.
- `analyzers.py` depends on `os`, `re`, `config`, `logging`.
- `rules_generator.py` depends on `os`, `json`, `typing`, `datetime`, `google.generativeai`, `re`, `rules_analyzer`, `dotenv`, `config`.
- `project_detector.py` depends on `os`, `json`, `re`, `config`, `time`, `typing`.
- `config.py` depends on `os`, `json`.
- `me_generator.py` depends on `os`, `datetime`, `typing`, `content_generator`, `config`.
- `rules_watcher.py` depends on `os`, `time`, `typing`, `watchdog.observers`, `watchdog.events`, `rules_generator`, `project_detector`, `config`.
- `rules_analyzer.py` depends on `os`, `json`, `typing`.
- `setup.py` depends on `os`, `json`, `argparse`, `logging`, `project_detector`.
- `content_generator.py` depends on `os`, `datetime`, `analyzers`, `project_detector`, `config`, `re`, `logging`, `typing`.
- `focus.py` depends on `os`, `time`, `datetime`, `typing`, `config`, `content_generator`, `rules_analyzer`, `rules_generator`, `rules_watcher`, `logging`, `auto_updater`, `me_generator`.

#### Module Responsibilities
- **auto_updater.py**: Handles updating the application by checking for new versions on GitHub and applying updates.
- **analyzers.py**: Analyzes file content to detect functions and determine if files should be ignored.
- **rules_generator.py**: Generates rules for Cursor IDE based on project analysis using Gemini AI.
- **project_detector.py**: Detects the type of project (e.g., Python, JavaScript) based on file indicators and content.
- **config.py**: Manages project configuration settings, including file paths, ignored files, and code style settings.
- **me_generator.py**: Generates personal activity and project focus summary for the Me.md file.
- **rules_watcher.py**: Monitors project directories for changes and triggers updates to the .cursorrules file.
- **rules_analyzer.py**: Analyzes project metadata like name, language, and framework.
- **setup.py**: Provides command-line interface to manage the projects to monitor and configure application settings.
- **content_generator.py**: Generates the content for the Focus.md file, including project structure and function information.
- **focus.py**: Main application entry point; manages project monitoring, content generation, and updates.

#### Rules
- Each module should have a clear and specific responsibility.
- Modules should avoid tight coupling with each other.
- Configuration settings should be loaded from `config.py`.
- Logging should be used for error handling and debugging.
- Type hints should be used consistently throughout the project.
- Error handling should be implemented using `try...except` blocks.
- Project-specific settings should be stored in `config.json`.

#### Naming Conventions
- **modules**: Module names use snake_case (e.g., `rules_generator`, `auto_updater`).
- **classes**: Class names use PascalCase (e.g., `RulesGenerator`, `AutoUpdater`).
- **functions**: Function names use snake_case (e.g., `generate_rules_file`, `check_for_updates`).
- **variables**: Variable names use snake_case (e.g., `project_path`, `config`).
- **constants**: Constants use UPPER_SNAKE_CASE (e.g., `BINARY_EXTENSIONS`, `IGNORED_NAMES`).
