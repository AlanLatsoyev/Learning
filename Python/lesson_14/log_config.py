LOG_CONFIG = {
    "version": 1,
    "formatters": {
        "my_formatter": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            "datefmt": '%d-%m-%Y %H:%M:%S'
        },
    },
    "handlers": {
        "file_handler": {
            "class": "logging.FileHandler",
            "formatter": "my_formatter",
            "filename": "result.log",
            "encoding": "utf8",
        },
        "error_file_handler": {
            "class": "logging.FileHandler",
            "formatter": "my_formatter",
            "filename": "result_errors.log",
            "encoding": "utf8",

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
