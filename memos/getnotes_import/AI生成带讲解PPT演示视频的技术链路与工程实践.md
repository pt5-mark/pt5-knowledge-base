---
title: AI生成带讲解PPT演示视频的技术链路与工程实践
created: 2025-12-03 10:40:38
tags: ["AI链接笔记", "AI视频生成", "PPT讲解视频", "多模态AI"]
source: https://mp.weixin.qq.com/s/eKUamb_BqGzopjOlbrNUlA
---

# AI生成带讲解PPT演示视频的技术链路与工程实践

# AI生成带讲解PPT演示视频的技术链路与工程实践
创建于：2025-12-03 10:40:38

标签：
            
            
            AI链接笔记
AI视频生成
PPT讲解视频
多模态AI

原文：[解密谷歌 NotebookLM 技术幕后【下】：如何用 AI 制作“带讲解的 PPT 演示视频”？](https://mp.weixin.qq.com/s/eKUamb_BqGzopjOlbrNUlA)

📽️ **核心挑战：从“听”到“看”的维度升级**

- 音频播客仅需AI“开口说话”，而PPT讲解视频需实现“文字-画面-讲解”三者对齐

- 需保证PPT风格统一、画面切换自然，无法像Sora那样天马行空生成画面

🔧 **核心架构：6步生成链路**

1. **知识抽取**

   - 输入：URL/文档/图片 → 输出：结构化Markdown文本

   - 方案：优先用轻量级工具（如JINA Reader API），失败则切换到Playwright+VLM组合

   - 工程策略：双方案自动切换，保证效率与可靠性

**结构化编剧（LLM当导演）**

LLM按定义的Slide模型生成PPT大纲，包含页码、类型、核心要点、详解、图片提示词

关键：图片提示词需包含内容+布局指令，后续统一注入风格（如简笔画）

**图片生成**

技术选择：

端到端生成（如Google Nano Banana）：理解概念后自主设计，但中文支持待优化

基于提示词绘制（如Doubao Seedream）：可控性强，适合中文场景

避坑：减少图片文字，用图标/符号替代，降低AI绘图文字错误率

**解说脚本生成（看图说话）**

输入：图片+详细知识点 → 输出：口语化讲稿（需多模态VLM模型）

优势：让讲解跟随画面（如“大家看屏幕上的三条曲线…”），而非生硬念知识点

技巧：针对主题页/章节页/总结页设计不同提示词，加入口语化表达

**语音合成**

工具：阿里CosyVoice、Qwen-tts等TTS API

优化：

音色配置项适配不同场景

用SSML标签控制停顿（<break time="500ms"/>）、强调（<emphasis>），提升自然度

**视频合成（ffmpeg缝合）**

关键：片段时长严格匹配音频时长，避免错位

优化：加入转场效果，设置编码格式、分辨率等参数

📊 **案例验证：Gemini 3官方博客生成视频**

- 输入：[https://blog.google/products/gemini/gemini-3/#note-from-ceo](https://blog.google/products/gemini/gemini-3/#note-from-ceo)

- 步骤效果：

  - 知识抽取：Jina Reader API提取Markdown

  - 结构化编剧：生成PPT大纲，如第二页提示词含“左侧列要点+右侧AI推理示意图”

  - 图片生成：Seedream绘制对应PPT页

  - 脚本生成：多模态模型结合图片产出“指着图讲”的脚本

  - 最终输出：带讲解的PPT演示视频

💡 **扩展应用**

- 仅保留“结构化编剧+图片生成”：自动生成图片式PPT（企业内训/产品介绍）

- 仅保留“脚本+TTS”：生成音频摘要（新闻/技术文章）

- 加图表生成：自动生成行业周报