# CursorFocus 使用教程

## 项目简介

CursorFocus 是一个强大的项目监控和分析工具，它能够自动追踪和分析你的代码项目，生成项目文档，并提供实时的项目状态更新。

## 功能特点

- 🔍 自动扫描和发现项目
- 📊 实时项目状态监控
- 📝 自动文档生成
- ⚙️ 灵活的配置选项
- 🚀 支持多项目同时监控

## 快速开始

### 1. 基础配置

首先需要运行配置脚本来设置你要监控的项目：

```bash
python setup.py --scan
```

这个命令会：
- 扫描当前目录下的所有可监控项目
- 显示发现的项目列表
- 让你选择要监控的项目

### 2. 项目管理命令

#### 添加项目
```bash
# 添加单个项目
python setup.py --projects /path/to/your/project

# 添加多个项目
python setup.py --projects /path/to/project1 /path/to/project2

# 添加项目并指定自定义名称
python setup.py --projects /path/to/project --names "My Project"
```

#### 查看项目
```bash
# 列出所有已配置的项目
python setup.py --list
```

#### 移除项目
```bash
# 通过名称移除项目
python setup.py --remove "项目名称"

# 通过索引移除项目
python setup.py --remove 1

# 移除所有项目
python setup.py --remove all
```

### 3. 配置说明

每个项目的配置包含以下参数：
- `name`: 项目名称
- `project_path`: 项目路径
- `update_interval`: 更新间隔（默认60秒）
- `max_depth`: 最大扫描深度（默认3层）

### 4. 高级用法

#### 自定义扫描
```bash
# 扫描指定目录
python setup.py --scan /path/to/directory

# 扫描当前目录
python setup.py --scan .
```

#### 批量操作
```bash
# 添加多个项目并指定名称
python setup.py --projects /path/1 /path/2 --names "Project1" "Project2"
```

## 注意事项

1. **路径处理**
   - 所有项目路径都会被自动转换为绝对路径
   - 支持相对路径输入，会自动转换

2. **项目命名**
   - 自动清理项目名称中的常见后缀（-main, -master 等）
   - 自动处理重名项目，添加数字后缀

3. **配置文件**
   - 配置保存在 `config.json` 文件中
   - 自动创建和管理配置文件
   - 建议不要手动修改配置文件

4. **性能考虑**
   - 合理设置更新间隔，避免过于频繁的扫描
   - 适当设置扫描深度，避免扫描过多无关文件

## 常见问题

1. **Q: 如何修改项目的更新间隔？**
   A: 目前需要直接修改 config.json 文件，后续版本会添加命令行支持。

2. **Q: 支持哪些类型的项目？**
   A: 支持所有常见的项目类型，包括但不限于：
   - Python 项目
   - JavaScript/Node.js 项目
   - Java 项目
   - 等等...

3. **Q: 如何停止监控？**
   A: 可以通过 `--remove` 命令移除项目，或者直接停止运行中的监控进程。

## 最佳实践

1. **项目组织**
   - 建议将相关项目放在同一目录下统一管理
   - 使用有意义的项目名称

2. **监控策略**
   - 根据项目大小和更新频率设置合适的更新间隔
   - 只监控真正需要关注的项目

3. **资源管理**
   - 定期清理不再需要监控的项目
   - 避免同时监控过多项目

## 更新日志

### v1.0.0
- 初始版本发布
- 支持基础的项目监控功能
- 提供命令行配置界面

## 反馈与支持

如果你在使用过程中遇到任何问题，或有任何建议，欢迎：
1. 提交 Issue
2. 发送反馈
3. 贡献代码

---

希望这个教程能帮助你更好地使用 CursorFocus！如果还有任何问题，随时查阅本文档或寻求帮助。 