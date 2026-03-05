---
title: Clawdbot本地部署与使用完全指南（2026年最新版）
created: 2026-02-10 16:59:14
tags: ["AI链接笔记", "Clawdbot部署教程", "AI助理工具", "本地AI部署"]
source: https://mp.weixin.qq.com/s/yiXpptHUwxXPAQzajBj6sg
---

# Clawdbot本地部署与使用完全指南（2026年最新版）

# Clawdbot本地部署与使用完全指南（2026年最新版）
创建于：2026-02-10 16:59:14

标签：
            
            
            AI链接笔记
Clawdbot部署教程
AI助理工具
本地AI部署

原文：[保姆级Clawdbot 的部署教程](https://mp.weixin.qq.com/s/yiXpptHUwxXPAQzajBj6sg)

### **📋 部署准备与环境要求**

- **系统兼容性**：支持macOS、Linux及Windows（PowerShell）系统，其中Windows环境未经过测试。

- **安全提示**：建议使用**无重要数据的电脑**进行部署，需保持网络通畅（原文提及”mofa畅通”）。

### **🔧 安装Clawdbot（步骤一）**
根据操作系统选择对应安装命令：

操作系统
安装命令

**macOS/Linux**
`curl -fsSL [https://clawd.bot/install.sh](https://clawd.bot/install.sh)

**Windows (PowerShell)**
`iwr -useb [https://clawd.bot/install.ps1](https://clawd.bot/install.ps1)

执行后需耐心等待安装完成，过程中保持网络连接。

### **⚙️ 配置Clawdbot（步骤二）**
**1. 启动快速设置模式**
bash
clawdbot onboard --flow quickstart
- **版本信息**：当前部署版本为**Clawdbot 2026.1.24-3（885167d）**
- **安全协议**：需阅读安全文档（https://docs.clawd.bot/security），确认风险后选择**“Yes”**继续。

**2. 网关配置参数**

参数项
默认值
说明

**Gateway port**
18789
服务端口

**Gateway bind**
Loopback (127.0.0.1)
本地回环地址

**Gateway auth**
Token (default)
认证方式

**Tailscale exposure**
Off
远程访问开关

**3. 模型/认证提供商选择**
支持多平台API集成，原文示例选择**Google (Gemini API key + OAuth)**，其他可选包括：
- OpenAI / Anthropic / MiniMax / Qwen / Synthetic / Venice AI / Copilot / OpenRouter / Vercel AI Gateway / Moonshot AI / Z.AI (GLM 4.7) / OpenCode Zen

**4. 输入API密钥**
在配置流程中需提供**Google Gemini API key**，完成身份验证。

**5. 链接通讯工具**

- **推荐方案**：通过扫描二维码链接**WhatsApp**，完成后将生成专用联系人（格式：电话号码+（你））。

- **其他选项**：支持Slack/Discord/钉钉（需额外搜索钉钉接入教程）。

**6. 技能与钩子安装**
需选择安装**Claude Skill**和**hook**（可理解为AI功能扩展模块），完成后启动本地聊天界面。

### **🚀 实战应用（步骤三）**
**核心功能演示**

- **基础交互**：通过聊天界面发送指令，如”画图”、”收集AI资讯”。

- **高级应用**：已验证用例包括餐厅预订、脚本编写等自动化任务。

**部署完成界面选项**

启动方式
说明

**Hatch in TUI (推荐)**
终端用户界面启动

**Open the Web UI**
网页界面启动

**Do this later**
稍后启动

### **💡 Clawdbot核心优势**

- **生态壁垒打破**：整合多平台工具与服务，实现跨软件协同。

- **生产力解放**：支持构建”数字员工队伍”，已有用户批量部署（如使用Mac mini集群）。

### **📝 补充细节**

- **安全风险提示**：Clawdbot代理可执行命令、读写文件，建议采用**沙箱模式**和**最小权限原则**（参考文档：[https://docs.clawd.bot/sandboxing）。](https://docs.clawd.bot/sandboxing）。)

- **令牌管理**：网关令牌存储路径为~/.clawdbot/clawdbot.json（gateway.auth.token），或通过环境变量CLAWDBOT_GATEWAY_TOKEN获取；可随时通过命令clawdbot dashboard --no-open生成令牌链接。