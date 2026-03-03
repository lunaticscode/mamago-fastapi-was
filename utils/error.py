import logging
from enum import Enum

logger = logging.getLogger(__name__)

DEFAULT_ERROR_MESSAGE = "알 수 없는 오류 발생"

class ErrorCode(str, Enum):
    UNKNOWN_ERROR = "UNKNOWN_ERROR"
    MODEL_FILE_ERROR = "MODEL_FILE_ERROR"
    MODEL_RUNTIME_ERROR = "MODEL_RUNTIME_ERROR"
    MODEL_LOAD_ERROR = "MODEL_LOAD_ERROR"

ERROR_MESSAGES = {
    ErrorCode.UNKNOWN_ERROR: DEFAULT_ERROR_MESSAGE,
    ErrorCode.MODEL_FILE_ERROR: "모델 파일 다운로드/경로 오류",
    ErrorCode.MODEL_RUNTIME_ERROR: "모델 로드 중 런타임 오류",
    ErrorCode.MODEL_LOAD_ERROR: "모델 로드 중 예상하지 못한 오류",
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
        logger.error(f"[{self.code}] {self.message}")