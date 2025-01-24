# Focus.md 生成实现原理

## 1. 概述

`Focus.md` 是 CursorFocus 项目的实时项目文档，通过 `content_generator.py` 自动生成和更新。它提供了项目的结构、指标和关键信息的实时视图，帮助开发者更好地理解和管理项目。

## 2. 系统架构

### 2.1 核心组件
```
content_generator.py
├── ProjectMetrics 类     # 项目指标统计
├── 目录分析功能          # 项目结构分析
├── 文件分析功能          # 代码文件分析
└── Markdown 生成功能     # 文档生成
```

### 2.2 工作流程

让我们通过一个具体的项目示例来说明整个工作流程：

```python
# 假设我们有一个典型的项目结构：
project_structure = {
    'src': {
        'components': {
            'UserList.tsx': '''
import React from 'react';
import { User } from '../types';

interface Props {
    users: User[];
    onSelect: (user: User) => void;
}

export const UserList: React.FC<Props> = ({ users, onSelect }) => {
    return (
        <div className="user-list">
            {users.map(user => (
                <div key={user.id} onClick={() => onSelect(user)}>
                    {user.name}
                </div>
            ))}
        </div>
    );
};
'''
        },
        'types': {
            'index.ts': '''
export interface User {
    id: string;
    name: string;
    email: string;
}
'''
        }
    },
    'package.json': '{...}',
    'tsconfig.json': '{...}'
}

# 1. 初始化阶段
metrics = ProjectMetrics()

# 2. 分析阶段
def analyze_project():
    # 扫描目录结构
    structure = analyze_directory_structure(project_structure)
    
    # 分析文件内容
    for file_path, content in get_files(project_structure):
        if file_path.endswith('.tsx'):
            # 分析 React 组件
            components = analyze_react_component(content)
            metrics.add_component(file_path, components)
        elif file_path.endswith('.ts'):
            # 分析 TypeScript 类型
            types = analyze_typescript_types(content)
            metrics.add_types(file_path, types)
    
    # 收集项目指标
    metrics.update({
        'total_files': 3,
        'total_components': 1,
        'total_types': 1,
        'language_stats': {
            'TypeScript': '80%',
            'TSX': '20%'
        }
    })
    
    return structure, metrics

# 3. 生成阶段
def generate_focus_md(structure, metrics):
    return f"""
# Project Focus: TypeScript React Project

## 📊 Project Overview
- Files: {metrics.total_files}
- Components: {metrics.total_components}
- Types: {metrics.total_types}

## 📁 Project Structure
{format_structure(structure)}

## 🔍 Key Components
### UserList
- **Path:** src/components/UserList.tsx
- **Props:**
  - users: User[]
  - onSelect: (user: User) => void
- **Description:** 用户列表组件，支持点击选择用户

## 📝 Type Definitions
### User
- **Path:** src/types/index.ts
- **Properties:**
  - id: string
  - name: string
  - email: string

## 📈 Language Distribution
{format_language_stats(metrics.language_stats)}
"""
```

## 3. 实现细节

### 3.1 文件分析机制

以 React 组件分析为例：

```python
def analyze_react_component(content: str) -> Dict:
    """分析 React 组件的实现"""
    # 1. 提取接口定义
    interface_pattern = r"interface\s+(\w+)\s*{([^}]+)}"
    interfaces = re.findall(interface_pattern, content)
    
    # 2. 提取组件定义
    component_pattern = r"export\s+const\s+(\w+):\s*React\.FC<(\w+)>"
    component = re.search(component_pattern, content)
    
    # 3. 提取 hooks 使用
    hooks_pattern = r"use\w+\("
    hooks = re.findall(hooks_pattern, content)
    
    return {
        'name': component.group(1) if component else None,
        'props_interface': interfaces[0][0] if interfaces else None,
        'hooks_used': hooks
    }

# 使用示例
content = '''
interface Props {
    users: User[];
    onSelect: (user: User) => void;
}

export const UserList: React.FC<Props> = ({ users, onSelect }) => {
    const [selected, setSelected] = useState<User | null>(null);
    
    useEffect(() => {
        console.log('Selected user:', selected);
    }, [selected]);
    
    return (...);
};
'''

result = analyze_react_component(content)
print(result)
# 输出:
# {
#     'name': 'UserList',
#     'props_interface': 'Props',
#     'hooks_used': ['useState', 'useEffect']
# }
```

### 3.2 指标收集

```python
class ProjectMetrics:
    def __init__(self):
        self.metrics = {
            'files': {},
            'components': {},
            'types': {},
            'hooks': set(),
            'dependencies': {}
        }
    
    def add_component(self, file_path: str, component_info: Dict):
        self.metrics['components'][file_path] = component_info
        self.metrics['hooks'].update(component_info.get('hooks_used', []))
    
    def add_types(self, file_path: str, type_info: Dict):
        self.metrics['types'][file_path] = type_info
    
    def get_summary(self) -> Dict:
        return {
            'total_files': len(self.metrics['files']),
            'total_components': len(self.metrics['components']),
            'total_types': len(self.metrics['types']),
            'hooks_usage': list(self.metrics['hooks'])
        }
```

### 3.3 文档生成

文档生成采用模板化方式，根据不同的项目类型使用不同的模板：

```python
TEMPLATES = {
    'react': '''
# Project Focus: {project_name}

## 📊 Project Overview
{project_overview}

## 📁 Project Structure
{project_structure}

## 🔍 Key Components
{components_section}

## 📝 Type Definitions
{types_section}

## 📈 Statistics
{statistics}
''',
    'python': '''
# Project Focus: {project_name}

## 📊 Project Overview
{project_overview}

## 📁 Project Structure
{project_structure}

## 🔍 Key Modules
{modules_section}

## 📈 Statistics
{statistics}
'''
}

def generate_focus_content(project_path: str, metrics: ProjectMetrics) -> str:
    """生成 Focus.md 内容"""
    project_type = detect_project_type(project_path)
    template = TEMPLATES.get(project_type, TEMPLATES['default'])
    
    return template.format(
        project_name=get_project_name(project_path),
        project_overview=generate_overview(metrics),
        project_structure=generate_structure(project_path),
        components_section=generate_components_section(metrics),
        types_section=generate_types_section(metrics),
        statistics=generate_statistics(metrics)
    )
```

## 4. 使用流程

### 4.1 自动更新示例

```python
def monitor_project(project_config: Dict):
    """监控项目变化并更新文档"""
    project_path = project_config['path']
    update_interval = project_config.get('update_interval', 300)  # 5分钟
    
    while True:
        try:
            # 1. 检查项目变化
            if has_changes(project_path):
                # 2. 分析项目
                structure, metrics = analyze_project(project_path)
                
                # 3. 生成新文档
                content = generate_focus_content(project_path, metrics)
                
                # 4. 更新文件
                update_focus_md(project_path, content)
                
                print(f"✓ Updated Focus.md at {datetime.now()}")
            
            time.sleep(update_interval)
        except Exception as e:
            logging.error(f"Error updating Focus.md: {e}")
            time.sleep(60)  # 出错后等待1分钟再试
```

### 4.2 手动触发示例

```bash
# 直接生成文档
$ python focus.py --generate /path/to/project
📊 Analyzing project...
✓ Found 15 source files
✓ Analyzed 5 components
✓ Generated Focus.md

# 启动监控
$ python focus.py --monitor /path/to/project
👀 Monitoring project for changes...
✓ Initial Focus.md generated
ℹ️ Waiting for changes...
```

## 5. 最佳实践

### 5.1 性能优化
1. **缓存机制**
   ```python
   class FileCache:
       def __init__(self):
           self.cache = {}
           self.last_modified = {}
       
       def should_update(self, file_path: str) -> bool:
           if file_path not in self.last_modified:
               return True
           
           current_mtime = os.path.getmtime(file_path)
           return current_mtime > self.last_modified[file_path]
       
       def update(self, file_path: str, content: Any):
           self.cache[file_path] = content
           self.last_modified[file_path] = os.path.getmtime(file_path)
   ```

2. **增量更新**
   ```python
   def update_focus_md(project_path: str, new_content: str):
       """增量更新 Focus.md"""
       focus_path = os.path.join(project_path, 'Focus.md')
       
       if os.path.exists(focus_path):
           with open(focus_path, 'r') as f:
               old_content = f.read()
           
           if old_content == new_content:
               return False  # 无需更新
       
       with open(focus_path, 'w') as f:
           f.write(new_content)
       
       return True
   ```

### 5.2 错误处理

```python
class ContentGenerationError(Exception):
    """文档生成错误"""
    pass

def safe_generate_content(project_path: str) -> str:
    """安全地生成文档内容"""
    try:
        # 1. 验证项目路径
        if not os.path.exists(project_path):
            raise ContentGenerationError(f"Project path not found: {project_path}")
        
        # 2. 分析项目
        try:
            structure, metrics = analyze_project(project_path)
        except Exception as e:
            raise ContentGenerationError(f"Project analysis failed: {e}")
        
        # 3. 生成文档
        try:
            content = generate_focus_content(project_path, metrics)
        except Exception as e:
            raise ContentGenerationError(f"Content generation failed: {e}")
        
        return content
    
    except ContentGenerationError as e:
        logging.error(f"Content generation error: {e}")
        # 生成一个基础版本的文档
        return generate_basic_content(project_path)
    
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise
```

## 6. 注意事项

1. **性能考虑**
   - 大型项目处理
   ```python
   def process_large_project(project_path: str):
       """处理大型项目"""
       # 1. 使用多进程分析
       with ProcessPoolExecutor() as executor:
           file_results = list(executor.map(
               analyze_file,
               get_project_files(project_path)
           ))
       
       # 2. 合并结果
       metrics = merge_results(file_results)
       
       # 3. 生成文档
       return generate_focus_content(project_path, metrics)
   ```

2. **文件处理**
   ```python
   def safe_read_file(file_path: str) -> str:
       """安全地读取文件"""
       try:
           # 1. 检查文件大小
           if os.path.getsize(file_path) > MAX_FILE_SIZE:
               return f"File too large: {file_path}"
           
           # 2. 尝试不同编码
           for encoding in ['utf-8', 'latin-1', 'utf-16']:
               try:
                   with open(file_path, 'r', encoding=encoding) as f:
                       return f.read()
               except UnicodeDecodeError:
                   continue
           
           return f"Unable to read file: {file_path}"
       
       except Exception as e:
           return f"Error reading file: {e}"
   ```

## 7. 未来改进

1. **智能分析**
   ```python
   async def analyze_with_ai(content: str) -> Dict:
       """使用 AI 分析代码"""
       try:
           response = await openai.ChatCompletion.create(
               model="gpt-4",
               messages=[{
                   "role": "system",
                   "content": "Analyze the following code and extract key information"
               }, {
                   "role": "user",
                   "content": content
               }]
           )
           
           return parse_ai_response(response.choices[0].message.content)
       except Exception as e:
           logging.error(f"AI analysis failed: {e}")
           return {}
   ```

2. **实时预览**
   ```python
   def start_preview_server(project_path: str):
       """启动实时预览服务器"""
       app = Flask(__name__)
       
       @app.route('/')
       def preview():
           content = generate_focus_content(project_path)
           return markdown.markdown(content)
       
       app.run(port=5000)
   ```

## 8. 参考资料

1. [Python 文件处理](https://docs.python.org/3/library/os.path.html)
2. [Markdown 格式规范](https://www.markdownguide.org/)
3. [项目源代码](https://github.com/yourusername/CursorFocus) 