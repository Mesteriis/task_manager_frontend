from .logger import get_logger_config
from .database import DataBaseSettings
from .mixin import PrintSettingsMixin


class Settings(PrintSettingsMixin):
    project_name: str
    project_version: str
    project_description: str = ""

    env: str = "dev"
    port: int = 8000
    origins: list = []

    db = DataBaseSettings()

    @property
    def logger_config(self) -> dict:
        return get_logger_config(self)

    @property
    def debug(self) -> bool:
        return self.env == "dev"

    disable_docs: bool = False
    docs_url: str = "/docs"
    redoc_url: str | None = None

    redis_url: str | None = None

    class Config:
        env_prefix = "api_"
        validate_assignment = True
