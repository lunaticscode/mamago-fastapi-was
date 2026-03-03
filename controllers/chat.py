from fastapi import UploadFile
# from starlette.responses import StreamingResponse
from services.chat import get_summary_result
from utils.file import check_upload_file_size

DUMMY_CHAT_HISTORIES = [
    {"title": "chat-history-1", "id": "chat-history-1"},
    {"title": "chat-history-2", "id": "chat-history-2"}
]

def get_chat_histories():
    return DUMMY_CHAT_HISTORIES

def summarize_chat(file: UploadFile):
    check_upload_file_size(file)
    result = get_summary_result(file)
    return result

    # SSE streaming 방식
    # openrouter.ai streaming 한도가 넘어서 사용 불가.
    # stream = get_summary_result(file)
    # def event_stream():
    #     for chunk in stream:
    #         yield f"data: {chunk}\n\n"
    #     yield "data: [DONE]\n\n"
    # return StreamingResponse(event_stream(), media_type="text/event-stream")
