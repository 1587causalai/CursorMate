# CursorFocus Rules.md 实现原理

## 1. 概述

`Rules.md` 是 CursorFocus 项目的核心配置文件，它通过结合静态代码分析和 Gemini AI 能力，为项目生成智能化的编码规则和建议。本文档详细介绍其实现原理和技术细节。

## 2. 系统架构

### 2.1 核心组件
```
CursorFocus
├── setup.py           # 项目配置管理工具
├── focus.py          # 主程序入口
├── rules_generator.py # 规则生成器
├── rules_analyzer.py  # 代码分析器
└── content_generator.py # 文档生成器
```

### 2.2 工作流程
1. **配置阶段**（setup.py）
   - 管理项目配置
   - 设置监控参数
   - 初始化项目环境

2. **监控阶段**（focus.py）
   - 实时监控项目变化
   - 触发规则更新
   - 维护项目状态

3. **分析阶段**（rules_analyzer.py）
   - 扫描项目结构
   - 分析代码特征
   - 提取编码模式

4. **生成阶段**（rules_generator.py）
   - 处理分析结果
   - 调用 AI 服务
   - 生成规则文件

## 3. 实现细节

### 3.1 代码分析机制

#### 3.1.1 文件分析
```python
def _analyze_project_structure(self):
    structure = {
        'files': [],          # 文件列表
        'dependencies': {},    # 项目依赖
        'frameworks': [],     # 使用的框架
        'languages': {},      # 编程语言
        'patterns': {         # 代码模式
            'classes': [],    # 类定义
            'functions': [],  # 函数定义
            'imports': [],    # 导入语句
            # ...
        }
    }
```

#### 3.1.2 模式识别
使用正则表达式识别各种语言的代码模式：
```python
PATTERNS = {
    'python': {
        'class': r'class\s+(\w+)(?:\((.*?)\))?\s*:',
        'function': r'def\s+(\w+)\s*\((.*?)\)(?:\s*->\s*([^:]+))?\s*:',
        'import': r'^(?:from|import)\s+([a-zA-Z0-9_\.]+)'
    },
    'javascript': {
        'class': r'class\s+(\w+)(?:\s+extends\s+(\w+))?\s*{',
        'function': r'(?:function\s+(\w+)|const\s+(\w+)\s*=\s*\([^)]*\)\s*=>)',
        'import': r'(?:import\s+.*?from\s+[\'"]([^\'\"]+)[\'"]|require\s*\([\'"]([^\'\"]+)[\'"]\))'
    }
    # ... 其他语言的模式
}
```

### 3.2 AI 集成

#### 3.2.1 环境配置
```python
# 初始化 Gemini AI (必需)
if not os.environ.get("GEMINI_API_KEY"):
    raise ValueError("GEMINI_API_KEY is required")
    
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",
    generation_config={
        "temperature": 0.7,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
    }
)
```

#### 3.2.2 提示工程
构建结构化的 AI 提示：
```python
prompt = f"""
Project Overview:
Language: {project_info['language']}
Framework: {project_info['framework']}
Type: {project_info['type']}

Project Metrics:
- Files: {metrics['files']}
- Dependencies: {metrics['dependencies']}
- Patterns: {metrics['patterns']}

Based on this analysis, create behavior rules for:
1. Code style and patterns
2. Error handling
3. Performance optimization
4. Documentation standards
"""
```

### 3.3 规则生成

#### 3.3.1 规则格式
```markdown
# Project Rules

## Project Information
- Version: 1.0.0
- Name: 项目名称
- Language: 编程语言
- Framework: 框架

## AI Behavior Rules
### Code Generation Style
#### Preferred Patterns
- 推荐模式 1
- 推荐模式 2

#### Patterns to Avoid
- 避免模式 1
- 避免模式 2
```

#### 3.3.2 降级机制
当未配置 GEMINI_API_KEY 时，系统会：
1. 使用预定义的规则模板
2. 基于项目分析结果填充模板
3. 生成基础的编码规范

### 4. 使用流程

### 4.1 初始化
```bash
# 设置必需的环境变量
export GEMINI_API_KEY=your_api_key

# 配置项目
python setup.py --scan
```

### 4.2 规则生成
```python
# 创建规则生成器实例
generator = RulesGenerator(project_path)

# 生成规则文件
rules_file = generator.generate_rules_file(project_info)
```

### 4.3 规则更新
- 监控项目变化
- 检测重要更新
- 自动更新规则

## 5. 最佳实践

### 5.1 配置建议
1. 合理设置更新间隔
2. 选择适当的扫描深度
3. 配置忽略规则

### 5.2 性能优化
1. 使用缓存减少分析开销
2. 增量更新规则文件
3. 优化正则表达式匹配

### 5.3 规则管理
1. 定期审查生成的规则
2. 手动调整特殊规则
3. 维护规则版本历史

## 6. 注意事项

1. **API 密钥管理**
   - GEMINI_API_KEY 是必需的
   - 安全存储 API 密钥
   - 避免密钥泄露
   - 定期更新密钥

2. **性能考虑**
   - 大型项目分析耗时
   - 规则生成需要网络连接
   - AI 调用可能有延迟

3. **规则维护**
   - 定期更新规则
   - 验证规则有效性
   - 处理特殊情况

## 7. 未来展望

1. **功能增强**
   - 支持更多编程语言
   - 改进 AI 模型集成
   - 增加自定义规则支持

2. **工具集成**
   - IDE 插件支持
   - CI/CD 集成
   - 团队协作功能

3. **性能优化**
   - 提升分析效率
   - 优化规则生成
   - 改进缓存机制

## 8. 参考资料

1. [Gemini AI 文档](https://ai.google.dev/docs)
2. [Python 正则表达式](https://docs.python.org/3/library/re.html)
3. [项目源代码](https://github.com/yourusername/CursorFocus) 