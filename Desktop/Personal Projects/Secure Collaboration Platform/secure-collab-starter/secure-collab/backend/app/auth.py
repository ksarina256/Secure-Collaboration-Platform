import os, datetime, jwt
from passlib.hash import bcrypt

JWT_SECRET = os.getenv("JWT_SECRET", "dev_secret_change_me")
JWT_AUD = "collab"
JWT_ISS = "secure-collab"
ACCESS_TTL_MIN = int(os.getenv("ACCESS_TTL_MIN", "15"))

def hash_pw(p:str)->str: return bcrypt.hash(p)
def verify_pw(p:str, h:str)->bool: return bcrypt.verify(p, h)

def issue_access_token(user_id:str, email:str, workspace_roles:dict[str,str]):
    now = datetime.datetime.utcnow()
    payload = {
        "sub": user_id,
        "email": email,
        "roles": workspace_roles,  # {workspace_id: role}
        "aud": JWT_AUD,
        "iss": JWT_ISS,
        "iat": now,
        "exp": now + datetime.timedelta(minutes=ACCESS_TTL_MIN),
    }
    return jwt.encode(payload, JWT_SECRET, algorithm="HS256")
