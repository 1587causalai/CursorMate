# Project Rules

## Project Information
- **Version**: 1.0.0
- **Last Updated**: January 26, 2025 at 08:59 PM
- **Name**: CursorFocus
- **Language**: markdown
- **Framework**: none
- **Type**: application

## Project Description
```
{
  "project_description": "This project is a code analysis and documentation tool designed to provide developers with insights into their projects. It automatically generates project documentation, coding style rules, and personal activity metrics, enhancing understanding and consistency. The tool monitors projects for changes, utilizes AI to suggest coding guidelines, and provides a structured view of codebases, targeting developers seeking to improve their workflow and project quality."
}
```

## AI Behavior Rules

### Code Generation Style
#### Preferred Patterns
- Use 4 spaces for indentation.
- Use snake_case for variables and function names.
- Use CamelCase for class names.
- Use descriptive variable and function names.
- Keep lines under 120 characters.
- Use f-strings for string formatting.
- Use type hints for function signatures and variables.
- Use docstrings for functions and classes.
- Use consistent import statements, grouped by standard library, third-party, and local modules.
- Use clear and concise comments where necessary.
- Use blank lines to separate logical blocks of code within functions.
- Use consistent naming patterns for similar concepts.

#### Patterns to Avoid
- Use tabs for indentation.
- Use inconsistent indentation.
- Use abbreviations or cryptic names.
- Exceeding line length limits.
- Inconsistent string formatting.
- Lack of type hints.
- Missing docstrings.
- Unorganized import statements.
- Unnecessary comments.
- Lack of whitespace between logical code blocks.
- Inconsistent naming.

### Error Handling
#### Preferred Patterns
- Use try-except blocks for error handling.
- Log exceptions using the logging module.
- Return None or False from functions upon failure instead of raising exceptions.
- Catch specific exceptions where possible, instead of a general 'Exception'
- Provide clear error messages in log statements.

#### Patterns to Avoid
- Using bare except statements
- Ignoring exceptions silently.
- Printing error messages to console instead of logging.
- Raising generic exceptions.
- Failing without returning information about failure.

### Performance
#### Preferred Patterns
- Use sets for membership testing.
- Use list comprehensions where appropriate.
- Use `os.path.join` for creating file paths.
- Avoid unnecessary file reads and writes.
- Use `os.scandir` over `os.listdir` for directory traversal where possible.
- Use `set` for faster lookups when checking for a list of items.

#### Patterns to Avoid
- Unnecessary loops.
- Inefficient string manipulations.
- Hardcoding paths.
- Repeatedly reading the same files.
- Using `os.listdir` when `os.scandir` is more efficient.
- Using lists for membership checks when sets are more performant.

### Module Organization
#### Structure
- The project is structured into multiple Python modules, each with specific responsibilities.
- The core logic is separated from configuration and utility functions.
- Modules are organized based on their functionality, such as auto-updating, analysis, rule generation, content generation, and project detection.
- Configuration settings are loaded from a dedicated `config.py` module and a `config.json` file.
- The `setup.py` script is used for project configuration and management.
- There is a consistent structure for main program execution with `focus.py` and `setup.py`.

#### Dependencies
- `auto_updater.py` depends on `os`, `requests`, `json`, `shutil`, `datetime`, `logging`, `typing`, `tempfile`, `zipfile`.
- `analyzers.py` depends on `os`, `re`, `config`, `logging`.
- `rules_generator.py` depends on `os`, `json`, `typing`, `datetime`, `google.generativeai`, `re`, `rules_analyzer`, `dotenv`, `config`.
- `project_detector.py` depends on `os`, `json`, `re`, `config`, `time`, `typing`.
- `config.py` depends on `os`, `json`.
- `me_generator.py` depends on `os`, `datetime`, `typing`, `content_generator`, `config`.
- `rules_watcher.py` depends on `os`, `time`, `typing`, `watchdog`, `rules_generator`, `project_detector`, `config`.
- `rules_analyzer.py` depends on `os`, `json`, `typing`.
- `setup.py` depends on `os`, `json`, `argparse`, `logging`, `project_detector`.
- `content_generator.py` depends on `os`, `datetime`, `analyzers`, `project_detector`, `config`, `re`, `logging`, `typing`.
- `focus.py` depends on `os`, `time`, `datetime`, `typing`, `config`, `content_generator`, `rules_analyzer`, `rules_generator`, `rules_watcher`, `logging`, `auto_updater`, `me_generator`.

#### Module Responsibilities
- **auto_updater.py**: Handles automatic updates of the application from a GitHub repository.
- **analyzers.py**: Analyzes code files to detect functions and determine if a file should be ignored.
- **rules_generator.py**: Generates project rules using Gemini AI based on project analysis.
- **project_detector.py**: Detects the type of project based on file system indicators.
- **config.py**: Loads and manages project configuration settings.
- **me_generator.py**: Generates a 'Me.md' file containing personal activity and project metrics.
- **rules_watcher.py**: Monitors project files for changes and triggers updates to the rules file.
- **rules_analyzer.py**: Analyzes the project to provide information for rule generation.
- **setup.py**: Handles project configuration, adding, removing, and listing projects, and scanning for new projects.
- **content_generator.py**: Generates the 'Focus.md' file containing project structure and function information.
- **focus.py**: The main entry point of the application, managing project monitoring, update checks, and document generation.

#### Rules
- Each module has a clear and specific purpose.
- Modules communicate through function calls and data passing.
- Configuration is centralized in the `config.py` module and loaded at startup.
- Error handling is consistent across modules using `try-except` blocks and logging.
- Modules use descriptive names to indicate their purpose.

#### Naming Conventions
- **modules**: Descriptive names using snake_case (e.g., `auto_updater.py`, `rules_generator.py`).
- **classes**: Descriptive names using CamelCase (e.g., `AutoUpdater`, `RulesGenerator`).
- **functions**: Descriptive names using snake_case (e.g., `check_for_updates`, `analyze_file_content`).
- **variables**: Descriptive names using snake_case (e.g., `repo_url`, `project_path`).
- **constants**: Descriptive names using UPPER_SNAKE_CASE (e.g. `BINARY_EXTENSIONS`).
