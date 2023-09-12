__all__ = [
    "LoggingMiddleware",
    "JSONLogFormatter",
    "write_log",
]


from .formatter import JSONLogFormatter
from .middlewares import LoggingMiddleware


def write_log(msg):
    msg.print()
