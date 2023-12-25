from ..base_deps import *
from osint_tools.rss import *

async def get_rss():
    urls = EnumRSS.list_name_or_value('value')
    data = RssSchemaList.get_urls(urls)
    await data.to_db(
        db,
        'rss',
        'article_id', 
    )
    return True

