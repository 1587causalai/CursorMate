# CursorMate

> 打造真正懂你的智能助手 - 超越项目监控，走向个性化协作

我们的阶段性产品是一个 MCP server：https://www.npmjs.com/package/@1587causalai/me-server

### 项目的演进与新方向

`CursorMate` 最初源于对 `CursorFocus` ([https://github.com/RenjiYuusei/CursorFocus](https://github.com/RenjiYuusei/CursorFocus)) 项目的探索。`CursorFocus` 旨在通过生成项目特定的上下文文件（如 `.cursorrules` 和 `Focus.md`）来增强 AI 的代码理解能力。

然而，在深入思考如何才能最大化 AI 对开发者的辅助价值后，我们认为 `CursorMate` 的使命需要超越 `CursorFocus` 原有的范畴。虽然 `.cursorrules` 等具体概念仍有其参考价值，但我们判断，仅仅停留在项目级上下文优化，对于实现真正"懂你"的 AI 助手而言，其"[[cursorrules_vs_focus]] 存在意义并不大！"——这正是驱动我们进行战略调整的核心洞察。

**`CursorMate` 的核心思路已转向构建一个基于 MCP (My Context Provider) server 架构的个性化协作平台。** 我们相信，通过深度整合开发者的个人履历、当前负责的多个项目详情、乃至个人的认知内核与思考模式，才能打造出真正贴合个体需求的智能助手。当前我们的阶段性产品（即上方链接的 MCP server npm 包）正是这一新方向的初步实践。

这代表着一个重要的战略转向：
- 原先基于 `CursorFocus` fork 的代码库将不再作为主要开发阵地进行更新。
- 未来的所有努力将聚焦于 MCP server 的研发与完善，这才是 `CursorMate` 实现其宏大愿景的技术路线。

我们致力于将 `CursorMate` 从一个项目上下文工具，进化为一个能够深度理解并赋能每一位开发者的个性化智能伙伴。

## 愿景

CursorMate 致力于创建一个能真正理解你的 AI 协作环境。我们相信：
- 🎯 最了解自己的是自己
- 🤝 最好的协作来自深度理解
- 🌱 个性化信息是最宝贵的上下文

个人信息融入的三个维度: 1) 个人简历; 2) 12个正在进行的项目; 3) 自己的认知内核.

认知内核包括:
- 原始世界信念
- 我的专业知识背后的关键理念
  - all models are wrong, but some are useful
  - 统计思维
  - 系统思维
- DiscoSCM 的认知内核


## 核心功能

CursorMate 不仅仅是一个项目监控工具，它是：

- 🧠 个性化上下文管理器
  - 个人信息收集
  - 认知内核跟踪

- 🔍 智能交互优化器
  - 自动整合相关上下文
  - 引导提出更好的问题

- 📈 持续学习伙伴
  - 记录思考过程演进
  - 长期目标追踪



## 快速开始

查看 [使用教程](USAGE.md) 开始使用 CursorMate。

## 为什么选择 CursorMate？

在与大模型交互时，效果取决于三个关键因素：
1. 上下文是否充分准确
2. 问题描述是否合适
3. 对话模型的智能水平

CursorMate 不仅致力于优化上下文提供，更进一步帮助你提出更好的问题，实现真正的个性化协作。


## 竞品分析


Mem0 调研: https://swze06osuex.feishu.cn/docx/UBN4dTLYuomE5lxexQkcQGiEn5c


## 灵魂拷问

为什么要写 .cursorrules 文件？ 如何写好 .cursorrules 文件？ 写好这个文件有什么好处？够了吗？

cursorrules 也有升级版本 notepads

有了 cursor 之后, 为什么还需要这个项目?

CursorMate 是增强 cursor 的智能助手, 帮助 cursor 更好的理解用户的过往经验和认知偏好, 从而优化其本身的上下文提供机制, 更好的理解用户需求, 从而得到更好的回答. 当前的做法没有充分使用用户个体信息, 更完备的用户信息意味着更好的上下文和更本质的理解用户需求. 他是用户的私有信息, 用户可以完全控制(可以有很多个版本的自己, 最准确的一定是最好的), 让我们的项目有了不可替代的性质. 

所以既能够提供独特的功能, 也能够有不可替代性. 进一步, 我们的还有诗和远方, 我们希望打造一个真正懂你的智能助手, 超越项目监控, 走向个性化协作, 走向人类最深入的自我认知之路. 

