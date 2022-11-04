from fastapi import FastAPI
from osint_tools.logs import logger
import asyncio
from .deps import get_pol, get_rss
from .celery_utils import create_celery
from .settings import get_settings

settings = get_settings()

async def news_task():
    while True:
        await get_rss()
        sleep_time = 10
        logger.info(f'news sleep time: {sleep_time}')
        await asyncio.sleep(sleep_time)


async def pol_task():
    while True:
        await get_pol()
        sleep_time = 69
        logger.info(f'sleep time: {sleep_time}')
        await asyncio.sleep(sleep_time)

def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.TITLE
    )
    app.celery_app = create_celery()
    # app.include_router(read_routes.router)

    @app.on_event("startup")
    def startup_function():
        # asyncio.create_task(pol_task())
        asyncio.create_task(news_task())


    # @app.on_event("startup")
    # def startup_function():
    #     app.state.shared_object = MySharedObject()
    #     asyncio.create_task(timed_checker(app.state.shared_object))


    return app

