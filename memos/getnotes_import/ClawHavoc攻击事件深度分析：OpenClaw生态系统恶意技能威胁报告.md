---
title: ClawHavoc攻击事件深度分析：OpenClaw生态系统恶意技能威胁报告
created: 2026-02-11 06:26:55
tags: ["AI链接笔记", "ClawHavoc攻击", "OpenClaw安全", "AMOS窃取器"]
source: https://mp.weixin.qq.com/s/MzAp0KwXM2mryFbiBdzgaA
---

# ClawHavoc攻击事件深度分析：OpenClaw生态系统恶意技能威胁报告

# ClawHavoc攻击事件深度分析：OpenClaw生态系统恶意技能威胁报告
创建于：2026-02-11 06:26:55

标签：
            
            
            AI链接笔记
ClawHavoc攻击
OpenClaw安全
AMOS窃取器

原文：[安全警告：ClawHub 发现 341 个恶意技能，正窃取 OpenClaw 用户数据](https://mp.weixin.qq.com/s/MzAp0KwXM2mryFbiBdzgaA)

### **🚨 事件核心数据概览**

统计项
具体数值
说明

**审计技能总数**
2,857个
ClawHub平台安全审计覆盖量

**恶意技能数量**
341个
占审计总量的11.96%

**携带木马技能**
335个
占恶意技能的98.24%，主要为AMOS窃取器

**C&C服务器地址**
91.92.242[.]30
所有恶意技能共享的命令与控制基础设施

### **01 事件概述：ClawHavoc攻击活动**
**Koi Security**研究发现，**ClawHub**平台存在大规模恶意技能攻击，被命名为**ClawHavoc**。在对2,857个技能审计中，发现341个恶意技能，其中335个通过虚假预装条件安装**Atomic Stealer (AMOS)**。

- **AMOS**：一种商品级macOS窃取器，售价**500-1000美元/月**，可收集用户敏感数据。

- **风险性质**：暴露了OpenClaw生态系统的**供应链安全风险**，与**OpenSourceMalware**报告相互印证。

### **02 攻击手法深度解析**
**社会工程学核心欺骗话术**

*“你安装了一个看似合法的技能——可能是solana-wallet-tracker或youtube-summarize-pro。该技能的文档看起来很专业。但有一个’前提条件’部分，说你需要先安装某个东西。”*

—— Koi研究员 Oren Yomtov

**攻击流程**

操作系统
诱导手段
恶意 payload

**Windows**
要求下载openclaw-agent.zip
内含键盘记录木马

**macOS**
要求复制glot[.]io脚本到终端执行
下载并安装AMOS窃取器

### **03 🎭 恶意技能伪装类型**

伪装类型
典型示例
风险等级

拼写错误
clawhub, clawhub1, clawhubb…
⚠️ 高危

加密货币工具
Solana钱包追踪器
⚠️ 高危

Polymarket机器人
polymarket-trader, polytrading
⚠️ 高危

YouTube工具
youtube-summarize, video-downloader
⚡ 中危

自动更新器
auto-updater-agent, updater
⚠️ 高危

### **04 🔍 安全研究确认**
安全研究员**6mile**指出：

> *“这些技能伪装成加密货币交易自动化工具，向macOS和Windows系统传递信息窃取恶意软件。所有这些技能共享相同的命令与控制基础设施（91.92.242[.]30），并使用复杂的社会工程学来说服用户执行恶意命令。”*

### **05 🛡️ OpenClaw应对措施**
**平台层面**

**新增举报功能**：OpenClaw创建者**Peter Steinberger**推出

每个用户最多**20个活跃举报**

超过**3个独立举报**的技能自动隐藏

**用户行动清单**

防护类型
具体措施

**立即执行**
• 检查已安装技能，卸载可疑项
• 检查~/.clawdbot/.env是否被篡改
• 更改所有API密钥和密码

**长期防护**
• 启用双重认证
• 避免安装要求”前提条件”的技能
• 不要复制粘贴未知终端命令
• 积极举报可疑技能

### **📝 补充细节**

**攻击工具商业化**：AMOS作为商品窃取器按月订阅销售，反映黑产成熟的商业模式。

**跨平台攻击**：同时针对Windows和macOS系统，扩大攻击覆盖面。

- **生态信任危机**：ClawHub作为技能平台，其审核机制存在明显漏洞，需加强安全准入控制。