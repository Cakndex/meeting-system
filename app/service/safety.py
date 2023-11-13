"""安全校验相关函数
"""

import hashlib
import random
import re

from redis.exceptions import RedisError

from app.constants import Error
from app.database.db import redis_db
from app.models.request import RegisterInRequest

FIELD_RULES = {

    'username': {
        # 规则：最大长度64，最小长度1，只能包含中文、英文、数字、emoji
        'pattern': r'^[\u4e00-\u9fff\u1F601-\u1F64Fa-zA-Z0-9]{1,64}$',
        'error': Error.IllegalUsername,
    },
    'password': {
        # 规则：最大长度64，最小长度8
        'pattern': r'^.{8,64}$',
        'error': Error.IllegalPassword,
    },
    'telephone': {
        # 规则：最大长度11，最小长度11，必须为11位数字
        'pattern': r'^[0-9]{11}$',
        'error': Error.IllegalTelephone,
    },
}


def check_field(field, rules) -> Error:
    """按照上述规则进行检查"""
    if not re.match(rules['pattern'], field):
        return rules['error']
    return Error.NoError


def safety_check_userinfo(userinfo) -> Error:
    """"检测用户输入信息是否规范"""
    fields: set = set()
    # 根据不同的用户信息类型，检测不同的字段
    if isinstance(userinfo, RegisterInRequest):
        fields = {"password", "username", "telephone"}
    return safety_check({field: getattr(userinfo, field) for field in fields})


def safety_check(userinfo: dict) -> Error:
    """检测用户输入信息是否规范"""
    for field, value in userinfo.items():
        rules = FIELD_RULES.get(field)
        err = check_field(value, rules)
        if err != Error.NoError:
            return err
    return Error.NoError


def len_check(ma, mi, value) -> bool:
    """检查字符串长度是否在范围内"""
    if len(value) >= ma or len(value) < mi:
        return False
    return True


def encode_password(password: str) -> str:
    """将密码加密"""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


class AdminCode:
    """邀请码类"""
    PREFIX = 'admin_code'
    VALUE = 'unused'

    def generate_code(self):
        """生成邀请码"""
        while True:
            try:
                code = str(random.randint(10000000, 99999999))
                try:
                    if redis_db.get(self.PREFIX + code) == self.VALUE:
                        continue
                except RedisError:
                    return "", Error.CodeReadError

                redis_db.set(self.PREFIX + code, self.VALUE)
                break
            except RedisError:
                return "", Error.CodeWriteError
        return code, Error.NoError

    def check_code(self, code):
        """检查邀请码是否正确"""
        try:
            if redis_db.get(self.PREFIX + code) == self.VALUE:
                return Error.NoError
        except RedisError:
            return Error.CodeError
        return Error.CodeReadError

    def delete_code(self, code):
        """删除邀请码"""
        redis_db.delete(self.PREFIX + code)
        return Error.NoError


admin_code = AdminCode()
