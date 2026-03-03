from enum import Enum

DEFAULT_ERROR_MESSAGE = "알 수 없는 오류 발생"

class ErrorCode(str, Enum):
    UNKNOWN_ERROR = "UNKNOWN_ERROR"

ERROR_MESSAGES = {
    ErrorCode.UNKNOWN_ERROR: DEFAULT_ERROR_MESSAGE,
}

class AppException(Exception):
    def __init__(
            self,
            status_code:int = 500,
            code: str = ErrorCode.UNKNOWN_ERROR,
            message: str | None = None
    ):
        self.status_code = status_code
        self.code = code
        self.message = message or DEFAULT_ERROR_MESSAGE