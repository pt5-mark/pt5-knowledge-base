---
title: 使用n8n自动化Reddit帖子监控与Notion同步工作流 🚀
created: 2025-11-11 19:08:13
tags: ["AI链接笔记", "n8n自动化", "Reddit监控", "Notion同步"]
source: https://mp.weixin.qq.com/s/IXG2bQIcXsyRwM3WVtfY0w
---

# 使用n8n自动化Reddit帖子监控与Notion同步工作流 🚀

# 使用n8n自动化Reddit帖子监控与Notion同步工作流 🚀
创建于：2025-11-11 19:08:13

标签：
            
            
            AI链接笔记
n8n自动化
Reddit监控
Notion同步

原文：[定期獲取reddit帖子內容並同步到notion | n8n自動化流程](https://mp.weixin.qq.com/s/IXG2bQIcXsyRwM3WVtfY0w)

### 需求背景

- 痛点：手动搜索Reddit产品信息时效性差，易遗漏关键内容

- 目标：构建自动化流程实现关键词帖子监控、筛选、内容提取与Notion同步

### 技术架构
📊 **核心工作流节点**（共11步）
1. **定时触发**

   - 使用Schedule Trigger节点设置每日23:00自动执行
2. **搜索帖子**

   - 配置Reddit节点：搜索关键词”n8n”，返回限制100条结果
   - 需通过Reddit OAuth2认证（Client ID + Client Secret）
3. **筛选条件**（If节点三规则）

   - selftext字段非空（排除无内容帖子）
   - 发布时间在当天0点后（{{ DateTime.fromSeconds($json.created).toISO() }} is after {{ $today.minus({days: 7}).toISO() }}）
   - 点赞数(ups) > 10
4. **循环处理**

   - Loop Over Items节点遍历筛选后的帖子列表

### 数据处理流程
🔄 **多线程并行处理**
- **内容提取**：Set节点提取selftext字段 → 命名为content变量
- **链接提取**：Set节点提取url字段 → 命名为url变量
- **评论处理**：

  1. Reddit节点获取Post Comment（需Subreddit+Post ID参数）

  2. Set节点提取body字段 → 命名为comment变量

  3. Code节点合并多条评论（JS代码：添加序号并换行拼接）

javascript
     const comments = items.map(item => item.json.comment);
     const mergedText = comments.map((c, i) => `${i+1}. ${c}`).join('\n');
     return [{ json: { mergedText } }];

### 数据整合与存储
📥 **最终数据流向**
1. Merge节点合并content+url → 生成基础信息集
2. 二次Merge节点整合基础信息+mergedText → 完整数据记录
3. Notion节点同步至Database

   - 字段映射：内容→content、链接→url、评论→mergedText

   - 同步效果：单条记录包含完整帖子信息（示例显示11条符合条件结果）

### 关键配置要点
⚠️ **Reddit应用创建步骤**
1. 访问[https://www.reddit.com/prefs/apps创建Script类型应用](https://www.reddit.com/prefs/apps创建Script类型应用)
2. 填写Redirect URI（取自n8n OAuth配置页）
3. 获取Client ID与Client Secret并填入n8n凭证管理