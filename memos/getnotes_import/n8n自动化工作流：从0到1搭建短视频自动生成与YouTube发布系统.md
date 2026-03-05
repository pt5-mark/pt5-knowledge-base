---
title: n8n自动化工作流：从0到1搭建短视频自动生成与YouTube发布系统
created: 2025-11-22 16:25:38
tags: ["AI链接笔记", "n8n工作流", "短视频自动化", "YouTube发布"]
source: https://mp.weixin.qq.com/s/I6o5ikAtSAXwTVrJCHdB1A
---

# n8n自动化工作流：从0到1搭建短视频自动生成与YouTube发布系统

# n8n自动化工作流：从0到1搭建短视频自动生成与YouTube发布系统
创建于：2025-11-22 16:25:38

标签：
            
            
            AI链接笔记
n8n工作流
短视频自动化
YouTube发布

原文：[从0到1玩转 n8n：1分钟学会自动生成短视频并一键发布到 YouTube](https://mp.weixin.qq.com/s/I6o5ikAtSAXwTVrJCHdB1A)

🔧 **核心工作流逻辑**

- **输入触发**：通过表单提交视频主题

- **AI生成**：调用DeepSeek API生成结构化脚本（含分镜旁白、标题、角色、标签）

- **多分支并行**：拆分6个分镜，同步调用KIE生图API生成对应插画（水彩风格，参考Eric Carle艺术）

- **视频合成**：通过Creatomate模板合并分镜图与ElevenLabs语音

- **自动化发布**：视频生成后自动上传至YouTube（需处理Shorts类别ID限制）

📊 **关键API配置**

- **DeepSeek**：生成脚本需启用Structured Output Parser，确保JSON格式输出

- **ElevenLabs**：创建API Key时需开放Text to Speech等全权限

- **KIE生图**：使用google/nano-banana模型，prompt需包含角色与场景风格

- **YouTube**：通过GCP创建OAuth凭证，Shorts需选assignable=true类别（如ID24娱乐类）

⚠️ **常见问题解决**

- **Shorts上传失败**：因ID42不可直接分配，需选替代类别+竖屏9:16+时长≤60秒

- **生图超时**：添加Wait节点（建议5分钟）+HTTP查询节点轮询状态

- **格式错误**：AI Agent节点必须打开Require Specific Output Format开关

🎯 **内容洞察**

- **效率提升**：全流程自动化可将短视频制作周期从小时级压缩至分钟级

- **扩展性**：支持通过飞书/Google Sheet批量导入主题，实现规模化生产

- **成本控制**：免费API组合（DeepSeek基础版+KIE免费额度）可降低创作成本