LOG_CONFIG = {
    "version": 1,
    "formatters": {
        "my_formatter": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        },
    },
    "handlers": {
        "file_handler": {
            "class": "logging.FileHandler",
            "formatter": "my_formatter",
            "filename": "result.log"
        },
        "error_file_handler": {
            "class": "logging.FileHandler",
            "formatter": "my_formatter",
            "filename": "result_errors.log"
        },

    },
    "loggers": {
        "result": {
            "handlers": ["file_handler"],
            "level": "INFO",
        },
        "errors": {
            "handlers": ["error_file_handler"],
            "level": "INFO",
        }
    },
}
