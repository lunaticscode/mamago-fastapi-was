from fastapi import UploadFile

DUMMY_CHAT_HISTORIES = [
    {"title": "chat-history-1", "id": "chat-history-1"},
    {"title": "chat-history-2", "id": "chat-history-2"}
]


def get_chat_histories():
    return DUMMY_CHAT_HISTORIES

def summarize_chat_(file: UploadFile):
    print(file)
    return
