from fastapi import Body, APIRouter, Response, HTTPException
from redis.exceptions import RedisError

from app.constants import Error
from app.data import common as common_data
from app.data import user as user_data
from app.database.db import redis_db
from app.database.db_models import User
from app.depends import AuthedUser
from app.models.request import RegisterInRequest, ChangePasswordRequest, LoginRequest, \
    UserToggleRequest
from app.models.response import TokenResponse, AdminCodeResponse, UsersResponse, UserInfoResponse
from app.service import safety as safety_utils
from app.service import status
from app.service import token as auth_utils
from app.service import user as user_utils

# 认证模块
userRouter = APIRouter(
    prefix="/user",
    tags=["user"],
)


@userRouter.post("/register", response_model=TokenResponse)
async def register(
        response: Response,
        *,
        register_body: RegisterInRequest = Body()
):
    """注册账号"""
    state = user_utils.check_if_exist(register_body) or safety_utils.safety_check_userinfo(register_body)

    if state != Error.NoError:
        return status.return_response(TokenResponse(status=state), response)

    if register_body.isAdmin:
        if register_body.code is None:
            return status.return_response(TokenResponse(status=Error.RegisterCodeError), response)
        err = safety_utils.admin_code.check_code(register_body.code)
        if err != Error.NoError:
            return status.return_response(TokenResponse(status=err), response)
        safety_utils.admin_code.delete_code(register_body.code)

    # 更新数据库

    new_user = user_utils.add_user(register_body)
    # 生成token
    try:
        access_token = auth_utils.create_access_token(new_user)
    except Exception:
        return status.return_response(TokenResponse(status=Error.TokenError), response)

    try:
        pipe = redis_db.pipeline()
        pipe.set(new_user.username, access_token)
        pipe.execute()
    except RedisError:
        return status.return_response(TokenResponse(status=Error.TokenError), response)

    token_out = user_utils.package_token_out(new_user, access_token)
    return status.return_response(token_out, response)


@userRouter.post("/login", response_model=TokenResponse)
async def login(
        response: Response,
        *,
        login_body: LoginRequest = Body()
):
    """登录账号"""
    password = safety_utils.encode_password(login_body.password)
    user = user_data.find_by_username(login_body.username)

    # 登录判定
    if user is None:
        return status.return_response(TokenResponse(status=Error.UserNotFound), response)
    if user.password != password:
        return status.return_response(TokenResponse(status=Error.PasswordError), response)
    if user.banned:
        return status.return_response(TokenResponse(status=Error.UserBanned), response)

    # 生成token
    try:
        access_token = auth_utils.create_access_token(user)
    except Exception:
        return status.return_response(TokenResponse(status=Error.TokenError), response)

    try:
        pipe = redis_db.pipeline()
        pipe.set(user.username, access_token)
        pipe.execute()
    except RedisError:
        return status.return_response(TokenResponse(status=Error.TokenError), response)

    token_out = user_utils.package_token_out(user, access_token)

    return status.return_response(token_out, response)


@userRouter.post("/changePassword", dependencies=[AuthedUser(admin=True)])
async def change_password(
        response: Response,
        *,
        change_password_body: ChangePasswordRequest = Body()
):
    """只有管理员可以修改密码"""

    password = safety_utils.encode_password(change_password_body.NewPassword)

    # 更新数据库
    user = user_data.find_by_userid(change_password_body.userId)
    if user is None:
        return status.return_status(Error.UserNotFound, response)
    user.password = password
    common_data.update(user)
    try:
        pipe = redis_db.pipeline()
        pipe.delete(user.username)
        pipe.execute()
    except RedisError:
        return status.return_response(TokenResponse(status=Error.TokenError), response)
    return status.return_status(Error.NoError, response)


@userRouter.post("/banned", dependencies=[AuthedUser(admin=True)])
async def remove_user_by_admin(
        response: Response,
        *,
        userToggle: UserToggleRequest = Body()
):
    """管理员封禁用户"""
    remove_user = user_data.find_by_userid(userToggle.userId)
    if remove_user.admin is True:
        return status.return_status(Error.BanAdmin, response)
    remove_user.banned = userToggle.value
    common_data.update(remove_user)
    return status.return_status(Error.NoError, response)


@userRouter.get("/logout")
async def logout(
        response: Response,
        *,
        user: User = AuthedUser()
):
    """登出"""
    user = user_data.find_by_userid(user.userId)
    try:
        pipe = redis_db.pipeline()
        pipe.delete(user.username)
        pipe.execute()
    except RedisError:
        raise HTTPException(status_code=500, detail="Redis error.")

    return status.return_status(Error.NoError, response)


@userRouter.get("/inviteCode", response_model=AdminCodeResponse, dependencies=[AuthedUser(admin=True)])
async def generate_invite_code(
        response: Response,
):
    """管理员生成管理员码"""
    code = safety_utils.admin_code.generate_code()
    return status.return_response(AdminCodeResponse(
        status=code[1],
        inviteCode=code[0]
    ), response)


@userRouter.get("/all", response_model=UsersResponse, dependencies=[AuthedUser(admin=True)])
async def user_get(
        response: Response,
):
    """获取所有用户信息"""
    users = user_data.find_user_all()

    # 封装返回的用户信息
    users_out = user_utils.package_users_out(users)
    return status.return_response(UsersResponse(list=users_out, status=Error.NoError), response)


@userRouter.get("/info", response_model=UserInfoResponse)
async def user_info(
        response: Response,
        *,
        user: User = AuthedUser()
):
    """获取用户信息"""
    user = user_data.find_by_userid(user.userId)
    return status.return_response(user_utils.package_user_info_out(user), response)