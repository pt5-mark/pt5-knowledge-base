# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

### OpenClaw 访问方式

**方式1：SSH 隧道（安全，推荐日常使用）**
```bash
# 建立隧道
ssh -L 18789:127.0.0.1:18789 root@76.13.176.222

# 后台保持
ssh -fNL 18789:127.0.0.1:18789 root@76.13.176.222

# 自动重连
autossh -M 0 -N -L 18789:127.0.0.1:18789 root@76.13.176.222
```
访问地址：`http://localhost:18789/?token=mySecretToken123`

**方式2：域名 + HTTPS（方便，已配置 Caddy）**
```
https://chinapt5.cloud
```
- 用户名：`openclaw`
- 密码：`openclaw123`

**VPS 信息**
- IP: `76.13.176.222`
- 本地端口: `18789`

---

Add whatever helps you do your job. This is your cheat sheet.
