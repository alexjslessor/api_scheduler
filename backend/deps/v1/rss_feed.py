from ..base_deps import *
from motor.core import AgnosticDatabase
from osint_tools.rss import EnumRSS, RssSchemaList

async def get_rss(db: AgnosticDatabase):
    urls = EnumRSS.list_name_or_value('value')
    data = RssSchemaList.from_url_list(urls)
    await data.to_db(
        db,
        'rss',
        'article_id', 
    )
    return True

