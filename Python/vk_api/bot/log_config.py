LOG_CONFIG = {
    "version": 1,
    "formatters": {
        "for_file": {
            "format": "%(asctime)s  - %(levelname)s - %(message)s",
            "datefmt": '%d-%m-%Y %H:%M'

        },
        "for_stream": {
            "format": " %(levelname)s - %(message)s"
        },
    },
    "handlers": {
        "file_handler": {
            "class": "logging.FileHandler",
            "formatter": "for_file",
            "filename": "result.log",
            "encoding": "utf8",
            "level": "DEBUG",
        },
        "stream_handler": {
            "class": "logging.StreamHandler",
            "formatter": "for_stream",
            "level": "DEBUG",


        },

    },
    "loggers": {
        "bot": {
            "handlers": ["file_handler", "stream_handler"],
            "level": "DEBUG",

        }
    },
}
