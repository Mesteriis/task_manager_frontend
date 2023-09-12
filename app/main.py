import logging
from logging.config import dictConfig

from asgi_correlation_id import CorrelationIdMiddleware
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi.middleware.cors import CORSMiddleware
from app.api import api_router
from app.config import settings
from app.utils.async_logger import LoggingMiddleware

dictConfig(settings.logger_config)
logger = logging.getLogger(settings.project_name)

app = FastAPI(**settings.dict())
app.middleware("http")(LoggingMiddleware())
app.add_middleware(CorrelationIdMiddleware)
app.add_middleware(DBSessionMiddleware, db_url=settings.db.url)

app.include_router(api_router, prefix="/api")


origins = [
    "http://localhost:5173",
    "http://localhost:8080",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
