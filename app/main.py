from fastapi import FastAPI
from loguru import logger
from fastapi.middleware.cors import CORSMiddleware
from app.api import api
from app.core.config import config
from app.version import VERSION


logger.add(
    "./logs/system_monitoring.log",
    rotation="50 MB",
    retention=5,
)


app = FastAPI(
    title=config.SERVICE_NAME,
    debug=config.DEBUG,
    description=config.DESCRIPTION,
    version=VERSION
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api.router, prefix=config.API_V1_STR)
