from fastapi import APIRouter
from routes.chat import chat_router

api_router = APIRouter()

api_router.include_router(chat_router, prefix="/chats")