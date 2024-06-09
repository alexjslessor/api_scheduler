from .settings import get_settings
from typing import Optional
# from celery.utils.log import get_task_logger
# from celery.signals import task_postrun, setup_logging

def setup_logger(which_logger: Optional[str] = None):
    import logging
    import logging.config
    from os import environ

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

