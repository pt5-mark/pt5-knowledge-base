# PT5 Knowledge Base

Personal knowledge base for PT5 Global, synchronized across OpenClaw instances via Git.

## Structure

```
/01_AI技术与编程/     - AI & Programming
/02_跨境电商与独立站/  - E-commerce
/03_社媒运营与营销/    - Social Media
/04_广告与投放/       - Advertising
/05_内容创作/         - Content Creation
/06_效率工具/         - Productivity Tools
/07_生活服务/         - Life Services
/08_其他/            - Miscellaneous
/tools/              - Scripts & utilities
```

## Git Workflow

- Auto-sync runs every hour
- Commit message: "Auto-sync: YYYY-MM-DD HH:MM:SS"
- Remote: https://github.com/pt5-mark/pt5-knowledge-base

## Security

- Secrets stored in gopass, never committed
- SSH key: `ssh/openclaw_ed25519`
- GitHub token: `github/token_pt5_kb`

## Multi-Agent Setup

Other OpenClaw instances can sync:
```bash
git clone https://github.com/pt5-mark/pt5-knowledge-base.git
cd pt5-knowledge-base
git remote set-url origin https://<TOKEN>@github.com/pt5-mark/pt5-knowledge-base.git
```
