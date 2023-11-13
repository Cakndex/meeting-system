from fastapi import Body, APIRouter, Response, Path
from app.constants import Error
from app.database.db import SessionLocal
from app.database.db_models import Meeting, IsCaptured, User
from app.depends import AuthedUser
from app.models.request import MeetingAddRequest, CheckRequest
from app.data import common as common_data
from app.models.response import CheckResponse
from app.models.schema import CheckInfo
from app.service.status import return_status, return_response

meetRouter = APIRouter(
    prefix="/meeting",
    tags=["meeting"],
)


@meetRouter.post("/add", dependencies=[AuthedUser(admin=True)])
async def meeting_add(
        response: Response,
        *,
        meeting_body: MeetingAddRequest = Body()
):
    """添加会议室"""
    room = Meeting(
        name=meeting_body.name,
        address=meeting_body.address,
        facility=",".join(meeting_body.facilities),
    )
    common_data.add(room)
    return return_status(Error.NoError, response)


@meetRouter.post("/change", dependencies=[AuthedUser(admin=True)])
async def meeting_change(
        response: Response,
        *,
        meeting_body: MeetingAddRequest = Body()
):
    """修改会议室"""
    with SessionLocal() as sess:
        room = sess.query(Meeting).filter_by(meetingId=meeting_body.id).first()
    if room is None:
        return return_status(Error.MeetingNotExist, response)
    room.name = meeting_body.name,
    room.address = meeting_body.address,
    room.capacity = ",".join(meeting_body.facilities),
    common_data.update(room)
    return return_status(Error.NoError, response)


@meetRouter.post("/delete/{{meetId}}", dependencies=[AuthedUser(admin=True)])
async def meeting_delete(
        response: Response,
        *,
        meetId: int = Path()
):
    """删除会议室"""
    with SessionLocal() as sess:
        room = sess.query(Meeting).filter_by(meetingId=meetId).first()
    if room is None:
        return return_status(Error.MeetingNotExist, response)
    common_data.remove_single(room)
    return return_status(Error.NoError, response)


@meetRouter.get("/list", dependencies=[AuthedUser(admin=True)])
async def meeting_list(
        response: Response,
):
    """获取会议室列表"""
    with SessionLocal() as sess:
        rooms = sess.query(Meeting).all()
    return rooms


@meetRouter.post("/check", dependencies=[AuthedUser(admin=True)])
async def meeting_check(
        response: Response,
        *,
        CheckBody: CheckRequest = Body()
):
    """审核会议室申请"""
    with SessionLocal() as sess:
        check = sess.query(IsCaptured).filter_by(CapturedId=CheckBody.CapturedId).first()
        if check is None:
            return return_status(Error.CheckNotExist, response)
        room = sess.query(Meeting).filter_by(meetingId=check.meetingId).first()
        if room is None:
            return return_status(Error.MeetingNotExist, response)

    check.isPassed = CheckBody.isCheck
    check.reason = CheckBody.reason
    common_data.update(check)
    return return_status(Error.NoError, response)


@meetRouter.get("/checklist", response_model=CheckResponse, dependencies=[AuthedUser(admin=True)])
async def meeting_checklist(
        response: Response
):
    """获取审核列表"""
    checkList = []
    with SessionLocal() as sess:
        checks = sess.query(IsCaptured). \
            join(User, User.userId == IsCaptured.userId). \
            join(Meeting, Meeting.meetingId == IsCaptured.meetingId). \
            all()
    if checks is None:
        return return_status(Error.CheckNotExist, response)
    for check in checks:
        check1 = CheckInfo(
            username=check.username,
            meetingName=check.name,
            meetingStartTime=check.StartTime,
            meetingEndTime=check.EndTime,
            meetingAddress=check.address,
            checkReason=check.reason,
            isPassed=check.isPass,
            number=check.number
        )
        checkList.append(check1)

    return return_response(CheckResponse(Checklist=checkList, status=Error.NoError), response)
