import os
from datetime import datetime
from typing import Dict, List, Tuple
from content_generator import ProjectMetrics, analyze_file_content
from config import load_config

class PersonalMetrics:
    def __init__(self):
        self.total_commits = 0
        self.lines_added = 0
        self.lines_deleted = 0
        self.files_modified = set()
        self.languages_used = {}
        self.recent_activities = []

def analyze_personal_activity(project_path: str) -> PersonalMetrics:
    """分析个人活动数据"""
    metrics = PersonalMetrics()
    
    # TODO: 后续添加 git 日志分析等
    # 目前先返回示例数据
    metrics.total_commits = 10
    metrics.lines_added = 500
    metrics.lines_deleted = 200
    metrics.languages_used = {
        "Python": 80,
        "Markdown": 20
    }
    metrics.recent_activities = [
        "添加了 Focus.md 生成功能",
        "优化了项目结构分析",
        "修复了配置文件读取问题"
    ]
    
    return metrics

def generate_me_content(project_path: str, config: Dict) -> str:
    """生成 Me.md 文件内容"""
    metrics = analyze_personal_activity(project_path)
    
    content = [
        "# 👤 Personal Focus",
        "",
        "## 📊 活动概览",
        f"- 总提交次数: {metrics.total_commits}",
        f"- 新增代码行数: {metrics.lines_added}",
        f"- 删除代码行数: {metrics.lines_deleted}",
        "",
        "## 💻 技术栈",
        *[f"- {lang}: {percent}%" for lang, percent in metrics.languages_used.items()],
        "",
        "## 🔄 最近活动",
        *[f"- {activity}" for activity in metrics.recent_activities],
        "",
        "## 📈 成长建议",
        "- 建议学习: 设计模式, 微服务架构",
        "- 推荐资源: 《Clean Code》, System Design课程",
        "- 下一步目标: 提升代码质量, 增强架构能力",
        "",
        f"*Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*"
    ]
    
    return '\n'.join(content) 