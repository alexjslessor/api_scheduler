from .conftest import *
from osint_tools.four_chan import get_catalog

@pytest.mark.asyncio
class TestChanWorker:
    async def test_get_chan(self):
        data = get_catalog('pol')
        logger.info(data[:3])
        assert data, 'result list empty'

        # loop = aio.get_or_create_eventloop()
        # loop.run_until_complete(
            # mon_db.insert_many_documents(db, CollectionNames.testing, data)
            # mon_db.insert_docs_test(db, CollectionNames.testing, d)
        # )

        # asyncio.run(db[CollectionNames.testing].insert_docs_test(db, CollectionNames.testing, data))
        # asyncio.run(mon_db.insert_many_documents(db, CollectionNames.testing, data))


































# class Decorators:

#     def timefunc(func):
#         def f(*args, **kwargs):
#             from time import time
#             start = time()
#             rv = func(*args, **kwargs)
#             finish = time()
#             print('Run time is.', finish - start)
#             return rv
#         return f


# @pytest.mark.asyncio
# class Test_Dependancies:

#     # @Decorators.timefunc
#     # async def test_get_chan_v2(self):
#         # data = await get_catalog_v2()
#         # pprint(data)

#     @Decorators.timefunc
#     async def test_get_chan(self):
#         data = get_catalog()
#         # pprint(data)

#     # async def test_chan_schema(self):
#     #     data = get_catalog()[0]
#     #     assert isinstance(data, BaseModel)

