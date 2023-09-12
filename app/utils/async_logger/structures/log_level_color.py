from pydantic import BaseModel


class LogLevelStringColor(BaseModel):
    level_name: str
    fore: str | None = None
    back: str | None = None

    class Config:
        arbitrary_types_allowed = True
