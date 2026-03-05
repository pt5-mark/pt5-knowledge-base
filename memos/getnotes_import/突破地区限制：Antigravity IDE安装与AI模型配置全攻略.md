---
title: 突破地区限制：Antigravity IDE安装与AI模型配置全攻略
created: 2025-12-13 09:00:48
tags: ["AI链接笔记", "Antigravity IDE", "地区限制突破", "Google账号归属地"]
source: https://mp.weixin.qq.com/s/ddJ5zEFbRkCrKoI80TybiQ
---

# 突破地区限制：Antigravity IDE安装与AI模型配置全攻略

# 突破地区限制：Antigravity IDE安装与AI模型配置全攻略
创建于：2025-12-13 09:00:48

标签：
            
            
            AI链接笔记
Antigravity IDE
地区限制突破
Google账号归属地

原文：[终于用上Antigravity了，谷歌地区限制解除！](https://mp.weixin.qq.com/s/ddJ5zEFbRkCrKoI80TybiQ)

### **🚀 核心成果概述**
用户成功解决**Antigravity IDE**的地区限制问题，实现对**Gemini 3 Pro**和**Claude Sonnet 4.5**等AI模型的访问。关键突破点在于通过修改Google账号归属地，而非单纯依赖VPN工具，最终完成软件安装与配置。

### **🔍 地区限制问题解析**
**(一) 限制本质**

- **核心矛盾**：传统认知中”更换IP即可解决地区限制”存在误区，实际关键在于**Google账号归属地**判定。

- **常见误导方案**：GPT及常规建议多提及本地工具、账号语言、系统语言、手机号/信用卡绑定等，均未触及根本。

**(二) 关键判定依据**

- **归属地查询方法**：访问https://policies.google.com/terms，页面底部”国家/地区版本”显示当前账号归属地（示例中显示”美国”为成功状态）。

- **限制表现**：若显示”中国”或”香港”，将无法访问Antigravity及相关AI模型服务。

### **🔧 归属地修改全流程**
**(一) 申请入口**

- **官方渠道**：通过https://policies.google.com/country-association-form提交地区变更申请。

**(二) 关键配置项**

字段
推荐设置
注意事项

**国家/地区**
美国
需与后续州信息匹配

**州**
加利福尼亚州
示例中红色框选，为高通过率选项

**申请理由**
1. ✅ 我在过去一年内搬到了这里
2. ✅ 我经常使用虚拟专用网(VPN)
单勾选”VPN”可能导致申请失败，建议双选

**(三) 审核结果**

- **反馈时效**：用户案例显示”周末审核通过”，无明确官方时效说明。

- **成功标志**：收到Google邮件通知，确认”账号关联地区改为美国-加利福尼亚州”。

### **💻 Antigravity安装与配置**
**(一) 软件下载**

- **官方地址**：https://antigravity.google/，支持Windows/macOS/Linux三大系统（含苹果M系列芯片）。

**(二) 安装步骤**

- **下载文件**：点击”Download for Windows”（以Windows为例）。

**安装向导**：

- 接受用户协议（默认路径需701.9MB空间）。

- 关键提示：若以管理员身份运行，会触发”User Installer”警告，建议直接点击”确定”继续。

**初始化配置**：

- 主题选择（Dark/Solarized Light等四种预设）。

- Agent使用方式：推荐选择”Agent-driven development”（智能体驱动开发）。

**(三) 账号登录**

- **核心验证**：通过”Sign in with Google”完成授权，需确保已完成归属地修改且生效。

- **成功标志**：进入主界面，显示已保存的工作区（如”topai”、”youtube”、”time”）。

### **🤖 AI模型配置与验证**
**(一) 可用模型列表**
在右侧”Agent”面板中，通过模型选择下拉菜单确认以下选项可用：
- **Gemini 3 Pro (High)**
- **Gemini 3 Pro (Low)**
- **Claude Sonnet 4.5**
- **Claude Sonnet 4.5 (Thinking)**
- **GPT-OSS 120B (Medium)**

**(二) 使用建议**

- **场景分工**：可将不同模型分配至前端开发、后端开发、代码审查等专项任务。

- **当前状态**：处于免费使用阶段，智能体(Agent)功能尚未详细测试。

### **📝 补充细节**

- **账号历史影响**：长期”潜伏”美区的账号（如曾收到Google美区服务邮件）可能提升申请通过率。

- **多账号差异**：美区注册且使用英语的账号，修改申请可能延迟或失败，需耐心等待审核。

- **软件特性**：基于VS Code开发，支持导入VS Code配置，适合熟悉该环境的用户快速上手。