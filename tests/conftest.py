from asgi_lifespan import LifespanManager
# from starlette.status import HTTP_200_OK
from httpx import AsyncClient
from pprint import pprint
import pytest_asyncio
import pytest
import asyncio

from osint_tools.db import MongoCrud

# from backend.entry import create_app
from backend.deps import *
from backend.settings import get_settings
from backend.init import logger

settings = get_settings()
mon_db = MongoCrud(settings.MONGO_URI, settings.MONGO_DB_NAME)
db = mon_db.get_mongo_db()



# app = create_app()


# @pytest_asyncio.fixture(scope="session")
# def event_loop():
#     loop = asyncio.get_event_loop()
#     yield loop
#     loop.close()

# @pytest_asyncio.fixture
# async def test_client():
#     async with LifespanManager(app):
#         async with AsyncClient(app=app, base_url="https://app.io", timeout=30) as test_client:
#             yield test_client
