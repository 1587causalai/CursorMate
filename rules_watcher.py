import os
import time
from typing import Dict, Any
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from rules_generator import RulesGenerator
from project_detector import detect_project_type
from config import get_default_config

class RulesWatcher(FileSystemEventHandler):
    def __init__(self, project_path: str, project_id: str):
        self.project_path = project_path
        self.project_id = project_id
        self.rules_generator = RulesGenerator(project_path)
        self.last_update = 0
        self.update_delay = 5  # Seconds to wait before updating to avoid multiple updates
        self.auto_update = False  # Disable auto-update by default
        self.config = get_default_config()  # 加载配置

    def on_modified(self, event):
        if event.is_directory or not self.auto_update:  # Skip if auto-update is disabled
            return
            
        # Only process Focus.md changes or project configuration files
        if not self._should_process_file(event.src_path):
            return
            
        current_time = time.time()
        if current_time - self.last_update < self.update_delay:
            return
            
        self.last_update = current_time
        self._update_rules()

    def _should_process_file(self, file_path: str) -> bool:
        """Check if the file change should trigger a rules update."""
        if not self.auto_update:  # Skip if auto-update is disabled
            return False
            
        filename = os.path.basename(file_path)
        focus_file = os.path.basename(self.config.get('file_paths', {}).get('focus', 'Focus.md'))
        
        # List of files that should trigger an update
        trigger_files = [
            focus_file,  # 使用配置中的Focus.md路径
            'package.json',
            'requirements.txt',
            'CMakeLists.txt',
            '.csproj',
            'composer.json',
            'build.gradle',
            'pom.xml'
        ]
        
        return filename in trigger_files or any(file_path.endswith(ext) for ext in ['.csproj'])

    def _update_rules(self):
        """Update the .cursorrules file."""
        if not self.auto_update:  # Skip if auto-update is disabled
            return
            
        try:
            # Re-detect project type
            project_info = detect_project_type(self.project_path)
            
            # 确保输出目录存在
            output_dir = os.path.join(self.project_path, self.config.get('output_directory', '.me'))
            os.makedirs(output_dir, exist_ok=True)
            
            # Generate new rules
            rules_file = os.path.join(self.project_path, self.config.get('file_paths', {}).get('rules', '.me/Rules.md'))
            os.makedirs(os.path.dirname(rules_file), exist_ok=True)
            self.rules_generator.generate_rules_file(project_info, rules_file)
            print(f"Updated {os.path.basename(rules_file)} for project {self.project_id} at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        except Exception as e:
            print(f"Error updating rules file for project {self.project_id}: {e}")

    def set_auto_update(self, enabled: bool):
        """Enable or disable auto-update of .cursorrules."""
        self.auto_update = enabled
        status = "enabled" if enabled else "disabled"
        print(f"Auto-update of .cursorrules is now {status} for project {self.project_id}")

class ProjectWatcherManager:
    def __init__(self, project_path: str = None, config: Dict = None):
        self.observers = {}
        self.watchers = {}
        if project_path:
            self.add_project(project_path)
            
    def add_project(self, project_path: str, project_id: str = None) -> str:
        """
        添加一个项目到监控列表
        
        参数：
        - project_path: 项目路径
        - project_id: 项目ID（可选，默认使用路径的base name）
        
        返回：
        - project_id: 项目ID
        """
        project_path = os.path.abspath(project_path)
        if not project_id:
            project_id = os.path.basename(project_path)
            
        if project_id in self.observers:
            print(f"Project {project_id} is already being watched")
            return project_id
            
        try:
            # 创建观察者和处理器
            observer = Observer()
            watcher = RulesWatcher(project_path, project_id)
            
            # 启动观察者
            observer.schedule(watcher, project_path, recursive=True)
            observer.start()
            
            # 保存观察者和处理器的引用
            self.observers[project_id] = observer
            self.watchers[project_id] = watcher
            
            print(f"Started watching project {project_id}")
            return project_id
            
        except Exception as e:
            print(f"Error watching project {project_id}: {e}")
            raise

    def remove_project(self, project_id: str):
        """Stop watching a project."""
        if project_id not in self.observers:
            print(f"Project {project_id} is not being watched")
            return
            
        observer = self.observers[project_id]
        observer.stop()
        observer.join()
        
        del self.observers[project_id]
        del self.watchers[project_id]
        
        print(f"Stopped watching project {project_id}")

    def list_projects(self) -> Dict[str, str]:
        """Return a dictionary of watched projects and their paths."""
        return {pid: watcher.project_path for pid, watcher in self.watchers.items()}

    def stop_all(self):
        """Stop watching all projects."""
        for project_id in list(self.observers.keys()):
            self.remove_project(project_id)

    def set_auto_update(self, project_id: str, enabled: bool):
        """Enable or disable auto-update for a specific project."""
        if project_id in self.watchers:
            self.watchers[project_id].set_auto_update(enabled)
        else:
            print(f"Project {project_id} is not being watched")

def start_watching(project_paths: str | list[str]):
    """Start watching one or multiple project directories for changes.
    
    Args:
        project_paths: A single project path or list of project paths to watch
    """
    manager = ProjectWatcherManager()
    
    if isinstance(project_paths, str):
        project_paths = [project_paths]
        
    for path in project_paths:
        manager.add_project(path)
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        manager.stop_all() 