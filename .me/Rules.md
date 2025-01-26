# Project Rules

## Project Information
- **Version**: 1.0.0
- **Last Updated**: January 27, 2025 at 12:53 AM
- **Name**: CursorMate
- **Language**: markdown
- **Framework**: none
- **Type**: application

## Project Description
This project provides an automated system for analyzing and documenting software projects, generating tailored coding rules and project insights for developers. It dynamically monitors project files, creating documentation, personalized metrics, and rules for the Cursor IDE, aiming to enhance developer workflows and project understanding. Its unique approach lies in the integration of project analysis with automatic rule generation, providing a tailored development experience based on the specific project structure and characteristics.

## AI Behavior Rules

### Code Generation Style
#### Preferred Patterns
- Use 4 spaces for indentation.
- Use snake_case for variable and function names.
- Use PascalCase for class names.
- Use descriptive variable and function names.
- Use type hints for function and variable declarations.
- Use f-strings for string formatting.
- Use docstrings for functions and classes.
- Keep lines within the 120 character limit where possible.
- Use consistent blank lines for code separation.
- Group related code together.
- Use list comprehensions where appropriate.
- Avoid magic numbers, use constants defined in config.py
- Use specific imports instead of wildcard imports where possible
- Favor early returns for error handling.
- Use standard library where possible.
- Use relative paths when accessing files within the project.
- Use dictionaries for configurations
- Use sets for storing unique values (e.g., file extensions)
- Use list for storing ordered elements (e.g., file paths)
- Use regex for pattern matching
- Use logging module for logging instead of print statement

#### Patterns to Avoid
- Use tabs for indentation.
- Inconsistent indentation.
- Inconsistent spacing.
- Inconsistent naming conventions.
- Magic numbers.
- Wildcard imports.
- Overly complex logic.
- Long lines of code.
- Using print statements for logging
- Using hardcoded paths
- Redundant comments

### Error Handling
#### Preferred Patterns
- Use try-except blocks for error handling.
- Log errors using the logging module.
- Return None or False on errors, depending on the context.
- Catch broad exceptions when necessary, but be specific when possible.
- Provide informative error messages.
- Avoid using bare except blocks

#### Patterns to Avoid
- Ignoring errors.
- Crashing the program on errors.
- Using print statements for logging errors.
- Not handling potential exceptions
- Using bare except blocks

### Performance
#### Preferred Patterns
- Use sets instead of lists for membership testing where possible.
- Use os.scandir for faster directory traversal.
- Use os.path.join for creating file paths.
- Use regular expression for pattern matching where possible
- Use caching for repeated computation where possible
- Use `set` for unique lookups.
- Use `itertools` for efficient iteration.
- Use `os.path.splitext` for file extension parsing.
- Use `set` for storing unique elements.

#### Patterns to Avoid
- Inefficient loops.
- Unnecessary file operations.
- Repeated computations.
- String concatenation in loops.
- Using `os.listdir` when `os.scandir` is more efficient.
- Overusing recursive function calls.

### Module Organization
#### Structure
- The project is organized into several modules, each with a specific responsibility.
- Modules are separated into core modules and support modules.
- Core modules include: `auto_updater.py`, `rules_generator.py`, `project_detector.py`, `rules_analyzer.py`, `content_generator.py`, `me_generator.py`, `focus.py`
- Support modules include: `config.py`, `analyzers.py`, `rules_watcher.py`, `setup.py`.
- The `setup.py` is responsible for project configuration.
- The `focus.py` is the main entry point of the application.
- The `config.py` is responsible for storing configuration.
- Modules are generally organized by functionality.

#### Dependencies
- The `auto_updater.py` depends on `os`, `requests`, `json`, `shutil`, `datetime`, `logging`, `typing`, `tempfile`, `zipfile`.
- The `analyzers.py` depends on `os`, `re` and `config.py`.
- The `rules_generator.py` depends on `os`, `json`, `typing`, `datetime`, `google.generativeai`, `re`, `rules_analyzer.py`, `dotenv`, `config.py`.
- The `project_detector.py` depends on `os`, `json`, `re` and `config.py`.
- The `config.py` depends on `os`, `json`.
- The `content_generator.py` depends on `os`, `datetime`, `analyzers.py`, `project_detector.py`, `config.py`, `re`, `logging`, `typing`.
- The `me_generator.py` depends on `os`, `datetime`, `typing`, `content_generator.py` and `config.py`.
- The `rules_watcher.py` depends on `os`, `time`, `typing`, `watchdog`, `rules_generator.py`, `project_detector.py` and `config.py`
- The `rules_analyzer.py` depends on `os`, `json`, `typing`
- The `setup.py` depends on `os`, `json`, `argparse`, `logging` and `project_detector.py`
- The `focus.py` depends on `os`, `time`, `datetime`, `typing`, `config.py`, `content_generator.py`, `rules_analyzer.py`, `rules_generator.py`, `rules_watcher.py`, `logging`, `auto_updater.py` and `me_generator.py`

#### Module Responsibilities
- **auto_updater.py**: Handles auto-updates of the application.
- **analyzers.py**: Analyzes files for code patterns and metrics.
- **rules_generator.py**: Generates rules for the Cursor IDE based on project analysis.
- **project_detector.py**: Detects the type of project based on its structure.
- **config.py**: Loads and provides access to project configuration.
- **content_generator.py**: Generates the Focus.md file with project information.
- **me_generator.py**: Generates the Me.md file with personal activity information.
- **rules_watcher.py**: Monitors project files for changes and updates rules.
- **rules_analyzer.py**: Analyzes the project for rules generation.
- **setup.py**: Sets up the project and manages project configurations.
- **focus.py**: The main entry point of the application, handles project monitoring and documentation generation.

#### Rules
- Each module should have a single responsibility.
- Modules should be loosely coupled.
- Core modules should not depend on support modules.
- Configuration should be loaded from config.py.
- Logging should be done using the logging module.
- Error handling should be done using try-except blocks.
- Use relative paths when accessing files within the project.
- Use dictionaries for configurations
- Use sets for storing unique values (e.g., file extensions)
- Use list for storing ordered elements (e.g., file paths)
- Use regex for pattern matching

#### Naming Conventions
- **variables**: snake_case
- **functions**: snake_case
- **classes**: PascalCase
- **constants**: UPPER_SNAKE_CASE
- **files**: snake_case.py
