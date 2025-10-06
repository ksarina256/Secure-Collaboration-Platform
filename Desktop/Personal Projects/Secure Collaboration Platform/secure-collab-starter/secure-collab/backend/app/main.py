from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .db import Base, engine
from . import models
from .routers import users, messages

# Create tables on startup (simple dev path; replace with migrations in prod)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Secure Collaboration Platform")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten for prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(messages.router)

@app.get("/healthz")
def health():
    return {"ok": True}
