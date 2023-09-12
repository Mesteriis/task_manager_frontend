__all__ = [
    "v1_router",
]

from fastapi import APIRouter

from .endpoints import employees_router, tasks_router, important_router

v1_router = APIRouter(prefix="/v1")

v1_router.include_router(employees_router)
v1_router.include_router(tasks_router)
v1_router.include_router(important_router)
