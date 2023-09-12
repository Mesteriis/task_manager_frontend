from fastapi_sqlalchemy import db
from sqlalchemy.orm import joinedload

from app.models import TasksModel, EmployeesModel
from app.models.tasks.constants import StatusTaskEnum


class ImportantTasks:
    __db = db

    @classmethod
    def __get_important_tasks(cls) -> list[type[TasksModel]]:
        return (
            cls.__db.session.query(TasksModel)
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

    @classmethod
    def __get_most_free_employee(cls) -> type[TasksModel] | None:
        most_free_employees = (
            cls.__db.session.query(
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
        return most_free_employee

    @classmethod
    def get_important_tasks(cls) -> list[dict]:
        answer = []
        most_free_employee = cls.__get_most_free_employee()
        for el in cls.__get_important_tasks():
            employees = [most_free_employee]
            if emp := cls.__get_employee_from_parent(el, len(most_free_employee.tasks)):
                employees.append(emp)
            answer.append(
                {
                    "task": el,
                    "deadline": el.deadline,
                    "employees": employees,
                },
            )

        return answer

    @classmethod
    def __get_employee_from_parent(cls, task: TasksModel, task_barrier):
        if task.parent:
            return cls.__get_employee_from_parent(task.parent, task_barrier)
        return (
            task.employee
            if ((len(task.employee.tasks) or 0) + 2) < task_barrier
            else None
        )
