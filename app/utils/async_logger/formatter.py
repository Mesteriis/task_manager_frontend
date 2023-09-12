import datetime
import logging
import traceback

from .structures.base import LogMessage, BaseJsonLogSchema
from ...config import settings

NAMED_LOG_LEVEL = {
    0: "NOT_SET",
    10: "DEBUG",
    20: "INFO",
    30: "WARNING",
    40: "ERROR",
    50: "CRITICAL",
}


class JSONLogFormatter(logging.Formatter):
    """
    Custom formatter class for logs in json format
    """

    def format(self, record: logging.LogRecord, *args, **kwargs) -> LogMessage:
        """
        :param record: journal log record
        :return: log dict
        """
        return LogMessage(**self._format_log_object(record))

    @staticmethod
    def _format_log_object(record: logging.LogRecord) -> dict:
        """
        Translation of a log object entry
        to json format with the required list of fields

        :param record: log object
        :return: Dictionary with log objects
        """
        now = (
            datetime.datetime.fromtimestamp(record.created)
            .astimezone()
            .replace(microsecond=0)
            .isoformat()
        )
        message = record.getMessage()
        duration = record.duration if hasattr(record, "duration") else record.msecs
        json_log_fields = BaseJsonLogSchema(
            thread=record.process,
            timestamp=now,
            level=record.levelno,
            level_name=NAMED_LOG_LEVEL[record.levelno],
            message=message,
            source=record.name,
            duration=duration,
            app_name=settings.project_name,
            app_version=settings.project_version,
            app_env=settings.env,
        )

        if hasattr(record, "props"):
            json_log_fields.props = record.props

        if record.exc_info:
            json_log_fields.exceptions = traceback.format_exception(*record.exc_info)

        elif record.exc_text:
            json_log_fields.exceptions = record.exc_text

        json_log_object = json_log_fields.dict(
            exclude_unset=True,
            by_alias=True,
        )
        if hasattr(record, "request_json_fields"):
            json_log_object.update(record.request_json_fields)

        return json_log_object
