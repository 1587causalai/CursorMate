# Project Rules

## Project Information
- **Version**: 1.0.0
- **Last Updated**: January 26, 2025 at 11:48 PM
- **Name**: CursorMate
- **Language**: markdown
- **Framework**: none
- **Type**: application

## Project Description
This project is a code analysis and automation tool designed to enhance the development workflow by generating project-specific documentation, coding rules, and personal activity metrics. It leverages AI to suggest coding standards and best practices, while also providing real-time monitoring and automatic updates to keep projects synchronized with established guidelines; the tool is intended for developers who aim to maintain consistency and quality across their projects.

## AI Behavior Rules

### Code Generation Style
#### Preferred Patterns
- Use snake_case for variables and functions.
- Use PascalCase for classes.
- Use docstrings to document functions and classes.
- Use type hints for function arguments and return values.
- Use consistent indentation (4 spaces).
- Keep lines under 120 characters long when possible.
- Use f-strings for string formatting.
- Use clear and concise variable names.
- Use imports at the top of the file, grouped by standard library, third-party, and local modules.
- Use consistent spacing around operators and commas.
- Use list comprehensions or generator expressions for simple iterations when appropriate.

#### Patterns to Avoid
- Camel case for variables or functions.
- Inconsistent indentation.
- Long lines that wrap around.
- Magic numbers or hardcoded values.
- Inconsistent spacing.
- Unnecessary blank lines.
- Using overly complex code constructs where simpler ones suffice.

### Error Handling
#### Preferred Patterns
- Use try-except blocks to handle potential errors.
- Log errors using the logging module.
- Return None or False to indicate failure in functions or methods where appropriate.
- Provide informative error messages in log statements.
- Catch specific exceptions where possible rather than generic Exception.
- Use a basic error handling approach without complex custom error classes or decorators.

#### Patterns to Avoid
- Ignoring errors without logging or handling them.
- Using bare except blocks.
- Raising exceptions without context.
- Using print statements for error messages (use logging instead).
- Complex error handling patterns.

### Performance
#### Preferred Patterns
- Use sets for membership testing.
- Use list comprehensions or generator expressions instead of loops when possible.
- Optimize regex patterns for efficiency.
- Avoid unnecessary file reads or writes.
- Use efficient data structures for lookups and storage.
- Use cached results when possible.
- Use os.scandir for directory traversal.
- Use shutil.copy2 for copying files and directories.
- Use temporary files and directories for operations.

#### Patterns to Avoid
- Unnecessary loops or iterations.
- Repeatedly opening and closing files.
- Inefficient regex patterns.
- Performing computationally expensive operations in loops.
- Excessive memory consumption.

### Module Organization
#### Structure
- The project is organized into several modules, each with a specific responsibility.
- The core modules are: auto_updater.py, analyzers.py, rules_generator.py, project_detector.py, config.py, me_generator.py, rules_watcher.py, rules_analyzer.py, setup.py, content_generator.py, and focus.py.
- Modules are located in the root directory of the project.
- There are no sub-packages.

#### Dependencies
- auto_updater.py: os, requests, json, shutil, datetime, logging, typing, tempfile, zipfile.
- analyzers.py: os, re, config, logging.
- rules_generator.py: os, json, typing, datetime, google.generativeai, re, rules_analyzer, dotenv, config.
- project_detector.py: os, json, re, config, time, typing.
- config.py: os, json.
- me_generator.py: os, datetime, typing, content_generator, config.
- rules_watcher.py: os, time, typing, watchdog, rules_generator, project_detector, config.
- rules_analyzer.py: os, json, typing.
- setup.py: os, json, argparse, logging, project_detector.
- content_generator.py: os, datetime, analyzers, project_detector, config, re, logging, typing.
- focus.py: os, time, datetime, typing, config, content_generator, rules_analyzer, rules_generator, rules_watcher, logging, auto_updater, me_generator.

#### Module Responsibilities
- **auto_updater.py**: Handles auto-updating the application from a GitHub repository.
- **analyzers.py**: Analyzes file content for functions, descriptions, and other code features.
- **rules_generator.py**: Generates rules for the Cursor IDE using Gemini AI based on project analysis.
- **project_detector.py**: Detects the type of project based on file patterns and indicators.
- **config.py**: Loads and manages configuration settings for the application.
- **me_generator.py**: Generates personal activity metrics and recommendations.
- **rules_watcher.py**: Monitors file changes and triggers rule updates.
- **rules_analyzer.py**: Analyzes project metadata for rule generation.
- **setup.py**: Manages project configuration, adding, removing, and listing projects.
- **content_generator.py**: Generates content for the Focus.md file, including directory structure and file information.
- **focus.py**: The main entry point for the application, coordinates project monitoring, analysis, and documentation generation.

#### Rules
- Each module should have a clear and defined responsibility.
- Modules should have minimal dependencies with each other.
- Configuration should be managed in a central config.py file.
- Project detection should be separated from other analysis logic.
- Rules generation should be handled by a dedicated module.
- File monitoring and automatic updates should be handled by dedicated modules.
- Focus.md, Me.md and Rules.md generation should be handled by dedicated modules.

#### Naming Conventions
- **variables**: Use snake_case (e.g., project_path, file_name).
- **functions**: Use snake_case (e.g., analyze_file_content, generate_focus_content).
- **classes**: Use PascalCase (e.g., AutoUpdater, RulesGenerator, ProjectMetrics).
- **constants**: Use UPPER_SNAKE_CASE (e.g., PROJECT_TYPES, CACHE_EXPIRATION).
- **files**: Use snake_case for file names (e.g., auto_updater.py, rules_generator.py).
- **method**: Use snake_case (e.g., _get_timestamp, _analyze_project_structure).
