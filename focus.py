#!/usr/bin/env python3
"""
CursorFocus 主程序 (focus.py)

这是 CursorFocus 项目的核心执行程序，负责项目的监控、分析和文档生成。
与 setup.py（配置管理工具）配合使用，形成完整的项目监控系统。

核心功能：
1. 项目监控
   - 多线程监控多个项目
   - 实时更新项目状态
   - 自动检测文件变化

2. 文档生成
   - 生成和更新 Focus.md 文档
   - 生成项目规则文件 (.cursorrules)
   - 实时更新项目分析结果

3. 自动更新
   - 检查程序版本更新
   - 自动下载并应用更新
   - 支持更新确认

工作流程：
1. 启动时检查程序更新
2. 加载项目配置信息
3. 为每个项目生成初始文档
4. 启动多线程监控各个项目
5. 定期更新项目文档和分析结果

配置项说明：
- update_interval: 更新间隔（秒）
- max_depth: 目录扫描深度
- ignored_directories: 忽略的目录
- ignored_files: 忽略的文件
- binary_extensions: 二进制文件扩展名
- file_length_standards: 各类文件的标准长度
- file_length_thresholds: 文件长度警告阈值
- project_types: 支持的项目类型定义

使用方式：
python focus.py

注意事项：
1. 需要先通过 setup.py 配置要监控的项目
2. 支持多项目同时监控
3. 可以通过 Ctrl+C 安全退出
4. 自动保存所有分析结果
"""

import os
import time
from datetime import datetime
from typing import Dict, List
from config import load_config
from content_generator import generate_focus_content
from rules_analyzer import RulesAnalyzer
from rules_generator import RulesGenerator
from rules_watcher import ProjectWatcherManager
import logging
from auto_updater import AutoUpdater
from me_generator import generate_me_content

def get_default_config():
    """
    获取默认配置
    
    返回一个包含默认配置的字典，包括：
    - 项目路径（默认为父目录）
    - 更新间隔（60秒）
    - 扫描深度（3层）
    - 忽略的目录和文件
    - 二进制文件扩展名
    - 各类文件的标准长度
    - 文件长度警告阈值
    - 支持的项目类型定义
    """
    return {
        'project_path': os.path.abspath(os.path.join(os.path.dirname(__file__), '..')),
        'update_interval': 60,
        'max_depth': 3,
        'ignored_directories': [
            '__pycache__',
            'node_modules',
            'venv',
            '.git',
            '.idea',
            '.vscode',
            'dist',
            'build',
            'CursorFocus'
        ],
        'ignored_files': [
            '.DS_Store',
            '*.pyc',
            '*.pyo'
        ],
        'binary_extensions': [
            '.png',
            '.jpg',
            '.jpeg',
            '.gif',
            '.ico',
            '.pdf',
            '.exe',
            '.bin'
        ],
        'file_length_standards': {
            '.js': 300,
            '.jsx': 250,
            '.ts': 300,
            '.tsx': 250,
            '.py': 400,
            '.css': 400,
            '.scss': 400,
            '.less': 400,
            '.sass': 400,
            '.html': 300,
            '.vue': 250,
            '.svelte': 250,
            '.json': 100,
            '.yaml': 100,
            '.yml': 100,
            '.toml': 100,
            '.md': 500,
            '.rst': 500,
            '.php': 400,
            '.phtml': 300,
            '.ctp': 300,
            '.swift': 300,
            '.kt': 300,
            'default': 300
        },
        'file_length_thresholds': {
            'warning': 1.0,
            'critical': 1.5,
            'severe': 2.0
        },
        'project_types': {
            'chrome_extension': {
                'indicators': ['manifest.json'],
                'required_files': [],
                'description': 'Chrome Extension'
            },
            'node_js': {
                'indicators': ['package.json'],
                'required_files': [],
                'description': 'Node.js Project'
            },
            'python': {
                'indicators': ['setup.py', 'pyproject.toml'],
                'required_files': [],
                'description': 'Python Project'
            },
            'react': {
                'indicators': [],
                'required_files': ['src/App.js', 'src/index.js'],
                'description': 'React Application'
            },
            'php': {
                'indicators': ['composer.json', 'index.php'],
                'required_files': [],
                'description': 'PHP Project'
            },
            'laravel': {
                'indicators': ['artisan'],
                'required_files': [],
                'description': 'Laravel Project'
            },
            'wordpress': {
                'indicators': ['wp-config.php'],
                'required_files': [],
                'description': 'WordPress Project'
            }
        }
    }

def retry_generate_rules(project_path, project_name, max_retries=5):
    """
    重试生成项目规则文件
    
    参数：
    - project_path: 项目路径
    - project_name: 项目名称
    - max_retries: 最大重试次数（默认5次）
    
    功能：
    1. 分析项目结构
    2. 让用户选择规则文件格式（JSON/Markdown）
    3. 生成规则文件
    4. 失败时提供重试机制
    """
    retries = 0
    while retries < max_retries:
        try:
            print(f"\n📄 Analyzing: {project_path}")
            analyzer = RulesAnalyzer(project_path)
            project_info = analyzer.analyze_project_for_rules()
            
            # Ask for format preference using numbers
            print("\nSelect format for .cursorrules file:")
            print("1. JSON")
            print("2. Markdown")
            while True:
                try:
                    choice = int(input("Enter selection (1-2): "))
                    if choice in [1, 2]:
                        format_choice = 'json' if choice == 1 else 'markdown'
                        break
                    print("Please enter 1 or 2")
                except ValueError:
                    print("Please enter a number")
            
            rules_generator = RulesGenerator(project_path)
            rules_file = rules_generator.generate_rules_file(project_info, format=format_choice)
            print(f"✓ {os.path.basename(rules_file)}")
            return rules_file
        except Exception as e:
            retries += 1
            if retries < max_retries:
                print(f"\n❌ Failed to generate rules (attempt {retries}/{max_retries}): {e}")
                response = input("Retry? (y/n): ").lower()
                if response != 'y':
                    raise
            else:
                print(f"\n❌ Failed to generate rules after {max_retries} attempts: {e}")
                raise

def setup_cursor_focus(project_path, project_name=None):
    """
    为项目设置 CursorFocus
    
    参数：
    - project_path: 项目路径
    - project_name: 项目名称（可选）
    
    功能：
    1. 生成 Focus.md 文档
    2. 生成 Me.md 文档
    3. 生成 Rules.md 文件 (作为 .cursorrules 的候选内容)
    """
    try:
        # 加载配置
        config = load_config()
        project_config = None
        
        # 查找对应项目的配置
        if config and 'projects' in config:
            for proj in config['projects']:
                if proj['project_path'] == project_path:
                    project_config = proj
                    break
        
        # 如果没有找到项目配置，使用默认配置
        if not project_config:
            project_config = get_default_config()
        
        # 确保输出目录存在
        output_dir = os.path.join(project_path, project_config.get('output_directory', '.me'))
        os.makedirs(output_dir, exist_ok=True)
        
        # 生成 Focus.md
        focus_file = os.path.join(project_path, project_config.get('file_paths', {}).get('focus', '.me/Focus.md'))
        content = generate_focus_content(project_path, project_config)
        os.makedirs(os.path.dirname(focus_file), exist_ok=True)
        with open(focus_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Generated {os.path.basename(focus_file)}")

        # 生成 Me.md
        me_file = os.path.join(project_path, project_config.get('file_paths', {}).get('me', '.me/Me.md'))
        me_content = generate_me_content(project_path, project_config)
        os.makedirs(os.path.dirname(me_file), exist_ok=True)
        with open(me_file, 'w', encoding='utf-8') as f:
            f.write(me_content)
        print(f"✓ Generated {os.path.basename(me_file)}")

        # 生成 Rules.md
        try:
            rules_file = os.path.join(project_path, project_config.get('file_paths', {}).get('rules', '.me/Rules.md'))
            os.makedirs(os.path.dirname(rules_file), exist_ok=True)
            
            # 分析项目并生成规则
            analyzer = RulesAnalyzer(project_path)
            project_info = analyzer.analyze_project_for_rules()
            rules_generator = RulesGenerator(project_path)
            rules_generator.generate_rules_file(project_info, rules_file)
            print(f"✓ Generated {os.path.basename(rules_file)}")
        except Exception as e:
            print(f"⚠️ Warning: Could not generate rules file: {e}")

    except Exception as e:
        print(f"❌ Setup error: {e}")
        raise

def monitor_project(project_path: str, config: Dict):
    """监控项目变化并更新文档"""
    try:
        # 确保输出目录存在
        output_dir = os.path.join(project_path, config.get('output_directory', '.me'))
        os.makedirs(output_dir, exist_ok=True)
        
        # 生成 Focus.md
        focus_file = os.path.join(project_path, config.get('file_paths', {}).get('focus', '.me/Focus.md'))
        focus_content = generate_focus_content(project_path, config)
        os.makedirs(os.path.dirname(focus_file), exist_ok=True)
        with open(focus_file, 'w', encoding='utf-8') as f:
            f.write(focus_content)
            
        # 生成 Me.md
        me_file = os.path.join(project_path, config.get('file_paths', {}).get('me', '.me/Me.md'))
        me_content = generate_me_content(project_path, config)
        os.makedirs(os.path.dirname(me_file), exist_ok=True)
        with open(me_file, 'w', encoding='utf-8') as f:
            f.write(me_content)
                
        print(f"✓ Generated documents at {datetime.now()}")
    except Exception as e:
        logging.error(f"Error generating documents: {e}")

def test_me_generation():
    """测试 Me.md 生成功能"""
    try:
        project_path = os.getcwd()  # 使用当前目录
        config = get_default_config()
        
        # 确保输出目录存在
        output_dir = os.path.join(project_path, config['output_directory'])
        os.makedirs(output_dir, exist_ok=True)
        
        # 生成 Me.md
        me_file = os.path.join(project_path, config['file_paths']['me'])
        me_content = generate_me_content(project_path, config)
        os.makedirs(os.path.dirname(me_file), exist_ok=True)
        with open(me_file, 'w', encoding='utf-8') as f:
            f.write(me_content)
            
        print(f"✓ Generated {os.path.basename(me_file)} successfully")
    except Exception as e:
        print(f"❌ Error generating Me.md: {e}")

def main():
    """
    主函数 - 程序入口
    
    功能流程：
    1. 检查更新
    2. 加载配置文件
    3. 设置默认项目（如果没有配置）
    4. 生成文档并启动监控
    """
    try:
        # 检查更新
        print("\n🔄 Checking updates...")
        updater = AutoUpdater()
        if updater.check_for_updates():
            if updater.should_update():
                updater.update()
                print("✓ Updated to latest version")
                return
        else:
            print("✓ Latest version")

        # 加载配置
        config = load_config()
        if not config:
            config = get_default_config()

        if 'projects' not in config:
            config['projects'] = [{
                'name': 'Default Project',
                'project_path': os.getcwd(),
                'update_interval': config.get('update_interval', 60),
                'max_depth': config.get('max_depth', 3)
            }]

        # 为每个项目生成文档并启动监控
        for project in config['projects']:
            if os.path.exists(project['project_path']):
                setup_cursor_focus(project['project_path'], project.get('name'))
            else:
                print(f"⚠️ Not found: {project['project_path']}")

        # 启动监控
        print(f"\n📝 Monitoring {len(config['projects'])} projects (Ctrl+C to stop)")
        watcher = ProjectWatcherManager()
        for project in config['projects']:
            if os.path.exists(project['project_path']):
                watcher.add_project(project['project_path'], project.get('name'))

        try:
            while True:
                # 使用配置中的更新间隔
                update_interval = min([p.get('update_interval', 60) for p in config['projects']])
                time.sleep(update_interval)
                for project in config['projects']:
                    if os.path.exists(project['project_path']):
                        setup_cursor_focus(project['project_path'], project.get('name'))
                print(f"✓ Generated documents at {datetime.now()}")
        except KeyboardInterrupt:
            watcher.stop_all()
            print("\n👋 Bye!")

    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == '__main__':
    main() 