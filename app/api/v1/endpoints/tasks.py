from fastapi import APIRouter
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from fastapi_sqlalchemy import db
from sqlalchemy.orm import joinedload

from app.core.db import get_session
from app.models import TasksModel, EmployeesModel
from app.models.tasks.constants import StatusTaskEnum
from app.structs.tasks import TaskStruct, TaskCreateStruct, TaskImportantStruct

tasks_router = SQLAlchemyCRUDRouter(
    schema=TaskStruct,
    create_schema=TaskCreateStruct,
    db_model=TasksModel,
    db=get_session,
    delete_all_route=False,
)

important_router = APIRouter(prefix="/important")


@tasks_router.get("", response_model=list[TaskImportantStruct])
def get_important_tasks():
    important_tasks = (
        db.session.query(TasksModel)
        .filter(
            TasksModel.status.in_(
                [
                    StatusTaskEnum.BACKLOG,
                    StatusTaskEnum.SPIRIT_BACKLOG,
                    StatusTaskEnum.SPRINT_CANDIDATE,
                ],
            )
            | TasksModel.employee_id.is_(None),  # noqa W503
        )
        .options(
            joinedload(TasksModel.employee),
        )
        .all()
    )

    most_free_employees = (
        db.session.query(
            EmployeesModel,
        )
        .options(
            joinedload(EmployeesModel.tasks),
        )
        .all()
    )

    most_free_employee = None
    for el in most_free_employees:
        if not most_free_employee:
            most_free_employee = el
        if len(most_free_employee.tasks) > len(el.tasks):
            most_free_employee = el

    answer = []
    for el in important_tasks:
        employees = [most_free_employee]
        if emp := get_employee_from_parent(el, len(most_free_employee.tasks)):
            employees.append(emp)
        answer.append(
            {
                "task": el,
                "deadline": el.deadline,
                "employees": employees,
            },
        )

    return answer


def get_employee_from_parent(task: TasksModel, task_barrier):
    if task.parent:
        return get_employee_from_parent(task.parent, task_barrier)
    return (
        task.employee if ((len(task.employee.tasks) or 0) + 2) < task_barrier else None
    )
