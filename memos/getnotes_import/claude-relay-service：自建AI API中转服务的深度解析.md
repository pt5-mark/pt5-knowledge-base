---
title: claude-relay-service：自建AI API中转服务的深度解析
created: 2026-02-02 00:16:24
tags: ["AI链接笔记", "claude-relay-service", "AI API中转", "开源项目"]
source: https://mp.weixin.qq.com/s/adib8wfnemT-vOIqOXj6XA
---

# claude-relay-service：自建AI API中转服务的深度解析

# claude-relay-service：自建AI API中转服务的深度解析
创建于：2026-02-02 00:16:24

标签：
            
            
            AI链接笔记
claude-relay-service
AI API中转
开源项目

原文：[白嫖 Claude 和 Gemini 官方额度，同时自建 AI 中转站（隐私安全），7.5K人都在用](https://mp.weixin.qq.com/s/adib8wfnemT-vOIqOXj6XA)

### **🔍 项目概述**
**claude-relay-service**是一个开源的API中转服务项目，旨在解决Claude、Gemini等AI服务访问受限、第三方镜像站数据安全风险及官方免费额度利用问题。该项目在GitHub上已获得**7.5K Star**，支持直连官方API，提供一站式中转解决方案。

**核心定位**：CRS-自建Claude Code镜像，一站式开源中转服务，支持Claude、OpenAI、Gemini、Droid订阅统一接入，支持拼车共享以高效分摊成本，实现原生工具无缝使用。

### **✨ 核心亮点**

- **支持免费额度利用**：无需付费订阅即可使用高质量AI模型，包括Antigravity渠道（免费用Claude Opus）和Gemini CLI免费额度（每天1000次调用）。

- **直连官方API**：不经过第三方镜像站，数据仅在用户服务器与官方之间流转，保障隐私安全。

- **多人拼车功能**：支持付费订阅多人拼车分摊费用，系统自动轮换账号，提升可用性。

### **🚀 核心功能**
**(一) 免费额度利用**

- **Antigravity渠道**：免费使用Claude Opus 4.5等高级模型。

- **Gemini CLI免费额度**：每天1000次免费调用，支持Gemini-2.5-Pro模型及100万token上下文。

**请求路由分流机制**：
| 路由路径 | 对应渠道 |
| :— | :— |
| /api | 付费Claude账号池 |
| /antigravity/api | Antigravity免费渠道 |
| /gemini | Gemini CLI免费额度 |

系统支持多账户自动轮换，额度用完自动切换下一个账号，最大化利用免费资源。

**(二) 付费订阅与拼车**
支持Claude Code Max付费订阅，支持多人拼车分摊成本。系统自动轮换账号，某个账号出问题时立即切换，保障服务连续性。

**(三) 多客户端接入支持**

- **命令行工具**：Claude Code、Gemini CLI等。

- **第三方应用**：Cherry Studio、Continue等开发工具。

- **API格式**：支持Claude标准格式和OpenAI兼容格式。

配置完成后，只需设置API地址和密钥即可使用。

**(四) Web管理界面**
提供直观的Web管理界面，无需命令行操作，主要功能模块包括：
* **仪表盘**：展示请求统计、账户状态、token使用量等核心指标。
* **API密钥管理**：分配独立API Key，支持设置速率限制、并发限制。
* **账户管理**：查看账户余额、状态，支持添加新账户。
* **使用统计**：展示用户token使用量、花费等成本信息。

**(五) 隐私与安全**

- 所有请求直连官方API，不经过第三方。

- 支持JWT认证、加密密钥管理等安全机制。

### **📥 部署流程**
推荐采用**脚本部署**方式，步骤如下：

**第一步：执行安装脚本**
curl -fsSL https://pincc.ai/manage.sh -o manage.sh && chmod +x manage.sh && ./manage.sh install  

脚本自动完成系统环境检测、依赖安装（Node.js、Redis等）、交互式配置及服务启动，整个过程约3-5分钟。

**第二步：访问管理界面**
浏览器访问 http://服务器IP:3000/web，使用data/init.json文件中的管理员账号登录。

**第三步：添加账户**
点击「Claude账户」→「添加账户」→「生成授权链接」，完成登录授权后复制返回的Authorization Code。（国内用户需科学上网完成授权）

**第四步：创建API Key并使用**
在Web界面点击「API Keys」→「创建新Key」，设置名称和使用限制。根据使用场景配置环境变量：

使用场景
环境变量配置

Antigravity免费渠道
export ANTHROPIC_BASE_URL="http://服务器:3000/antigravity/api/"
export ANTHROPIC_AUTH_TOKEN="API密钥"

Gemini CLI免费额度
export CODE_ASSIST_ENDPOINT="http://服务器:3000/gemini"
export GOOGLE_CLOUD_ACCESS_TOKEN="API密钥"
export GOOGLE_GENAI_USE_GCA="true"

付费Claude Code Max
export ANTHROPIC_BASE_URL="http://服务器:3000/api/"
export ANTHROPIC_AUTH_TOKEN="API密钥"

**常用管理命令**：
- crs status：查看服务状态
- crs restart：重启服务
- crs update：更新到最新版
- crs stop：停止服务

### **💡 补充细节**

- **项目价值**：对于个人开发者，免费额度（Antigravity渠道的Claude Opus、Gemini CLI每天1000次调用）通常已满足需求；免费额度不足时，可通过付费订阅拼车进一步降低成本。

- **数据安全**：相比第三方镜像站，自建服务器直连官方API的方式大幅降低数据泄露风险。

- **技术门槛**：具备基础服务器操作能力即可部署使用，适合有一定技术基础的用户。