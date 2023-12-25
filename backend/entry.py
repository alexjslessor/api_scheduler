# from contextlib import asynccontextmanager
from fastapi import FastAPI
import asyncio

from .init import logger
from .deps import get_pol, get_rss
# from .celery_utils import create_celery
from .settings import get_settings

settings = get_settings()
week_seconds =  604800

async def news_task():
    while True:
        logger.info(f'rss task start')
        await get_rss()
        # sleep_time = 5
        sleep_time = 1000
        logger.info(f'rss task complete - sleeping for: {sleep_time}')
        await asyncio.sleep(sleep_time)

async def pol_task():
    while True:
        await get_pol()
        sleep_time = 85
        logger.info(f'pol sleep time: {sleep_time}')
        await asyncio.sleep(sleep_time)

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     asyncio.create_task(pol_task())
#     asyncio.create_task(news_task())
#     yield


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.TITLE,
        # lifespan=lifespan
    )
    # from .init import configure_logging
    # configure_logging()

    # app.celery_app = create_celery()# type: ignore
    # app.include_router(read_routes.router)

    @app.on_event("startup")
    def startup_function():
        asyncio.create_task(pol_task(), name='4chan pol task')
        asyncio.create_task(news_task(), name='RSS feed task')

    return app

