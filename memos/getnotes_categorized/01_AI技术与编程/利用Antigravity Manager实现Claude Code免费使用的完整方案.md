---
title: 利用Antigravity Manager实现Claude Code免费使用的完整方案
created: 2026-01-17 09:14:35
tags: ["AI链接笔记", "Claude Code", "Antigravity Manager", "Gemini模型"]
source: https://mp.weixin.qq.com/s/A-yuhpM4pFzczPzsAsfbVw
---

# 利用Antigravity Manager实现Claude Code免费使用的完整方案

# 利用Antigravity Manager实现Claude Code免费使用的完整方案
创建于：2026-01-17 09:14:35

标签：
            
            
            AI链接笔记
Claude Code
Antigravity Manager
Gemini模型

原文：[谷歌没想到：Antigravity 竟成了 Claude Code 的“免费充电宝”？](https://mp.weixin.qq.com/s/A-yuhpM4pFzczPzsAsfbVw)

### **🔍 背景与核心问题**
**用户痛点**
- **Claude使用限制**：Claude账号易被封禁，直接充值风险高；API调用成本高，尤其**vibe coding**（沉浸式编码）场景下token消耗量大。
- **谷歌资源优势**：谷歌AI IDE **Antigravity**的Pro账户提供充足的**Gemini模型**和**Claude 4.5模型**额度，且国内可低价获取（原价1680元，实际几十元）。

**核心需求**：如何将谷歌Antigravity的大模型额度转移到Claude Code中使用？

### **💡 解决方案：Antigravity Manager工具**
**工具概述**
- **名称**：Antigravity Manager（GitHub项目，已获5K星标）。
- **功能**：通过API反代技术，将Antigravity的模型额度“转移”至Claude Code，实现**免费使用Claude 4.5**。

### **📋 实施步骤详解**
**(一) 前期准备**

- **获取Gemini Pro账号**：通过闲鱼等渠道购买低价Pro账户。

- **下载安装Antigravity**：从官方渠道下载并安装谷歌AI IDE Antigravity，完成账号登录。

**(二) Antigravity Manager配置**

- **下载工具**：访问GitHub地址 https://github.com/lbjlaq/Antigravity-Manager，下载最新版本（如v3.3.3），根据系统选择对应安装包（支持Windows、macOS、Linux等）。

- **添加账号**：在工具仪表盘点击「添加账号」，通过Oauth方式登录谷歌账号，登录后可查看当前账号的**模型配额**（如Gemini 3 Pro额度92%、Claude 4.5额度77%）。

**启动API反代服务**：进入「API反代」页面，点击「启动服务」，系统生成：

- **Base URL**：http://127.0.0.1:8045

- **API密钥**：工具自动生成（需妥善保管，避免泄露）。

**(三) 与Cherry Studio集成**

**配置模型服务**：

- 打开Cherry Studio，进入「设置-模型服务-Anthropic」。

- 输入API密钥和反代地址 http://127.0.0.1:8045。

**添加模型**：

- 在「管理」中添加Claude 4.5系列模型（Sonnet 4.5、Haiku 4.5、Opus 4.5）。

- 通过「添加」功能手动输入模型ID gemini-3-pro-high，添加Gemini 3 Pro模型。

- **连通性检测**：点击「检测」按钮验证API配置是否生效。

**(四) 创建Agent并使用**

- **添加Agent**：在Cherry Studio聊天界面选择「添加Agent」（用于复杂任务处理）。

- **配置Agent**：选择已添加的Gemini 3 Pro或Claude 4.5模型，设置工作目录及权限模式。

- **功能说明**：Agent支持调用终端执行文件读写、工具调用等操作，实现类Claude Code的完整功能，无需单独下载Claude Code。

### **📝 补充细节**

- **工具版本**：Antigravity Manager v3.3.3支持账号订阅等级（PRO/ULTRA/FREE）自动识别，修复了历史消息格式校验错误。

- **模型支持**：除Claude 4.5外，还可通过自定义模型ID添加Gemini 3 Pro等谷歌模型。

- **安全性**：API密钥需本地保管，默认仅允许本机访问（127.0.0.1），可通过设置允许局域网访问。