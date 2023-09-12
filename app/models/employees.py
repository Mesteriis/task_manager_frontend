from sqlalchemy import Column, Integer, String

from app.core.db import Base


class EmployeesModel(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
