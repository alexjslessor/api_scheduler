from functools import lru_cache
from pydantic import BaseSettings
from os import environ
import ssl

class _BaseSettings(BaseSettings):
    TITLE: str = 'Schedule API'
    # DOCS_URL: str = '/docs'
    # OPENAPI_URL: str = '/openapi'
    # REDOC_URL: str = '/redoc'

    # V1_PREFIX = '/'
    # TAGS: List[str] = ['']
    # CORS_ALLOW_CREDENTIALS: bool = True
    # CORS_ALLOW_METHODS: List[str] = ['*']
    # CORS_ALLOW_HEADERS: List[str] = ['*']
    # CORS_ORIGINS: List[str] = ['*']
    # PORT: int = environ.get('PORT')
    API_LOGGER = environ.get('API_LOGGER', __name__)
    TASK_LOGGER = environ.get('TASK_LOGGER', __name__)

    MONGO_URI: str = environ['MONGO_URI']
    MONGO_DB_NAME: str = environ['MONGO_DB_NAME']

    # https://docs.celeryq.dev/en/stable/userguide/configuration.html#id11
    BROKER_USE_SSL = {
        'cert_reqs': ssl.CERT_NONE
    }
    # for celery namespace vars must be prefixed with CELERY_
    # CELERY_BROKER_URL: str = environ["CELERY_BROKER_URL"]
    # CELERY_RESULT_BACKEND: str = environ["CELERY_RESULT_BACKEND"]
    # WS_MESSAGE_QUEUE: str = environ["WS_MESSAGE_QUEUE"]
    CELERY_CELERYD_LOG_FORMAT: str = '[%(asctime)s: %(levelname)s/%(processName)s] %(message)s'
    CELERY_CELERYD_TASK_LOG_FORMAT: str = '[%(asctime)s: %(levelname)s/%(processName)s][%(task_name)s(%(task_id)s)] %(message)s'
    # CELERY_CELERYD_LOG_FILE: str = environ['LOG_FILE_PATH']  # Update with your log file path
    # for prod
    # CELERYD_LOG_FILE = '[stderr]'

    CELERY_CELERYD_LOG_LEVEL: str = 'INFO'  # Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    # https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html#available-fields
    CELERY_BEAT_SCHEDULE: dict = {
        "sanity-task": {
            "task": "tasks.sanity_task",
            "schedule": 5,
        },
        "get-pol": {
            "task": "tasks.get_pol",
            "schedule": 10,
        },
        "get-rss-celery": {
            "task": "tasks.get_rss_celery",
            "schedule": 45,
        }
    }

# class DevSettings(_BaseSettings):
    # ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    # DATA_DIR = os.path.join(ROOT_DIR, 'data')

# class ProdSettings(_BaseSettings):
#     pass

# class TestSettings(_BaseSettings):
#     pass

@lru_cache()
def get_settings() -> BaseSettings:
    return _BaseSettings()

# @lru_cache()
# def get_settings() -> BaseSettings:
#     config_dict = {
#         'development': DevSettings,
#         # 'production': ProdSettings,
#         # 'testing': TestSettings
#     }
#     config_name: str = environ.get('ENV_NAME', 'development')
#     assert config_name != None, f'Set ENV_NAME variable: {list(config_dict.keys())}'
#     config_cls = config_dict[config_name]
#     return config_cls()
