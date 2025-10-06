from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import get_db
from .. import models, schemas
from ..deps import get_current_claims
from ..rbac import enforce_role

router = APIRouter(prefix="/messages", tags=["messages"])

@router.post("")
def post_message(body: schemas.MessageCreate, claims=Depends(get_current_claims), db: Session = Depends(get_db)):
    ch = db.query(models.Channel).filter(models.Channel.id == body.channel_id).first()
    if not ch: raise HTTPException(404, "Channel not found")
    enforce_role(claims, str(ch.workspace_id), {"owner","admin","member"})
    m = models.Message(channel_id=ch.id, sender_id=claims["sub"], ciphertext=body.ciphertext)
    db.add(m); db.commit(); db.refresh(m)
    return {"id": str(m.id), "created_at": m.created_at.isoformat()}

@router.get("/{channel_id}")
def list_messages(channel_id: str, claims=Depends(get_current_claims), db: Session = Depends(get_db)):
    ch = db.query(models.Channel).filter(models.Channel.id == channel_id).first()
    if not ch: raise HTTPException(404, "Channel not found")
    enforce_role(claims, str(ch.workspace_id), {"owner","admin","member","guest"})
    msgs = db.query(models.Message).filter(models.Message.channel_id == ch.id).order_by(models.Message.created_at.asc()).all()
    return [{"id": str(x.id), "ciphertext": x.ciphertext, "sender_id": str(x.sender_id), "created_at": x.created_at.isoformat()} for x in msgs]
