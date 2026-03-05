---
title: OpenClaw（原Moltbot/Clawdbot）部署与优化完全指南
created: 2026-02-10 16:54:04
tags: ["AI链接笔记", "OpenClaw部署", "AI Agent优化", "Token消耗控制"]
source: https://mp.weixin.qq.com/s/qqt8Jef7FhOaS-BpTuxCIw
---

# OpenClaw（原Moltbot/Clawdbot）部署与优化完全指南

# OpenClaw（原Moltbot/Clawdbot）部署与优化完全指南
创建于：2026-02-10 16:54:04

标签：
            
            
            AI链接笔记
OpenClaw部署
AI Agent优化
Token消耗控制

原文：[你的OpenClaw不好用？买家秀和卖家秀？你需要这些调优。](https://mp.weixin.qq.com/s/qqt8Jef7FhOaS-BpTuxCIw)

### **📋 引言：OpenClaw的用户痛点与优化方向**
当前用户在部署和使用OpenClaw（曾用名Moltbot、Clawdbot）过程中面临四大核心问题：**安装门槛高**、**国内社交软件支持不足**、**Token消耗过快**、**能力效果未达预期**。本文针对这些问题提供系统性解决方案，降低使用门槛并提升应用体验。

### **🔧 安装部署策略**
**(一) 硬件选择建议**

- **避免盲目采购**：无需为适配Mac系统额外购买Mac mini，现有设备可充分利用。

- **低成本云服务方案**：国内云服务商提供**轻量应用服务器一键部署**，如阿里云2核2G配置年费低至68元，支持7×24小时运行及海外地域部署，可通过钉钉直接使用。

- **旧设备复用**：家庭旧电脑或设备可改造使用，但需具备基础技术能力进行配置。

- **技术用户方案**：拥有VPS资源的技术人员可直接部署至云服务器，便于故障恢复（随时重装系统）。

### **💬 国内社交软件支持优化**
**(一) 规避海外平台障碍**

- **不推荐方案**：Telegram、Whatsapp、Discord等海外平台存在注册复杂、短信验证困难、国内网络访问不稳定等问题，非出海用户建议避免。

**(二) 国内平台替代方案**

- **云服务商集成版**：阿里云（钉钉集成）、字节跳动（飞书集成）提供本土化解决方案。

- **本地部署插件**：通过社区开源的**飞书插件**实现本地化部署后的流畅使用，支持自定义身份设置（名称、类型、个性、表情符号）及SOUL.md文件协作。

### **💰 Token消耗控制策略**
**(一) 消耗现状分析**

- Agent类应用本身存在**Token消耗量大**的特性，Claude code开发场景日均消耗可达数百M Token；中端模型因推理精度不足导致的返工进一步加剧消耗。

**(二) 优化方案**

方案类型
具体选项
核心优势

**国产模型**
Kimi2.5
多模态支持、价格低廉（输入缓存命中仅0.7元/1M Token）、上下文长度262,144 tokens

Minimax2.1
提供Coding Plan（29-119元/月），适合开发场景

千问
开源路线，成本可控（作者未实测）

**API反代方案**
Antigravity Tool + Gemini订阅
支持Claude/Gemini模型接入，Pro版本有周限额，Ultra版本5小时重置额度，Token不计费

### **🚀 能力效果增强方案**
**(一) Skill插件扩展**

- **核心问题**：官方内置Skill无法满足个性化场景需求。

- **解决方案**：通过开源仓库[https://github.com/VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills)获取700+专项Skill，覆盖20+应用场景，部分核心分类如下：

分类
数量
典型功能

DevOps和云计算
41
Linux服务问题诊断、云资源管理

编码代理和集成开发环境
15
多账号管理、会话日志监控

生产力和任务
42
自动化工作流、项目管理

人工智能与法学硕士
38
法律文本分析、AI伦理评估

- **自定义扩展**：用户可自行编写Skill，适配特定任务需求。

### **📌 补充细节**

- **名称变更历史**：OpenClaw经历两次更名，依次为Clawdbot → Moltbot → OpenClaw（当前名称）。

- **社区生态**：可通过接入Moltbook平台观察OpenClaw的自主思考与社交行为，探索AI自主意识相关研究。

- **关联工具推荐**：Antigravity Tool可解决Gemini订阅地区限制问题，支持多模型API统一管理。