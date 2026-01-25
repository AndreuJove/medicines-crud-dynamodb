import logging

# from logging.config import dictConfig
# from os import getenv

# LOG_CONFIG = {
#     "version": 1,
#     "formatters": {
#         "default": {
#             "format": "%(asctime)s  %(levelname)s %(message)s",
#             "datefmt": "%d-%m-%Y %H:%M:%S",
#         }
#     },
#     "handlers": {
#         "console": {
#             "formatter": "default",
#             "class": "logging.StreamHandler",
#             "stream": "ext://sys.stdout",
#             "level": getenv("LOG_LEVEL", "DEBUG"),
#         }
#     },
#     "root": {"handlers": ["console"], "level": getenv("LOG_LEVEL", "DEBUG")}
# }

# dictConfig(LOG_CONFIG)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
