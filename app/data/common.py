"""
通用增删改查
"""
from app.database.db import SessionLocal


def update(item):
    """更新数据库"""
    with SessionLocal() as sess:
        merged_item = sess.merge(item)
        sess.commit()
        sess.refresh(merged_item)


def add(item):
    """添加到数据库"""
    with SessionLocal() as sess:
        sess.add(item)
        sess.commit()
        sess.refresh(item)
    return item


def remove_single(item):
    """从数据库中删除"""
    with SessionLocal() as sess:
        sess.delete(item)
        sess.commit()
