---
title: X推文采集报告生成与优化指南 📊
created: 2025-11-13 16:44:26
tags: ["AI链接笔记", "X推文采集", "Claude Code", "数据可视化"]
source: https://mp.weixin.qq.com/s/q-FvSxmxV18tjQDIRffNMA
---

# X推文采集报告生成与优化指南 📊

# X推文采集报告生成与优化指南 📊
创建于：2025-11-13 16:44:26

标签：
            
            
            AI链接笔记
X推文采集
Claude Code
数据可视化

原文：[Google浏览器MCP真好用：用Claude Code快速实现了推文爬取系统](https://mp.weixin.qq.com/s/q-FvSxmxV18tjQDIRffNMA)

### 报告概览

- **基础数据**：推文总数17条、关键词10个、生成时间2025-11-07 17:56:19

- **时间范围**：最近3天，最小观看数≥100

- **核心功能**：支持按内容/用户名搜索，提供最新发布/最多观看/最多点赞/最多互动4种排序方式

### 关键推文案例

**Sam Altman**

内容：”GPT-6 will be renamed GPT-6-7, you’re welcome”

互动数据：1379.0万观看、4.4万点赞、4.0K转发、4.4K评论

**柴郡 | Crypto+AI Plus**

内容：推荐GPT个性化设置提示词

互动数据：53.0万观看、1.8K点赞、284转发、20评论

**AI Frontliner**

内容：”72+ AI tools to finish months of work in minutes”

互动数据：37.0万观看、2.8K点赞、731转发、57评论

### 实现步骤
1. 安装Claude Code浏览器MCP
claude mcp add chrome-devtools npx chrome-devtools-mcp@latest

⚠️ 注意：需手动执行命令，避免AI自动安装错误

2. 绕过X网站登录限制

**问题**：无法复用登录态，MCP窗口手工登录失败

**解决方案**：从浏览器请求头复制Cookie，通过JavaScript脚本注入实现登录

3. 可视化输出功能

**核心特性**：排序功能（观看/点赞/互动等）、卡片式展示、搜索功能

**优化点**：

按AI方向关键词筛选内容

自动下拉加载feed流

- 长推文内容限制显示5行