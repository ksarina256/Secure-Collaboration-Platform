# Secure Collaboration Platform (MVP)

React + FastAPI + PostgreSQL + JWT + RBAC + client-side E2EE (ciphertext-only server).

## Quick start (Docker Compose)

```bash
docker compose up --build
# API: http://localhost:8000/docs
# Web: http://localhost:5173
```

### Test flow
1) Open the web app and register or login.
2) The backend returns a JWT; it will be attached to API calls.
3) Messages API stores ciphertext only (E2EE happens on the client via libsodium).

## Services
- **db**: Postgres 16
- **api**: FastAPI app (port 8000)
- **web**: React app (Nginx static) (port 5173)

## Environment
See `.env.example` for hints. Compose injects sensible defaults for local dev.

## Dev notes
- Tables auto-create on API start (see `app/main.py`). Use migrations for production.
- Replace JWT secrets and tighten CORS for production.
- Add AV scan + presigned URLs for file uploads in the next iteration.
