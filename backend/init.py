from osint_tools.db import MongoCrud
from .settings import get_settings
import logging
import logging.config
from os import environ
from typing import Optional
# from celery.utils.log import get_task_logger
# from celery.signals import task_postrun, setup_logging


# @setup_logging.connect()
# def on_setup_logging(**kwargs):
#     logging_dict = {
#         'version': 1,
#         'disable_existing_loggers': False,
#         'handlers': {
#             'file_log': {
#                 'class': 'logging.FileHandler',
#                 'filename': 'celery.log',
#             },
#             'console': {
#                 'class': 'logging.StreamHandler',
#             }
#         },
#         'loggers': {
#             'celery': {
#                 'handlers': ['console', 'file_log'],
#                 'propagate': False,
#             },
#         },
#         'root': {
#             'handlers': ['console'],
#             'level': 'INFO',
#         },
#     }

#     logging.config.dictConfig(logging_dict)

#     # display task_id and task_name in task log
#     from celery.app.log import TaskFormatter
#     celery_logger = logging.getLogger('celery')
#     for handler in celery_logger.handlers:
#         handler.setFormatter(
#             TaskFormatter(
#                 '[%(asctime)s: %(levelname)s/%(processName)s/%(thread)d] [%(task_name)s(%(task_id)s)] %(message)s'
#             )
#         )

# def configure_logging():
#     logging_dict = {
#         "version": 1,
#         "disable_existing_loggers": False,
#         "formatters": {
#             "verbose": {
#                 "format": "[%(asctime)s: %(levelname)s] [%(pathname)s:%(lineno)d] %(message)s",
#             },
#         },
#         "handlers": {
#             "console": {
#                 "class": "logging.StreamHandler",
#                 "formatter": "verbose",
#             },
#         },
#         "root": {
#             "handlers": ["console"],
#             "level": "INFO",
#         },
#         "loggers": {
#             "project": {
#                 "handlers": ["console"],
#                 "propagate": False,
#             },
#             "uvicorn.access": {
#                 "propagate": True,
#             },
#         },
#     }

#     logging.config.dictConfig(logging_dict)

def setup_logger(which_logger: Optional[str] = None):
    lib_level = logging.DEBUG # Default level for your logger
    # root_level = logging.WARNING # Default level for root logger
    root_level = logging.INFO
    log_format = '%(asctime)s - %(process)d - %(levelname)s - %(funcName)s - %(message)s'
    logging.basicConfig(
        filename=environ.get('LOG_FILE_PATH'),# taken from loca .env file, not set in settings.py
        format=log_format,
        datefmt='%d-%b-%y %H:%M:%S',
        level=root_level,
        force=True
    )
    log = logging.getLogger(which_logger)
    log.setLevel(lib_level)
    return log

settings = get_settings()
logger = setup_logger(__name__)
# logger = logging.getLogger(__name__)

mon_db = MongoCrud(settings.MONGO_URI, settings.MONGO_DB_NAME)
db = mon_db.get_mongo_db()

