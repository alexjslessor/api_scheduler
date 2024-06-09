from contextlib import asynccontextmanager
from motor.core import AgnosticDatabase
from fastapi import FastAPI
import asyncio

from osint_tools.db import MongoCrud
from .init import logger
from .deps import get_pol, get_rss
from .settings import get_settings
# from .celery_utils import create_celery

settings = get_settings()
week_seconds =  604800

async def news_task(db: AgnosticDatabase):
    try:
        while True:
            logger.info(f'rss task start')
            await get_rss(db)
            # sleep_time = 5
            sleep_time = 1000
            logger.info(f'rss task complete - sleeping for: {sleep_time}')
            await asyncio.sleep(sleep_time)
    except Exception as e:
        logger.error(f'{e!s}')
        raise

async def pol_task(db: AgnosticDatabase):
    try:
        while True:
            await get_pol(db)
            sleep_time = 85
            logger.info(f'pol sleep time: {sleep_time}')
            await asyncio.sleep(sleep_time)
    except TypeError as e:
        logger.error(f'{e!s}')
        raise

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info('app startup...')

    mon_db = MongoCrud(settings.MONGO_URI, settings.MONGO_DB_NAME)
    db = mon_db.get_mongo_db()

    # create index on "no" field
    idx = await mon_db.create_unique_idx(db['4chan'], 'no')

    asyncio.create_task(pol_task(db))
    asyncio.create_task(news_task(db))
    yield
    logger.info('app shutdown...')

def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.TITLE,
        lifespan=lifespan
    )
    return app

