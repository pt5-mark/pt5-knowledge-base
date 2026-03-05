---
title: n8n-MCP：AI驱动的n8n工作流自动化工具详解
created: 2025-11-11 17:04:42
tags: ["AI链接笔记", "n8n-MCP", "工作流自动化", "AI生成工作流"]
source: https://mp.weixin.qq.com/s/ADMVOV9JClrFB4BShU_HKw
---

# n8n-MCP：AI驱动的n8n工作流自动化工具详解

# n8n-MCP：AI驱动的n8n工作流自动化工具详解
创建于：2025-11-11 17:04:42

标签：
            
            
            AI链接笔记
n8n-MCP
工作流自动化
AI生成工作流

原文：[【强烈推荐】n8n工作流自动化创建工具，开源！！](https://mp.weixin.qq.com/s/ADMVOV9JClrFB4BShU_HKw)

🔧 **核心功能与价值**

- **降低学习成本**：无需手动拖拽节点，通过自然语言描述需求，AI自动生成完整工作流

- **开源免费**：基于MIT协议开源，GitHub Stars达6.7k

- **AI桥接能力**：作为n8n与AI模型的中间层，提供525+节点的结构化访问

📊 **关键技术指标**

- **节点覆盖**：535个n8n节点（含n8n-nodes-base和langchain节点）

- **属性覆盖率**：99%节点属性覆盖，含详细 schema

- **操作覆盖率**：63.6%可用操作覆盖

- **文档覆盖率**：90%官方文档覆盖（含AI节点）

- **AI工具支持**：263个AI能力节点，附完整文档

🚀 **部署与配置指南**

1. **本地部署步骤**

bash
   git clone https://github.com/czlonkowski/n8n-mcp.git  
   cd n8n-mcp  
   npm install  
   npm run build  

2. **核心配置参数**（需替换为用户实际信息）

json
   {
     "mcpServers": {
       "n8n-mcp": {
         "command": "node",
         "args": ["/absolute/path/to/dist/mcp/index.js"],
         "env": {
           "N8N_API_URL": "https://your-n8n-instance.com",
           "N8N_API_KEY": "your-api-key"
         }
       }
     }
   }

3. **验证方法**：在Claude Code中输入/mcp命令，显示”n8n-mcp connected”即配置成功

💡 **实战案例：温州天气预报工作流**

- **需求**：每日7点获取温州天气→AI分析→生成中文报告→发送QQ邮箱

- **实现流程**（7个节点）：

  1. 定时触发（Schedule Trigger）

  2. 城市配置（Set节点：温州代码330300）

  3. 天气数据获取（HTTP Request调用高德API）

  4. AI分析（Claude模型处理天气数据）

  5. 邮件格式化（Set节点生成HTML内容）

  6. 邮件发送（Email Send节点）

  7. AI模型集成（OpenRouter节点）

- **效果**：2分钟内生成工作流，导入n8n后仅需配置API密钥即可运行

⚠️ **常见问题与解决方案**

- **邮件内容变量错误**：检查”格式化邮件内容”节点中的{{ $json.output }}表达式是否正确

- **节点连接失败**：确保n8n实例处于运行状态，API密钥权限包含workflow:create