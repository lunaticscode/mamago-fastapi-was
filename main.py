from contextlib import asynccontextmanager
from fastapi import FastAPI

from middlewares.logger import LoggerMiddleware
from routes.index import api_router
from libs.translate import load_whisper

@asynccontextmanager
async def lifespan(_app: FastAPI):
    load_whisper()
    print("startup")
    yield
    print("cleanup")


app = FastAPI(lifespan=lifespan)

app.add_middleware(LoggerMiddleware)
app.include_router(api_router, prefix="/api")
