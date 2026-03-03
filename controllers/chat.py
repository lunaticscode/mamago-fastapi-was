from fastapi import UploadFile
from services.chat import get_summary_result
from utils.file import check_upload_file_size

DUMMY_CHAT_HISTORIES = [
    {"title": "chat-history-1", "id": "chat-history-1"},
    {"title": "chat-history-2", "id": "chat-history-2"}
]

def get_chat_histories():
    return DUMMY_CHAT_HISTORIES

async def summarize_chat(file: UploadFile):
    check_upload_file_size(file)
    result = await get_summary_result(file)
    return result
