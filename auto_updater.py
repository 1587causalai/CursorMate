import os
import requests
import json
import shutil
from datetime import datetime, timezone
import logging
from typing import Optional, Dict, Any
import tempfile
import zipfile

def clear_console():
    """Clear console screen for different OS."""
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Unix/Linux/MacOS
    else:
        os.system('clear')

class AutoUpdater:
    def __init__(self, repo_url: str = "https://github.com/RenjiYuusei/CursorFocus"):
        self.repo_url = repo_url
        self.api_url = repo_url.replace("github.com", "api.github.com/repos")
        self.current_version = self._get_current_version()
        self.latest_version = None
        self.update_available = False

    def _get_current_version(self):
        """获取当前版本号"""
        try:
            with open('.current_commit', 'r') as f:
                return f.read().strip()
        except FileNotFoundError:
            return None

    def check_for_updates(self) -> Optional[Dict[str, Any]]:
        """Check update from latest update"""
        try:
            # Check commit latest
            response = requests.get(f"{self.api_url}/commits/main")
            if response.status_code == 404:  
                response = requests.get(f"{self.api_url}/commits/master")
            
            if response.status_code != 200:
                return None

            latest_commit = response.json()
            current_commit = self._get_current_commit()
            
            if latest_commit['sha'] != current_commit:
                # Convert UTC time to local time
                utc_date = datetime.strptime(
                    latest_commit['commit']['author']['date'], 
                    "%Y-%m-%dT%H:%M:%SZ"
                )
                local_date = utc_date.replace(tzinfo=timezone.utc).astimezone(tz=None)
                formatted_date = local_date.strftime("%B %d, %Y at %I:%M %p")
                
                return {
                    'sha': latest_commit['sha'],
                    'message': latest_commit['commit']['message'],
                    'date': formatted_date,
                    'author': latest_commit['commit']['author']['name'],
                    'download_url': f"{self.repo_url}/archive/refs/heads/main.zip"
                }
            
            return None

        except Exception as e:
            logging.error(f"Error checking for updates: {e}")
            return None

    def _get_current_commit(self) -> str:
        """Get the SHA of the current commit."""
        try:
            version_file = os.path.join(os.path.dirname(__file__), '.current_commit')
            if os.path.exists(version_file):
                with open(version_file, 'r') as f:
                    return f.read().strip()
            return ''
        except:
            return ''

    def should_update(self):
        """是否应该更新"""
        # 暂时禁用自动更新
        return False

    def update(self, update_info: Dict[str, Any]) -> bool:
        """Update from latest commit."""
        try:
            # Download zip file of branch
            response = requests.get(update_info['download_url'])
            if response.status_code != 200:
                return False

            # Save zip file temporarily
            temp_dir = tempfile.mkdtemp()
            zip_path = os.path.join(temp_dir, 'update.zip')
            with open(zip_path, 'wb') as f:
                f.write(response.content)

            # Unzip and update
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                # Get root directory name in zip
                root_dir = zip_ref.namelist()[0].split('/')[0]
                zip_ref.extractall(temp_dir)

                # Copy new files
                src_dir = os.path.join(temp_dir, root_dir)
                dst_dir = os.path.dirname(__file__)
                
                for item in os.listdir(src_dir):
                    s = os.path.join(src_dir, item)
                    d = os.path.join(dst_dir, item)
                    if os.path.isfile(s):
                        shutil.copy2(s, d)
                    elif os.path.isdir(s):
                        shutil.copytree(s, d, dirs_exist_ok=True)

            # Save SHA of new commit
            with open(os.path.join(dst_dir, '.current_commit'), 'w') as f:
                f.write(update_info['sha'])

            # Clean up
            shutil.rmtree(temp_dir)
            
            # Clear console after successful update
            clear_console()
            return True

        except Exception as e:
            logging.error(f"Error updating: {e}")
            return False 