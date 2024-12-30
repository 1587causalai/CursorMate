#!/usr/bin/env python3
import os
import json
import argparse
import logging

def create_launch_agent(project_path, python_path='/usr/local/bin/python3'):
    """Create and install the LaunchAgent plist file."""
    home = os.path.expanduser('~')
    launch_agents_dir = os.path.join(home, 'Library/LaunchAgents')
    plist_path = os.path.join(launch_agents_dir, 'com.cursorfocus.plist')
    
    # Create LaunchAgents directory if it doesn't exist
    os.makedirs(launch_agents_dir, exist_ok=True)
    
    plist_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.cursorfocus</string>
    <key>ProgramArguments</key>
    <array>
        <string>{python_path}</string>
        <string>{os.path.join(project_path, 'focus.py')}</string>
    </array>
    <key>WorkingDirectory</key>
    <string>{project_path}</string>
    <key>EnvironmentVariables</key>
    <dict>
        <key>PATH</key>
        <string>/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin</string>
    </dict>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardOutPath</key>
    <string>{os.path.join(project_path, 'cursorfocus.log')}</string>
    <key>StandardErrorPath</key>
    <string>{os.path.join(project_path, 'cursorfocus.error.log')}</string>
</dict>
</plist>'''

    # Write the plist file
    with open(plist_path, 'w') as f:
        f.write(plist_content)
    
    # Set proper permissions
    os.chmod(plist_path, 0o644)
    
    return plist_path

def setup_cursorfocus():
    """Set up CursorFocus for multiple projects."""
    parser = argparse.ArgumentParser(description='Set up CursorFocus for your projects')
    parser.add_argument('--projects', '-p', nargs='+', help='Paths to projects to monitor')
    parser.add_argument('--names', '-n', nargs='+', help='Names for the projects (optional)')
    parser.add_argument('--intervals', '-i', nargs='+', type=int, help='Update intervals in seconds for each project')
    parser.add_argument('--depths', '-d', nargs='+', type=int, help='Maximum directory depths for each project')
    parser.add_argument('--install-agent', '-a', action='store_true', help='Install LaunchAgent for automatic startup')
    parser.add_argument('--list', '-l', action='store_true', help='List all configured projects')
    parser.add_argument('--remove', '-r', nargs='+', help='Remove projects by name or index')
    parser.add_argument('--clear', '-c', action='store_true', help='Remove all projects')
    
    args = parser.parse_args()
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, 'config.json')
    
    config = load_or_create_config(config_path)
    
    if 'projects' not in config:
        config['projects'] = []

    if args.list:
        list_projects(config['projects'])
        return

    if args.clear:
        if confirm_action("Are you sure you want to remove all projects?"):
            config['projects'] = []
            save_config(config_path, config)
            print("\n✅ All projects have been removed.")
        return

    if args.remove:
        remove_projects(config, args.remove)
        save_config(config_path, config)
        return

    # Add/update projects
    if args.projects:
        # Validate project paths first
        valid_projects = []
        for i, project_path in enumerate(args.projects):
            abs_path = os.path.abspath(project_path)
            if not os.path.exists(abs_path):
                print(f"\n⚠️  Warning: Project path does not exist: {abs_path}")
                continue
                
            project_config = {
                'name': args.names[i] if args.names and i < len(args.names) else f"Project {i+1}",
                'project_path': abs_path,
                'update_interval': args.intervals[i] if args.intervals and i < len(args.intervals) else 60,
                'max_depth': args.depths[i] if args.depths and i < len(args.depths) else 3
            }
            valid_projects.append(project_config)
            
        # Check for duplicate names
        names = [p['name'] for p in valid_projects]
        if len(names) != len(set(names)):
            print("\n⚠️  Warning: Duplicate project names found. Adding unique suffixes...")
            name_counts = {}
            for project in valid_projects:
                base_name = project['name']
                if base_name in name_counts:
                    name_counts[base_name] += 1
                    project['name'] = f"{base_name} ({name_counts[base_name]})"
                else:
                    name_counts[base_name] = 1
        
        # Update existing projects or add new ones
        for project in valid_projects:
            existing = next((p for p in config['projects'] if p['project_path'] == project['project_path']), None)
            if existing:
                existing.update(project)
            else:
                config['projects'].append(project)

    # Save the config
    save_config(config_path, config)
    
    # Install LaunchAgent if requested
    if args.install_agent:
        try:
            python_path = args.python_path or '/usr/local/bin/python3'
            if not os.path.exists(python_path):
                print("⚠️  Warning: Default Python path not found. Please specify with --python-path")
                return
            
            plist_path = create_launch_agent(script_dir, python_path)
            print(f"\n✅ LaunchAgent installed at: {plist_path}")
            print("CursorFocus will now start automatically at login")
            print("\nTo start now:")
            print(f"$ launchctl load {plist_path}")
            print("\nTo stop:")
            print(f"$ launchctl unload {plist_path}")
        except Exception as e:
            print(f"\n❌ Error installing LaunchAgent: {e}")
            print("Please check permissions and try again")
    
    print("\n✅ CursorFocus configuration updated!")
    print("\n📁 Configured projects:")
    for project in config['projects']:
        print(f"\n  • {project['name']}:")
        print(f"    Path: {project['project_path']}")
        print(f"    Update interval: {project['update_interval']} seconds")
        print(f"    Max depth: {project['max_depth']} levels")
    
    print("\nTo start monitoring all projects, run:")
    print(f"python3 {os.path.join(script_dir, 'focus.py')}")

def load_or_create_config(config_path):
    """Load existing config or create default one."""
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            return json.load(f)
    return get_default_config()

def get_default_config():
    """Return default configuration."""
    return {
        "projects": [],
        "ignored_directories": [
            "__pycache__",
            "node_modules",
            "venv",
            ".git",
            ".idea",
            ".vscode",
            "dist",
            "build"
        ],
        "ignored_files": [
            ".DS_Store",
            "*.pyc",
            "*.pyo"
        ]
    }

def save_config(config_path, config):
    """Save configuration to file."""
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=4)

def list_projects(projects):
    """Display list of configured projects."""
    if not projects:
        print("\n📁 No projects configured.")
        return
        
    print("\n📁 Configured projects:")
    for i, project in enumerate(projects, 1):
        print(f"\n  {i}. {project['name']}:")
        print(f"     Path: {project['project_path']}")
        print(f"     Update interval: {project['update_interval']} seconds")
        print(f"     Max depth: {project['max_depth']} levels")

def remove_projects(config, targets):
    """Remove specific projects by name or index."""
    if not config['projects']:
        print("\n⚠️ No projects configured.")
        return
        
    remaining_projects = []
    removed = []
    
    for project in config['projects']:
        should_keep = True
        
        for target in targets:
            # Check if target is an index
            try:
                idx = int(target)
                if idx == config['projects'].index(project) + 1:
                    should_keep = False
                    removed.append(project['name'])
                    break
            except ValueError:
                # Target is a name
                if project['name'].lower() == target.lower():
                    should_keep = False
                    removed.append(project['name'])
                    break
                    
        if should_keep:
            remaining_projects.append(project)
    
    if removed:
        config['projects'] = remaining_projects
        print(f"\n✅ Removed projects: {', '.join(removed)}")
    else:
        print("\n⚠️ No matching projects found.")

def confirm_action(message):
    """Ask for user confirmation."""
    while True:
        response = input(f"\n{message} (y/n): ").lower()
        if response in ['y', 'yes']:
            return True
        if response in ['n', 'no']:
            return False

if __name__ == '__main__':
    setup_cursorfocus() 