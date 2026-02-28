from contextlib import asynccontextmanager
from fastapi import FastAPI

from middlewares.logger import LoggerMiddleware


@asynccontextmanager
async def lifespan(_app: FastAPI):
    print("startup")
    yield
    print("cleanup")


app = FastAPI()

app.add_middleware(LoggerMiddleware)
