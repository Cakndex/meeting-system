"""
对表user的操作
"""
from typing import Union

from app.database.db import SessionLocal
from app.database.db_models import User


def find_by_username(user: str) -> Union[User, None]:
    """根据用户名获取用户"""
    with SessionLocal() as sess:
        return sess.query(User).filter_by(username=user).first()


def find_by_phone(phone: str) -> Union[User, None]:
    """根据邮箱获取用户"""
    with SessionLocal() as sess:
        return sess.query(User).filter_by(telephone=phone).first()


def find_by_userid(user_id: int) -> Union[User, None]:
    """根据用户id获取用户"""
    with SessionLocal() as sess:
        return sess.query(User).filter_by(userId=user_id).first()


def find_user_all() -> Union[list[User], None]:
    """获取所有用户"""
    with SessionLocal() as sess:
        return sess.query(User).all()


def find_user_group(userGroup: int) -> Union[list[User], None]:
    """根据用户组获取用户"""
    with SessionLocal() as sess:
        return sess.query(User).filter_by(userGroup=userGroup).all()
