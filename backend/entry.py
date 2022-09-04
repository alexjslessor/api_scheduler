from fastapi import FastAPI
from .routers.v1 import read_routes
from .celery_utils import create_celery
from osint_tools import get_catalog, Board
from pprint import pprint
import asyncio


async def get_pol():
    # time.sleep(45)
    data = get_catalog(Board.b)
    assert data is not None
    assert len(data) > 0
    pprint(data[:1])

async def timed_checker():
    while True:
        await get_pol()
        await asyncio.sleep(5)

def create_app() -> FastAPI:
    app = FastAPI()
    app.celery_app = create_celery()
    app.include_router(read_routes.router)

    @app.on_event("startup")
    def startup_function():
        # app.state.shared_object = MySharedObject()
        asyncio.create_task(timed_checker())
        # asyncio.create_task(timed_checker(app.state.shared_object))


    # @app.on_event("startup")
    # def startup_function():
    #     app.state.shared_object = MySharedObject()
    #     asyncio.create_task(timed_checker(app.state.shared_object))


    return app

