import logging
from datetime import datetime
from colorama import init as colorama_init, Style


from pydantic import BaseModel

from ..constants import NAMED_LOG_LEVEL_COLOR

logger = logging.getLogger(__name__)


class BaseJsonLogSchema(BaseModel):
    """
    Schema of the main body of the log in JSON format
    """

    thread: int | str
    level: int
    level_name: str
    message: str
    source: str
    timestamp: str
    app_name: str
    app_version: str
    app_env: str
    duration: int
    exceptions: list[str] | None = None
    trace_id: str | None = None
    span_id: str | None = None
    parent_id: str | None = None

    class Config:
        allow_population_by_field_name = True


class LogMessage(BaseModel):
    app_env: str
    app_name: str
    app_version: str
    duration: int
    exceptions: list | None
    level_name: str
    level: int
    message: str
    remote_ip: str | None
    remote_port: int | None
    request_body: str | None
    request_content_type: str | None
    request_direction: str | None
    request_headers: str | None
    request_host: str | None
    request_method: str | None
    request_path: str | None
    request_path: str | None
    request_protocol: str | None
    request_referer: str | None
    request_size: int | None
    request_uri: str | None
    response_body: str | None
    response_headers: str | None
    response_size: int | None
    response_status_code: int | None
    source: str
    timestamp: datetime
    thread: int | str
    level: int
    level_name: str
    message: str
    trace_id: str | None = None
    span_id: str | None = None
    parent_id: str | None = None

    def print(self):  # noqa: T202
        colorama_init()
        format_ = NAMED_LOG_LEVEL_COLOR[self.level]
        print(  # noqa: T201
            "%s%s[%-5s] %-8s: %s%s"
            % (
                format_.fore or "",
                format_.back or "",
                self.thread,
                self.level_name,
                self.message,
                Style.RESET_ALL,
            ),
        )
        if self.exceptions:
            for el in self.exceptions:
                print(el, end="")  # noqa: T201
