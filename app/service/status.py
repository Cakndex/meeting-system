"""返回状态处理
"""

from fastapi import status, Response

from app.constants import Error
from app.models.response import Status

HTTP_432_ERROR = 432


# OK状态
def status_ok():
    return Status(status=Error.NoError)


# Error状态
def status_error(state: Error):
    return Status(status=state)


def return_status(state: Error = Error.NoError, status_response: Response = status.HTTP_200_OK):
    """返回状态码"""
    if state != Error.NoError:
        status_response.status_code = HTTP_432_ERROR
        return status_error(state)
    else:
        return status_ok()


def return_response(json_response, status_response: Response = status.HTTP_200_OK):
    """返回响应"""
    if json_response.status != Error.NoError:
        status_response.status_code = HTTP_432_ERROR
        return json_response
    return json_response
