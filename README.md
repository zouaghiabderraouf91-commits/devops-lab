# DevOps Lab — Production Stack

بنية تحتية كاملة تعمل على Docker

## المكونات
- **Nginx** — Reverse Proxy + SSL/TLS
- **Gunicorn + Flask** — Application Server
- **UFW + Fail2Ban** — Security Layer

## التشغيل
```bash
docker compose up -d
```

## الخدمات
| الخدمة | المنفذ |
|--------|--------|
| HTTPS  | 443    |
| HTTP (redirect) | 80 |
