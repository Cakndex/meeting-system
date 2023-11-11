"""
其他模型
"""

from __future__ import annotations

from pydantic import BaseModel


class UserInfo(BaseModel):
    userId: int = 0
    admin: bool = False
    banned: bool = False
    telephone: str = ""
    username: str = ""


class MeetingInfo(BaseModel):
    name: str
    address: str
    facilities: list[str]


class CheckInfo(BaseModel):
    username: str = ""
    meetingName: str = ""
    meetingStartTime: str = ""
    meetingEndTime: str = ""
    meetingAddress: str = ""
    checkReason: str = ""
    isPassed: int = -1
    number: int = 0
