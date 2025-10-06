from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import get_db
from .. import models, schemas, auth

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/register")
def register(data: schemas.UserCreate, db: Session = Depends(get_db)):
    if db.query(models.User).filter(models.User.email == data.email).first():
        raise HTTPException(400, "Email exists")
    u = models.User(email=data.email, password_hash=auth.hash_pw(data.password))
    db.add(u); db.commit(); db.refresh(u)
    token = auth.issue_access_token(str(u.id), u.email, {})
    return {"user_id": str(u.id), "token": token}

@router.post("/login", response_model=schemas.Token)
def login(data: schemas.Login, db: Session = Depends(get_db)):
    u = db.query(models.User).filter(models.User.email == data.email).first()
    if not u or not auth.verify_pw(data.password, u.password_hash or ""):
        raise HTTPException(401, "Invalid credentials")
    mems = db.execute(
        "SELECT workspace_id, role FROM memberships WHERE user_id = :uid",
        {"uid": str(u.id)}
    ).fetchall()
    roles = {str(row[0]): row[1] for row in mems}
    return {"access_token": auth.issue_access_token(str(u.id), u.email, roles)}
