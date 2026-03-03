from fastapi import APIRouter, UploadFile, File
from shared.consts.router_name import ChatRouterName
from controllers.chat import get_chat_histories as ctrl_get_chat_histories
from controllers.chat import summarize_chat as ctrl_summarize_chat
chat_router = APIRouter()

@chat_router.get("/", name=ChatRouterName.GET_CHAT_HISTORIES, tags=["chat"])
async def get_chat_histories():
    return ctrl_get_chat_histories()


@chat_router.post("/summary", name=ChatRouterName.SUMMARIZE_CHAT)
async def summarize_chat(file: UploadFile = File(...)):
    return await ctrl_summarize_chat(file)


