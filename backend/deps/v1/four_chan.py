from ..base_deps import *
from pymongo import ReplaceOne
from motor.core import AgnosticDatabase
from osint_tools.four_chan import get_catalog, Board

async def get_pol(db: AgnosticDatabase):
    try:
        data = get_catalog(Board.pol)

        update: list = []
        for catalog_model in data:
            update.append(
                ReplaceOne(
                    {'no': catalog_model.no}, 
                    catalog_model.dict(), 
                    upsert=True
                )
            )

        result = await db['4chan'].bulk_write(update)    
        logger.info(f"4chan nModified: {result.bulk_api_result['nModified']}")
        logger.info(f"4chan nUpserted: {result.bulk_api_result['nUpserted']}")
        logger.info(f"4chan nInserted: {result.bulk_api_result['nInserted']}")
        logger.info(f"4chan nMatched: {result.bulk_api_result['nMatched']}")
        return True
    except Exception as e:
        logger.error(f'Error get_pol: {e!s}')

