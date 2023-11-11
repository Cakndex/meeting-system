"""token相关处理函数
"""

from datetime import datetime, timedelta
from typing import TypedDict, Union

import jwt

from app.data import user as user_data
from app.database.db_models import User
from app.settings import settings


class JWTPayload(TypedDict):
    userId: int
    exp: int


def get_payload(token: str) -> JWTPayload:
    """获取token负载
    :raises ValueError: 如果是无效token
    :raises TimeoutError: 如果token已过期
    """
    try:
        return jwt.decode(token, settings.JWT_SECRET_KEY, settings.JWT_ALGORITHMS)
    except jwt.DecodeError:
        raise ValueError
    except jwt.ExpiredSignatureError:
        raise TimeoutError


def get_user(token: str) -> Union[User, None]:
    """获取token对应的用户，如无对应用户则返回 `None`
    :raises ValueError: 如果是无效token
    :raises TimeoutError: 如果token已过期
    """
    payload = get_payload(token)
    return user_data.find_by_userid(payload['userId'])


def create_access_token(user: Union[User, int], expire_delta: int = settings.ACCESS_TOKEN_EXPIRE_IN) -> str:
    """签发JWTToken

    :param user: 待签发用户
    :param expire_delta: 有效期，以分钟计
    :return token: 签发的 token
    """
    expire = datetime.utcnow() + timedelta(minutes=expire_delta)
    payload: JWTPayload = {
        'userId': user if isinstance(user, int) else user.userId,
        'exp': int(expire.timestamp())
    }
    return jwt.encode(payload, settings.JWT_SECRET_KEY, settings.JWT_ALGORITHMS)
