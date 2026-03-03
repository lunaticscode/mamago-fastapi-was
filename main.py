from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from starlette.middleware.gzip import GZipMiddleware
from starlette.responses import JSONResponse

from libs.openrouter import init as openrouter_ai_init
from middlewares.logger import LoggerMiddleware
from routes.index import api_router
from libs.translate import load_whisper
from utils.error import AppException, ErrorCode, ERROR_MESSAGES


@asynccontextmanager
async def lifespan(_app: FastAPI):
    openrouter_ai_init()
    load_whisper()
    print("startup")
    yield
    print("cleanup")


app = FastAPI(lifespan=lifespan)

app.add_middleware(LoggerMiddleware)
app.include_router(api_router, prefix="/api")
app.add_middleware(GZipMiddleware, minimum_size=1000)

# AppException 처리
@app.exception_handler(AppException)
async def app_exception_handler(_request: Request, err: AppException):
    return JSONResponse(
        status_code=err.status_code,
        content={"error": {"code": err.code, "message": err.message}},
    )


# 기타 예외 → 500
@app.exception_handler(Exception)
async def global_exception_handler(_request: Request, _exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "error": {
                "code": ErrorCode.UNKNOWN_ERROR,
                "message": ERROR_MESSAGES[ErrorCode.UNKNOWN_ERROR],
            }
        },
    )