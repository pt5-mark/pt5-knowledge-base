---
title: OpenClaw成本优化方案：qmd+MCP实现Token消耗降低90%的实战指南
created: 2026-02-11 06:30:39
tags: ["AI链接笔记", "OpenClaw优化", "Token消耗降低", "qmd搜索引擎"]
source: https://mp.weixin.qq.com/s/_TPEdjCJOzFt9M5JHMAAug
---

# OpenClaw成本优化方案：qmd+MCP实现Token消耗降低90%的实战指南

# OpenClaw成本优化方案：qmd+MCP实现Token消耗降低90%的实战指南
创建于：2026-02-11 06:30:39

标签：
            
            
            AI链接笔记
OpenClaw优化
Token消耗降低
qmd搜索引擎

原文：[怒省 1 亿 Token：用 qmd 给你的 Agent 装上「本地大脑」](https://mp.weixin.qq.com/s/_TPEdjCJOzFt9M5JHMAAug)

### **💡 核心问题与解决方案概述**
**痛点分析**：AI Agent（如OpenClaw）在运行中存在**Token消耗过快**问题，主要原因是每次调用模型时需将全部历史对话、文档和记忆塞入上下文，导致无关内容浪费资源、拖慢响应并降低准确度。

**解决方案**：提出**qmd + MCP + OpenClaw**集成方案，通过本地语义搜索实现精准记忆检索，仅将相关内容送入模型，实测可将Token消耗压缩至原来的1/10，检索精准度达90%以上。

### **🔍 qmd：Agent专用本地语义搜索引擎**
**核心定位**
qmd是Shopify创始人Tobi用Rust开发的**本地语义搜索引擎**，专为AI Agent设计的记忆组件，提供高质量混合检索能力，使Agent在调用模型前先进行精准”记忆查询”。

**核心特性**

特性
说明

**知识载体支持**
搜索markdown笔记、会议记录、文档等日常知识载体

**混合搜索能力**
BM25全文检索 + 向量语义检索 + LLM重排序，兼顾召回率与精准度

**本地运行模式**
使用GGUF模型，无需外部API；Embedding和Reranker模型下载后可离线使用

**MCP原生集成**
可作为工具被Agent调用，实现”自主回忆”，无需手动复制上下文

**模型组件**
首次运行自动下载两类模型：
- **Embedding模型**：jina-embeddings-v3（约330MB）
- **Reranker模型**：jina-reranker-v2-base-multilingual（约640MB）

### **🚀 10分钟上手：qmd本地记忆库搭建流程**
**Step 1：安装qmd**
通过bun包管理器一键安装：

bun install -g https://github.com/tobi/qmd
```> 首次运行会自动下载所需模型，完成后即可离线使用

#### **Step 2：创建记忆库并生成Embedding**

以OpenClaw工作目录`~/clawd`为例，创建两层记忆空间：
```bash
# 进入OpenClaw工作目录
cd ~/clawd  

# 创建"日常日志库"：索引memory文件夹下的md文件
qmd collection add memory/*.md --name daily-logs  
qmd embed daily-logs memory/*.md  

# 创建"工作空间库"：索引根目录核心markdown文件
qmd collection add *.md --name workspace
qmd embed workspace *.md
```> 索引速度：12个文件仅需数秒，全程本地完成

#### **Step 3：测试检索效果**

qmd提供三种检索模式，推荐使用混合搜索：

| 检索模式 | 命令示例 | 精准度 | 适用场景 |
|---------|---------|--------|---------|
| **混合搜索** | `qmd search daily-logs "关键词" --hybrid` | **93%** | 默认推荐，兼顾召回与精准 |
| **纯语义搜索** | `qmd search daily-logs "关键词"` | 59% | 记忆模糊、关键词难描述场景 |
| **关键词搜索** | `qmd search daily-logs "关键词" --keyword` | - | 传统全文检索需求 |

### **🔄 MCP集成：实现Agent自主"翻笔记"**

#### **集成配置**

创建`config/mcporter.json`配置文件：
```json
{  
  "mcpServers": {    
    "qmd": {      
      "command": "/Users/你的用户名/.bun/bin/qmd",      
      "args": ["mcp"]    
    }  
  }
}

**核心工具接口**
qmd通过MCP暴露以下工具：
- query：混合搜索（默认最推荐，精度最高）
- vsearch：纯语义检索
- search：关键词检索
- get/multi_get：根据ID精准获取文档片段
- status：健康检查

**工作流程**

- Agent收到用户问题后，通过MCP调用qmd的query工具

- qmd返回高相关片段（约200 Token）

- Agent拼接精简上下文后调用LLM

- 生成最终回答（Token消耗远少于全量MEMORY.md）

### **📊 实战效果：Token消耗立省90%**
**场景一：回忆用户偏好**

- **传统方案**：将2000 Token的完整MEMORY.md塞入上下文，其中90%内容无关

- **qmd方案**：仅返回约200 Token的高相关片段

- **效果**：Token消耗减少约90%，答案更精准集中

**场景二：跨文件知识检索**

- **传统痛点**：相关内容散落在不同文件，需手动指定或全量塞入

- **qmd方案**：统一索引多文件集合，跨文件回忆准确率约93%

- **优势**：支持多天、多项目、多话题历史记录的精准检索

### **🔧 持续维护：自动增量更新机制**
建议将embed命令加入heartbeat或cron任务，实现记忆库自动更新：
bash
qmd embed daily-logs memory/*.md
qmd embed workspace *.md
> 可集成到开发流程（如更新日志后自动触发），确保Agent始终拥有最新记忆

### **📌 关键洞察**

- **技术趋势**：大模型专注”推理与生成”，本地工具负责”记忆与检索”，通过MCP协议松耦合集成，实现降本、增效、隐私安全提升

- **成本效益**：按Claude API成本估算，该方案可实现”怒省1亿”级别的长期成本优化

- **适用范围**：不仅适用于OpenClaw，也可扩展至vibe coding及各类自研Agent框架