from fastapi import APIRouter
from fastapi_crudrouter import SQLAlchemyCRUDRouter

from app.core.db import get_session
from app.models import TasksModel
from app.service import ImportantTasks
from app.structs.tasks import TaskStruct, TaskCreateStruct, TaskImportantStruct

tasks_router = SQLAlchemyCRUDRouter(
    schema=TaskStruct,
    create_schema=TaskCreateStruct,
    db_model=TasksModel,
    db=get_session,
    delete_all_route=False,
)

important_router = APIRouter(prefix="/important")


@important_router.get("", response_model=list[TaskImportantStruct], tags=["service"])
def get_important_tasks():

    return ImportantTasks.get_important_tasks()
