from tests.conftest import db, logger
import pytest
from backend.deps import get_rss

@pytest.mark.asyncio
class TestRssWorker:
    async def test_rss_worker(self):
        data = await get_rss(db)
        logger.info(data)
        assert data, 'result list empty'
