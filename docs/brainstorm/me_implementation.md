# Me.md 双模架构设计

## 核心定位
- 人工主导的「数字自传」
- 机器辅助的「成长画布」
- 动态更新的「认知镜像」

## 文档结构
```python:me_generator.py
def generate_me_template():
    return '''# {username} 的认知图谱

## 我的诗与远方（手动维护）
<!-- 在这里自由书写你的长期目标、价值主张和人生哲学 -->

## 经验宝库（混合模式）
### 技术履历
{auto_tech_stack}

### 代表作
<!-- 手动列出引以为豪的项目 -->

## 思维特征（半自动）
### 决策模式
{auto_decision_pattern}

### 知识边界
<!-- 手动标注擅长领域 -->

## 成长轨迹（自动生成）
### 能力进化图
```mermaid
{auto_skill_graph}
```'''
```

## 实现机制

### 手动层（用户主权区）
```python:user_profile.json
{
    "manual_sections": {
        "philosophy": "我坚信技术应该...",
        "milestones": ["2020年掌握..."]
    }
}
```

### 自动层（系统建议区）
```python:me_generator.py
def generate_auto_profile():
    return {
        'tech_radar': analyze_tech_choices(),
        'learning_velocity': calc_skill_growth()
    }
```

### 混合交互
```python:me_generator.py
def update_me_file():
    if not os.path.exists('Me.md'):
        # 初始化带注释的模板
        create_template_with_guidelines()
    else:
        # 仅更新自动生成区块
        update_auto_sections()
        # 保留手动修改痕迹
        preserve_manual_edits()
```

## 技术实现要点

### 保留人工痕迹
```python:utils/file_utils.py
def preserve_manual_edits():
    # 使用特殊注释标记自动生成区域
    # 示例：<!--- AUTO-GENERATED START -->...<!--- AUTO-GENERATED END -->
    # 非标记区域的内容完全由用户掌控
```

### 智能建议系统
```python:me_generator.py
def suggest_updates():
    # 对比用户自述与行为数据的差异
    # 示例："您自述擅长前端开发，但检测到近三月主要提交在后端..."
    # 通过PR形式提交建议，由用户决定是否采纳
```

## 演进路线

### 阶段一：静态自传
- 纯Markdown模板
- 自由格式书写
- 基础元数据收集

### 阶段二：智能助手
- 差异检测提醒
- 写作建议生成
- 版本对比功能

### 阶段三：双向成长
- 用户与AI共同编辑
- 认知分歧可视化
- 自我反思提示系统
```

这个方案的优势：
1. **用户主权**：核心思想表达完全自主
2. **人机协作**：系统只在不擅长的领域（数据分析）提供辅助
3. **演进可能**：为未来更深入的自我认知留出接口
4. **符合直觉**：像维护个人博客一样自然

需要特别注意的实现细节：
1. 严格的版本控制（用户随时可回退）
2. 清晰的区域划分（避免机器覆盖人工内容）
3. 差异提示的友好性（以建议而非纠正的方式呈现）