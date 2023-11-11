"""数据库实例化
"""

from app.constants import WAITING
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime

from app.database.db import Base


class User(Base):
    __tablename__ = 'users'

    userId = Column(Integer, primary_key=True, autoincrement=True, index=True)
    # user might log in via either username or email
    username = Column(String(64), unique=True, index=True, nullable=False)
    password = Column(String(64), nullable=False)  # sha256 hashed password
    admin = Column(Boolean, nullable=False, default=False)  # is admin
    banned = Column(Boolean, nullable=False, default=False)  # is banned
    telephone = Column(String(16), nullable=False)


class Meeting(Base):
    __tablename__ = 'meetings'

    meetingId = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(64), nullable=False)
    address = Column(String(256), nullable=False)
    # 设施，如投影仪，白板，麦克风等
    facility = Column(String(256), nullable=False)


class IsCaptured(Base):
    __tablename__ = 'is_captured'

    CapturedId = Column(Integer, primary_key=True, autoincrement=True, index=True)
    userId = Column(Integer, nullable=False, index=True)
    meetingId = Column(Integer, nullable=False, index=True)
    StartTime = Column(DateTime, nullable=False)
    EndTime = Column(DateTime, nullable=False)
    # 参会人员
    participants = Column(Text(), nullable=False)
    # 人数
    number = Column(Integer, nullable=False)
    # 审核
    isPass = Column(Integer, nullable=False, default=WAITING)
    reason = Column(String(256), nullable=False, default=" ")
    # 简介
    summary = Column(Text(), nullable=False)
