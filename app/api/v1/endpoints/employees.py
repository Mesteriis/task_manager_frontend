from fastapi_crudrouter import SQLAlchemyCRUDRouter


from app.core.db import get_session
from app.models import EmployeesModel
from app.structs.employees import EmployeesStruct, EmployeesCreateStruct

employees_router = SQLAlchemyCRUDRouter(
    schema=EmployeesStruct,
    create_schema=EmployeesCreateStruct,
    db_model=EmployeesModel,
    db=get_session,
    delete_all_route=False,
)
