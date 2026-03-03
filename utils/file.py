from fastapi import UploadFile

from configs.file_upload import MAX_FILE_UPLOAD_SIZE
from utils.error import AppException, ErrorCode, ERROR_MESSAGES


def check_upload_file_size(file:UploadFile):
    if file.size and file.size > MAX_FILE_UPLOAD_SIZE:
        raise AppException(
            status_code=413,
            code=ErrorCode.FILE_SIZE_EXCEEDED,
            message=ERROR_MESSAGES[ErrorCode.FILE_SIZE_EXCEEDED],
    )

