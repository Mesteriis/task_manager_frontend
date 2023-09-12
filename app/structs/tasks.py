from datetime import datetime

from pydantic import BaseModel

from app.models.tasks.constants import StatusTaskEnum
from app.structs.employees import EmployeesStruct


class TaskCreateStruct(BaseModel):
    title: str
    employee_id: int | None
    parent_id: int | None
    deadline: datetime | None
    status: StatusTaskEnum = StatusTaskEnum.BACKLOG


class TaskStruct(TaskCreateStruct):
    id: int

    class Config:
        orm_mode = True


class TaskImportantStruct(BaseModel):
    task: TaskStruct
    deadline: datetime | None
    employees: list[EmployeesStruct] | None
