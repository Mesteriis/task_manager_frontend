def get_logger_config(settings) -> dict:
    return {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "json": {
                "()": "app.utils.async_logger.JSONLogFormatter",
            },
        },
        "handlers": {
            "json": {
                "formatter": "json",
                "class": "asynclog.AsyncLogDispatcher",
                "func": "app.utils.async_logger.write_log",
            },
        },
        "filters": {
            "correlation_id": {
                "()": "asgi_correlation_id.CorrelationIdFilter",
                "uuid_length": 32,
                "default_value": "-",
            },
        },
        "loggers": {
            "": {
                "handlers": ["json"],
                "level": "DEBUG" if settings.debug else "INFO",
                "propagate": False,
                "filters": ["correlation_id"],
            },
            "uvicorn": {
                "handlers": ["json"],
                "level": "INFO",
                "propagate": False,
                "filters": ["correlation_id"],
            },
            # Не даем стандартному логгеру fastapi работать по пустякам и замедлять работу сервиса
            "uvicorn.access": {
                "handlers": ["json"],
                "level": "ERROR",
                "propagate": False,
                "filters": ["correlation_id"],
            },
        },
    }
