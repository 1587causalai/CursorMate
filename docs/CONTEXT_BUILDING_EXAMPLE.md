# CursorFocus 上下文构建示例

## 示例项目

假设我们有一个典型的 React + TypeScript 项目：

```
example-project/
├── src/
│   ├── components/
│   │   ├── Header.tsx
│   │   ├── Footer.tsx
│   │   └── Dashboard.tsx
│   ├── hooks/
│   │   ├── useAuth.ts
│   │   └── useTheme.ts
│   ├── utils/
│   │   └── api.ts
│   ├── App.tsx
│   └── index.tsx
├── package.json
└── tsconfig.json
```

## 1. 上下文收集过程

### 1.1 项目基础信息收集

```python
# 项目结构分析
structure_info = {
    'files': [
        'src/components/Header.tsx',
        'src/components/Footer.tsx',
        'src/components/Dashboard.tsx',
        'src/hooks/useAuth.ts',
        'src/hooks/useTheme.ts',
        'src/utils/api.ts',
        'src/App.tsx',
        'src/index.tsx'
    ],
    'dependencies': {
        'react': '^18.2.0',
        'typescript': '^4.9.0',
        'axios': '^1.3.0'
    }
}

# 代码模式分析
code_patterns = {
    'components': [
        {
            'file': 'src/components/Header.tsx',
            'content': '''
import React from 'react';
import { useTheme } from '../hooks/useTheme';

export const Header: React.FC = () => {
    const { theme, toggleTheme } = useTheme();
    return (
        <header className={`header ${theme}`}>
            <nav>{/* ... */}</nav>
        </header>
    );
};
'''
        }
    ],
    'hooks': [
        {
            'file': 'src/hooks/useTheme.ts',
            'content': '''
import { useState, useEffect } from 'react';

export const useTheme = () => {
    const [theme, setTheme] = useState('light');
    
    const toggleTheme = () => {
        setTheme(prev => prev === 'light' ? 'dark' : 'light');
    };

    return { theme, toggleTheme };
};
'''
        }
    ]
}
```

### 1.2 代码特征提取

```python
# 分析代码模式
patterns = {
    'naming': {
        'components': 'PascalCase',
        'hooks': 'camelCase with use prefix',
        'utils': 'camelCase'
    },
    'structure': {
        'components': 'React Functional Components',
        'hooks': 'React Custom Hooks',
        'utils': 'Pure Functions'
    },
    'imports': {
        'style': 'ES6 imports',
        'organization': 'Relative paths'
    }
}

# 提取编码规范
coding_standards = {
    'typescript': {
        'prefer': [
            'Functional Components',
            'Custom Hooks',
            'Type Annotations'
        ],
        'avoid': [
            'Class Components',
            'Any Type',
            'Direct DOM Manipulation'
        ]
    },
    'react': {
        'prefer': [
            'Hooks for State',
            'Component Composition',
            'Controlled Components'
        ],
        'avoid': [
            'Multiple useEffect Dependencies',
            'Inline Styles',
            'Props Drilling'
        ]
    }
}
```

## 2. 文档生成过程

### 2.1 生成 Rules.md

```python
# 构建 Gemini AI 提示
prompt = f"""
分析这个 React + TypeScript 项目并生成编码规则：

项目结构：
{json.dumps(structure_info, indent=2)}

代码模式：
{json.dumps(patterns, indent=2)}

编码标准：
{json.dumps(coding_standards, indent=2)}

示例代码：
{code_patterns['components'][0]['content']}
{code_patterns['hooks'][0]['content']}

请生成一个 Rules.md 文件，包含：
1. 项目信息
2. 编码规则
3. 最佳实践
4. 性能考虑
"""

# Gemini AI 响应示例
rules_content = """
# Project Rules

## Project Information
- **Version**: 1.0.0
- **Name**: Example React Project
- **Language**: TypeScript
- **Framework**: React
- **Type**: Web Application

## Code Generation Style
### Preferred Patterns
- 使用函数式组件和 Hooks
- 组件使用 PascalCase 命名
- Hooks 使用 camelCase 并以 use 前缀开始
- 明确的类型注解
- 组件props使用interface定义

### Patterns to Avoid
- 避免使用 Class 组件
- 避免使用 any 类型
- 避免内联样式
- 避免过度嵌套组件
...
"""
```

### 2.2 生成 Focus.md

```python
# 收集项目指标
metrics = ProjectMetrics()
metrics.total_files = len(structure_info['files'])
metrics.files_by_type = {
    '.tsx': 5,
    '.ts': 3
}

# 分析项目结构
structure = get_directory_structure('example-project')

# 生成文档内容
focus_content = f"""
# Project Focus: Example React Project

**Current Goal:** Modern React Application with TypeScript

**Project Context:**
Type: Web Application
Target Users: End Users
Main Functionality: Interactive Dashboard

**Development Guidelines:**
- 组件驱动开发
- 类型安全
- 性能优化

# 📁 Project Structure
{structure_to_tree(structure)}

# 🔍 Key Files with Methods
`src/hooks/useAuth.ts`
- useAuth
- useAuthState
...
"""
```

## 3. 上下文构建策略

### 3.1 分层信息收集
1. **项目层面**
   - 技术栈识别
   - 依赖分析
   - 目录结构

2. **文件层面**
   - 命名规范
   - 代码组织
   - 文件关系

3. **代码层面**
   - 编码风格
   - 设计模式
   - 最佳实践

### 3.2 模式识别
1. **命名模式**
   ```typescript
   // 组件命名 (PascalCase)
   export const Header: React.FC = () => {};
   
   // Hook命名 (camelCase with use prefix)
   export const useTheme = () => {};
   ```

2. **结构模式**
   ```typescript
   // 组件结构
   import React from 'react';
   import { Props } from './types';
   
   export const Component: React.FC<Props> = () => {
       // hooks
       // handlers
       // render
   };
   ```

3. **类型模式**
   ```typescript
   // 接口定义
   interface Props {
       data: Array<Item>;
       onUpdate: (item: Item) => void;
   }
   ```

## 4. AI 提示优化

### 4.1 提示结构
```python
prompt = f"""
Project Analysis Request:

1. Context:
   - Project Type: {project_type}
   - Main Language: {language}
   - Framework: {framework}

2. Code Patterns Found:
   {json.dumps(patterns, indent=2)}

3. File Structure:
   {json.dumps(structure, indent=2)}

4. Code Samples:
   {code_samples}

Please analyze this information and generate:
1. Coding standards that match the existing patterns
2. Best practices based on the codebase
3. Performance recommendations
4. Error handling guidelines
5. Documentation requirements

Format the response as a structured markdown document.
"""
```

### 4.2 响应处理
```python
def process_ai_response(response: str) -> Dict:
    """处理 AI 响应并格式化"""
    # 解析 markdown 内容
    sections = parse_markdown_sections(response)
    
    # 提取规则
    rules = {
        'coding_standards': sections.get('Code Generation Style', {}),
        'best_practices': sections.get('Best Practices', {}),
        'performance': sections.get('Performance', {}),
        'error_handling': sections.get('Error Handling', {})
    }
    
    # 验证规则
    validate_rules(rules)
    
    return rules
```

## 5. 实际应用示例

### 5.1 规则生成
```bash
# 初始化项目分析
$ python setup.py --scan example-project

📁 Analyzing project structure...
✓ Found 8 source files
✓ Identified React + TypeScript patterns
✓ Detected coding conventions

# 生成规则文件
$ python focus.py
🤖 Generating rules...
✓ Created .cursorrules
✓ Created Focus.md
```

### 5.2 规则应用
```typescript
// 符合生成的规则
export const Dashboard: React.FC<DashboardProps> = ({ data }) => {
    const { theme } = useTheme();
    const { user } = useAuth();
    
    return (
        <div className={`dashboard ${theme}`}>
            {/* 组件实现 */}
        </div>
    );
};

// 违反生成的规则
class DashboardClass extends React.Component {  // ❌ 使用类组件
    render() {
        return (
            <div style={{ padding: '20px' }}>   // ❌ 内联样式
                {/* 组件实现 */}
            </div>
        );
    }
}
```

## 6. 持续优化

### 6.1 反馈循环
1. 收集开发者反馈
2. 调整规则生成策略
3. 优化 AI 提示
4. 更新文档模板

### 6.2 自动化改进
1. 自动检测规则违反
2. 提供修复建议
3. 更新项目文档
4. 维护规则版本

## 7. 结论

通过这个具体示例，我们可以看到：

1. **上下文构建**是一个多层次的过程，需要从项目、文件和代码三个层面收集信息

2. **AI 提示**需要结构化和完整的信息，包括：
   - 项目基础信息
   - 代码模式
   - 实际代码样例
   - 期望输出格式

3. **文档生成**是一个综合过程，需要：
   - 准确的项目分析
   - 合适的 AI 提示
   - 规范的输出格式
   - 持续的优化改进

这个过程可以确保生成的文档既符合项目的实际情况，又能提供有价值的指导。 