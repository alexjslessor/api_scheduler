from ..base_deps import *

rss = RSSFeed()

async def get_rss():
    all_feeds = []
    for url in EnumRSS.list_name_or_value('value'):
        all_feeds += rss.get_feed(url)

    update = []
    for article in all_feeds:
        update.append(ReplaceOne(
            {'unique_id': article.unique_id}, article.to_dict(), upsert=True)
        )

    # idx = await mon_db.create_unique_idx(db['rss'], '_id')
    # delete = await db['rss'].delete_many({})
    # delete = await db.drop_collection('rss')

    result = await db['rss'].bulk_write(update)

    logger.info(f"rss nModified: {result.bulk_api_result['nModified']}")
    logger.info(f"rss nUpserted: {result.bulk_api_result['nUpserted']}")
    logger.info(f"rss nInserted: {result.bulk_api_result['nInserted']}")
    logger.info(f"rss nMatched: {result.bulk_api_result['nMatched']}")


