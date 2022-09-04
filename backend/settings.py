from functools import lru_cache
from pydantic import BaseSettings
from os import environ
from typing import List
# import os.path
import ssl

class _BaseSettings(BaseSettings):
    # TITLE: str = 'Example App'
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
    # MONGO_URI_DEV: str = environ.get('MONGO_URI_DEV')
    # MONGO_DB_NAME: str = 'database'
    # https://docs.celeryq.dev/en/stable/userguide/configuration.html#id11
    BROKER_USE_SSL = {
        'cert_reqs': ssl.CERT_NONE
    }
    CELERY_BROKER_URL: str = environ.get("CELERY_BROKER_URL")
    RESULT_BACKEND: str = environ.get("RESULT_BACKEND")
    WS_MESSAGE_QUEUE: str = environ.get("WS_MESSAGE_QUEUE")

    # RESULT_BACKEND: str = 'rediss://default:AVNS_FI4Hb3oB0jG36lKv6Pv@db-redis-tor1-70141-do-user-4185874-0.b.db.ondigitalocean.com:25061?ssl_cert_reqs=none'
    # WS_MESSAGE_QUEUE: str = 'rediss://default:AVNS_FI4Hb3oB0jG36lKv6Pv@db-redis-tor1-70141-do-user-4185874-0.b.db.ondigitalocean.com:25061?ssl_cert_reqs=none'
    # CELERY_BROKER_URL: str = 'rediss://default:AVNS_FI4Hb3oB0jG36lKv6Pv@db-redis-tor1-70141-do-user-4185874-0.b.db.ondigitalocean.com:25061?ssl_cert_reqs=none'
    CELERY_BEAT_SCHEDULE: dict = {
        "sanity-task": {
            "task": "tasks.sanity_task",
            "schedule": 80.0,
        },
        "get-pol": {
            "task": "tasks.get_pol",
            "schedule": 40.0,
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
