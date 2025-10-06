# Secure Collaboration Platform

**React + FastAPI + PostgreSQL** — secure file sharing & messaging with **JWT authentication**, **role-based access control (RBAC)**, and **client-side end-to-end encryption (E2EE)**.  
Dockerized for local dev and CI/CD-ready.

> Server stores **ciphertext only** for messages (and, in the next iteration, files). Clients encrypt/decrypt with libsodium.

## Features
- Workspaces, channels (scaffolded; extend easily)
- Auth: email+password → short-lived JWT
- RBAC: owner/admin/member/guest (enforced by middleware)
- Messaging API stores ciphertext only
- React frontend with libsodium helpers for E2EE
- Docker Compose (Postgres + API + Web)
- GitHub Actions workflow (image build; optional push to GHCR)

## Architecture
- **Frontend**: React + Vite + TypeScript, libsodium-wrappers
- **Backend**: FastAPI (Python), SQLAlchemy, JWT
- **DB**: PostgreSQL
- **Containers**: Docker / Compose
