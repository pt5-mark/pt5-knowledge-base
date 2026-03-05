---
title: 📝 n8n本地部署与首次启动完整教程
created: 2025-11-11 18:55:29
tags: ["AI链接笔记", "n8n本地部署", "Docker容器配置", "工作流持久化存储"]
source: https://mp.weixin.qq.com/s/BQG1Zb4G4brN42isEsIbhw
---

# 📝 n8n本地部署与首次启动完整教程

# 📝 n8n本地部署与首次启动完整教程
创建于：2025-11-11 18:55:29

标签：
            
            
            AI链接笔记
n8n本地部署
Docker容器配置
工作流持久化存储

原文：[Docker首次启动n8n的图文教程](https://mp.weixin.qq.com/s/BQG1Zb4G4brN42isEsIbhw)

### 🔍 前期准备

**文件夹创建**

在桌面或指定路径新建n8n文件夹（用于持久化存储工作流数据，需妥善保管避免误删）

### 📌 核心操作步骤

**Docker界面操作**

左侧导航栏点击Images

找到n8nio/n8n:latest镜像，点击右侧▶️图标启动容器

**容器配置参数**

| 配置项         | 数值/路径                          | 说明                          |
|—————-|———————————–|——————————-|
| Container name | wenzhuo（示例）                 | 自定义容器名称便于识别        |
| Host port      | 5678                            | 本地访问端口                  |
| Container path | /home/node/.n8n                 | 容器内数据存储路径            |
| Host path      | C:\Users\Administrator\Desk（示例） | 本地映射文件夹路径            |

**启动与访问**

完成配置后点击Run按钮

在容器日志中找到地址http://localhost:5678，点击即可打开n8n编辑器

### ⚠️ 关键注意事项

**路径格式**：容器路径必须以/开头（如/home/node/.n8n）

**端口冲突**：确保5678端口未被占用，否则需修改Host port

- **数据安全**：本地n8n文件夹需定期备份，防止工作流丢失