"""依赖项
"""
from fastapi import Request, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.database.db import redis_db
from app.database.db_models import User
from app.service.token import get_user


class JWTBearer(HTTPBearer):
    """"JWT鉴权"""
    admin: bool

    def __init__(self, auto_error: bool = True, admin: bool = False):
        super(JWTBearer, self).__init__(auto_error=auto_error)
        self.admin = admin

    async def __call__(self, request: Request) -> User:
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=401, detail="Invalid authentication scheme.")
            try:
                user = get_user(credentials.credentials)
                token = redis_db.get(user.username)
                if token is None or token != credentials.credentials:
                    raise HTTPException(status_code=403, detail="Device changed.")
                if user is None:
                    raise HTTPException(status_code=401, detail="Authorized user not found.")
                if self.admin and not user.admin:
                    raise HTTPException(status_code=401, detail="Unauthorized")
                if user.banned:
                    raise HTTPException(status_code=403, detail="User been banned.")
                return user
            except ValueError:
                raise HTTPException(status_code=401, detail="Invalid token.")
            except TimeoutError:
                raise HTTPException(status_code=403, detail="Expired token.")
        else:
            raise HTTPException(status_code=401, detail="Please login")


def AuthedUser(admin: bool = False) -> User:
    """判断是否需要管理员权限"""
    return Depends(JWTBearer(admin=admin))
