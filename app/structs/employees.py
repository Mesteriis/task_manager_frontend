from pydantic import BaseModel


class EmployeesCreateStruct(BaseModel):
    name: str


class EmployeesStruct(EmployeesCreateStruct):
    id: int

    class Config:
        orm_mode = True
