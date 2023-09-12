from .mixin import PrintSettingsMixin


class DataBaseSettings(PrintSettingsMixin):
    is_async: bool = True
    user: str
    password: str
    host: str
    port: str
    name: str

    class Config:
        env_prefix = "db_"
        validate_assignment = True

    @property
    def url(self) -> str:
        if self.is_async:
            return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"
        else:
            return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"
