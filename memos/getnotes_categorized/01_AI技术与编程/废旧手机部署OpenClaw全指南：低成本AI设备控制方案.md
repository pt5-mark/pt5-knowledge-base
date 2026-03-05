---
title: 废旧手机部署OpenClaw全指南：低成本AI设备控制方案
created: 2026-02-11 06:21:45
tags: ["AI链接笔记", "OpenClaw部署", "废旧手机利用", "Termux教程"]
source: https://mp.weixin.qq.com/s/aBuJ1vkybpq5qxmyeJaxCQ
---

# 废旧手机部署OpenClaw全指南：低成本AI设备控制方案

# 废旧手机部署OpenClaw全指南：低成本AI设备控制方案
创建于：2026-02-11 06:21:45

标签：
            
            
            AI链接笔记
OpenClaw部署
废旧手机利用
Termux教程

原文：[旧手机别换不锈钢脸盆了！装上OpenClaw，瞬间变身AI机器人](https://mp.weixin.qq.com/s/aBuJ1vkybpq5qxmyeJaxCQ)

### **📱 项目背景与价值**
**核心目标**：利用Termux在废旧手机上部署OpenClaw（类AI Agent工具），实现通过自然语言控制手机硬件功能，将闲置设备转化为**低功耗微型服务器**。

**关键价值**：无需专业服务器，零成本实现AI与硬件交互，拓展物联网应用场景。

### **🔧 安装步骤详解**
**(一) 基础环境准备**

**Termux安装**

需下载两个APK：com.termux.api_1002.apk和com.termux_1022.apk

下载地址：夸克云盘（[https://pan.quark.cn/s/8fab168783aa）](https://pan.quark.cn/s/8fab168783aa）)

- 安装后生成两个图标：Termux（Linux环境）和Termux:API（硬件交互接口）

**依赖软件配置**

| 软件/命令 | 作用 | 关键操作 |
|———-|——|———-|
| termux-setup-storage | 配置存储访问权限 | 需在手机弹窗中允许权限 |
| termux-change-repo | 切换软件源仓库 | 优化下载速度 |
| ssh | 远程控制功能 | 实现电脑端操作手机 |
| nodejs | 运行环境 | OpenClaw依赖的运行时 |
| termux-torch | 手电筒控制工具 | 提供硬件控制命令 |
| termux-api | 系统接口代理 | 连接Termux与手机硬件 |

**OpenClaw安装**

核心命令：npm install -g openclaw --verbose --no-optional

- 参数说明：--verbose（输出详细日志）、--no-optional（跳过可选依赖）

**(二) 启动与访问流程**

**服务启动顺序**

mermaid
graph LR
A[启动Termux:API] --> B[启动Termux]
B --> C[启动SSH服务:sshd]
C --> D[启动OpenClaw:openclaw gateway]

2. **远程访问配置**

- 电脑SSH连接：ssh -p 8022 192.168.0.100（需替换手机局域网IP）

- 端口代理命令：ssh -L 18789:127.0.0.1:18789 -p 8022 192.168.0.100

- Web访问地址：http://localhost:18789/chat?session=main
### **🎯 功能测试与验证**
#### **(一) 手电筒控制示例**
1. **核心原理**：通过OpenClaw执行系统命令

- 打开手电筒：termux-torch on

- 关闭手电筒：termux-torch off

2. **测试流程**

- 在Web界面发送指令：”打开手电筒，10秒后关闭”

- OpenClaw自动生成执行序列：

bash
 termux-torch on  # 执行成功
 sleep 10         # 等待10秒
 termux-torch off # 执行成功

**(二) 系统日志验证**

OpenClaw启动日志显示监听端口：ws://127.0.0.1:18789

模型信息：agent model: qwen-portal/coder-model

- 设备交互记录：Browser control service ready (profiles=2)

### **💡 扩展应用与技术洞察**
**(一) 潜在硬件控制场景**

**摄像头**：通过termux-camera-photo命令调用相机拍照

**录音机**：使用termux-microphone-record录制音频

**通知管理**：通过termux-notification发送系统通知

**(二) 技术局限性**

**网络限制**：默认仅本地访问，需端口映射实现公网访问

**性能瓶颈**：老旧手机CPU可能无法支持复杂AI模型运行

**权限问题**：部分硬件功能需Android系统Root权限

### **📝 补充细节**

**Termux本质**：手机上的轻量级Linux环境，可类比”移动Docker”

**OpenClaw版本**：测试使用2026.2.6-3版本，支持OpenAI兼容接口

- **社区资源**：作者提供视频教程及QQ交流群（749827914）获取技术支持