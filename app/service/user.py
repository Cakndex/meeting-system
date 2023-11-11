"""用户相关处理函数
"""

from typing import Union, Any

from app.constants import Error
from app.data import common as common_data
from app.data import user as user_data
from app.database.db_models import User
from app.models.request import RegisterInRequest
from app.models.response import TokenResponse, UserInfoResponse
from app.models.schema import UserInfo
from app.service import safety as safety_utils


def add_user(register_body: RegisterInRequest) -> Any:
    user_register = User(username=register_body.username,
                         password=safety_utils.encode_password(register_body.password),
                         admin=register_body.isAdmin,
                         telephone=register_body.telephone
                         )
    return common_data.add(user_register)


def check_if_exist(register: RegisterInRequest) -> Union[Error, None]:
    """检查注册的用户是否存在"""
    user_exists = user_data.find_by_username(register.username) is not None
    telephone_exists = user_data.find_by_phone(register.telephone) is not None

    if any([user_exists, telephone_exists]):
        if user_exists:
            return Error.UserAlreadyExists
        elif telephone_exists:
            return Error.TelephoneAlreadyExists
    else:
        return Error.NoError


def package_token_out(user: User, access_token: str) -> TokenResponse:
    return TokenResponse(access=access_token,
                         userId=user.userId,
                         username=user.username,
                         telephone=user.telephone,
                         admin=user.admin,
                         status=Error.NoError)


def package_users_out(users: list[User]) -> list[UserInfo]:
    """将用户列表封装成UserOut列表"""
    users_out = []
    for user in users:
        usr_out = UserInfo(
            username=user.username,
            userId=user.userId,
            telephone=user.telephone,
            admin=user.admin,
            banned=user.banned,
        )
        users_out.append(usr_out)

    return users_out


def package_user_info_out(user: User) -> UserInfoResponse:
    return UserInfoResponse(
        username=user.username,
        userId=user.userId,
        telephone=user.telephone,
        admin=user.admin,
        banned=user.banned,
        status=Error.NoError
    )
