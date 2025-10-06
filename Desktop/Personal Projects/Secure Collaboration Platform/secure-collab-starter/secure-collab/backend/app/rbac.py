from fastapi import HTTPException, status

def enforce_role(claims, workspace_id: str, allowed: set[str]):
    roles = claims.get("roles", {})
    role = roles.get(workspace_id)
    if role not in allowed:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient role")
