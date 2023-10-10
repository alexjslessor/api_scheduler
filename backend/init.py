from osint_tools.db import *
from .settings import get_settings

import logging
from os import environ
from typing import Optional

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
logger = setup_logger(settings.API_LOGGER)
mon_db = MongoCrud(settings.MONGO_URI, settings.MONGO_DB_NAME)
db = mon_db.get_mongo_db()

