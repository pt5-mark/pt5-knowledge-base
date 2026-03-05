---
title: OpenClaw「中国套件」深度解析：飞书/钉钉/企微/QQ全平台AI助手集成方案
created: 2026-02-11 06:14:52
tags: ["AI链接笔记", "OpenClaw", "AI助手网关", "国内IM集成"]
source: https://mp.weixin.qq.com/s/-EChFngHnIenDib49c-8Dg
---

# OpenClaw「中国套件」深度解析：飞书/钉钉/企微/QQ全平台AI助手集成方案

# OpenClaw「中国套件」深度解析：飞书/钉钉/企微/QQ全平台AI助手集成方案
创建于：2026-02-11 06:14:52

标签：
            
            
            AI链接笔记
OpenClaw
AI助手网关
国内IM集成

原文：[OpenClaw 的「中国套件」来了：飞书钉钉企微QQ一锅端](https://mp.weixin.qq.com/s/-EChFngHnIenDib49c-8Dg)

### **🔍 OpenClaw项目背景与痛点**
**OpenClaw核心定位**

- **多渠道AI助手网关**：单个进程即可将AI能力接入WhatsApp、Telegram等数十个海外聊天平台。

- **开源影响力**：GitHub上增长最快的AI Agent项目之一，Star数已突破**140k**。

**国内生态适配缺口**

- **原生支持限制**：仅支持海外平台，**飞书、钉钉、企业微信、QQ**四大国内主流IM工具均未覆盖。

- **解决方案**：**OpenClaw-Docker-CN-IM**通过Docker镜像预装四大国内IM插件，填补适配空白。

### **🚀 中国套件核心价值**
**一站式整合方案**

- **预装四大插件**：飞书、钉钉、QQ机器人、企业微信插件全部集成至单一Docker镜像。

- **极简部署流程**：无需手动编译、安装插件或对接代码，仅需**配置环境变量→启动容器**即可完成部署。

### **💡 核心能力继承与增强**
**(一) OpenClaw原生能力**

能力项
具体说明

**多Agent路由**
支持不同聊天渠道/账号路由至独立AI Agent，每个Agent拥有独立工作空间和会话

**AI后端兼容性**
支持OpenAI协议（如GPT-4）和Anthropic协议（如Claude），兼容第三方API

**超长上下文窗口**
默认支持**200,000 tokens**，满足长对话和复杂任务需求

**开发工具集成**
内置OpenCode AI代码助手、Playwright浏览器自动化功能

**本地化功能**
中文语音合成（TTS）、Docker Volume数据持久化

**(二) 中国套件增强特性**

- **开箱即用的国内IM支持**：飞书、钉钉、企微、QQ插件预装，无需额外配置。

### **📦 三步极速部署指南**
**第一步：下载配置文件**
wget https://raw.githubusercontent.com/justlovemaki/OpenClaw-Docker-CN-IM/main/docker-compose.yml  
wget https://raw.githubusercontent.com/justlovemaki/OpenClaw-Docker-CN-IM/main/.env.example  
cp .env.example .env

**第二步：配置AI模型参数**

**基础配置（最少3个参数）**：

MODEL_ID=gpt-4  
BASE_URL=https://api.openai.com/v1  # OpenAI需带/v1，Claude无需
API_KEY=sk-your-api-key

**Claude适配示例**：

env
MODEL_ID=claude-sonnet-4-20250514  
BASE_URL=https://api.anthropic.com  
API_KEY=sk-ant-xxx  
API_PROTOCOL=anthropic-messages

#### **第三步：启动服务**
bash
docker-compose up -d
- **默认端口**：Gateway（18789）、Bridge（18790）。

### **🔌 国内IM平台配置指南**

平台
必要配置参数
备注

**飞书**
FEISHU_APP_ID、FEISHU_APP_SECRET
需手动配置事件订阅（im.message.receive_v1，长连接接收）

**钉钉**
DINGTALK_CLIENT_ID、DINGTALK_CLIENT_SECRET、DINGTALK_ROBOT_CODE
-

**QQ机器人**
QQBOT_APP_ID、QQBOT_CLIENT_SECRET
-

**企业微信**
WECOM_TOKEN、WECOM_ENCODING_AES_KEY
-

- **配置灵活性**：无需使用的平台留空即可，不影响其他平台运行。

### **⚠️ 常见问题与解决方案**

**环境变量修改不生效**

需删除 ~/.openclaw/openclaw.json 配置文件后重启容器。

**401错误**

检查API_KEY正确性及Base URL格式（OpenAI需带 /v1）。

**端口冲突**

在 .env 中修改 OPENCLAW_GATEWAY_PORT 和 OPENCLAW_BRIDGE_PORT。

**飞书消息接收异常**

- 必须在飞书开放平台完成事件订阅配置（步骤：应用管理→事件订阅→添加 im.message.receive_v1→长连接接收）。

### **🎯 典型应用场景**

**技术团队**：在飞书/钉钉群部署AI编程助手，支持实时代码提问与Review。

**客服场景**：企业微信接入AI实现7×24小时智能应答。

**个人用户**：QQ群机器人提供聊天、翻译、文案生成等功能。

- **多平台管理**：一套后端统一管控四个IM平台的对话与配置。

### **📌 项目资源**

**GitHub地址**：[https://github.com/justlovemaki/OpenClaw-Docker-CN-IM](https://github.com/justlovemaki/OpenClaw-Docker-CN-IM)

**Docker镜像**：justlikemaki/openclaw-docker-cn-im:latest

- **快速启动命令**：docker pull justlikemaki/openclaw-docker-cn-im:latest

### **补充细节**

**飞书配置关键坑点**：99%用户会遗漏事件订阅的长连接配置，导致机器人“能发不能收”。

**协议兼容性**：通过 API_PROTOCOL 参数切换OpenAI/Anthropic协议，适配不同AI模型生态。

- **数据安全**：依赖Docker Volume实现配置与工作空间持久化，容器重启后数据不丢失。