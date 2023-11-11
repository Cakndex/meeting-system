"""主函数
"""
import logging
import logging.handlers
from fastapi import FastAPI, Response
from starlette.middleware.cors import CORSMiddleware
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler


from app.api import user, meeting
from app.settings import limiter
from app.database.db import init_database

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有 HTTP 方法
    allow_headers=["*"],  # 允许所有 HTTP 头部
)
app.include_router(meeting.meetRouter)
app.include_router(user.userRouter)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


@app.on_event("startup")
async def startup():
    """startup event"""
    # 初始化日志
    logger = logging.getLogger("uvicorn.access")
    handler = logging.handlers.RotatingFileHandler("recruit.log", mode="a", maxBytes=1024 * 1024, backupCount=10)
    handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(handler)
    # 初始化数据库
    init_database()


@app.get('/ping')
def pong():
    """healthcheck"""
    return Response(content='pong')
