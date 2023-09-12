from sqlalchemy import (
    ForeignKey,
    Enum,
    DateTime,
)
from sqlalchemy.orm import relationship, mapped_column

from app.core.db import Base
from .constants import StatusTaskEnum

from sqlalchemy import Column, Integer, String


class TasksModel(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)

    employee_id = mapped_column(ForeignKey("employees.id"))
    employee = relationship("EmployeesModel", backref="tasks")

    parent_id = mapped_column(ForeignKey("tasks.id"))
    parent = relationship("TasksModel", backref="children", remote_side=id)  # noqa

    deadline = Column(DateTime(timezone=True), nullable=True)
    status = Column(Enum(StatusTaskEnum), default=StatusTaskEnum.BACKLOG)
