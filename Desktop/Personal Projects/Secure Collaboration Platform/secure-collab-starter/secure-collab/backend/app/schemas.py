from pydantic import BaseModel, EmailStr
from enum import Enum

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class Login(BaseModel):
    email: EmailStr
    password: str

class MessageCreate(BaseModel):
    channel_id: str
    ciphertext: str  # JSON/base64 produced by client E2EE

class Role(str, Enum):
    owner="owner"; admin="admin"; member="member"; guest="guest"
