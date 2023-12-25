from .conftest import *
from backend.deps import get_rss

'''
24-Dec-23 14:12:37 - 64007 - ERROR - get_rss
    - batch op errors occurred, 
    - full error: {'writeErrors': [{'index': 137, 'code': 66, 'errmsg': 'After applying the update, the (immutable) field \'_id\' was found to have been altered to _id: "f8dc2c9b-7e49-4c0c-92d7-dc4a21509195"', 

'op': SON([('q', {'unique_id': 'https://feeds.simplecast.com/54nAGcIl-https://www.nytimes.com/the-daily'}), 
    ('u', {
        '_id': 'f8dc2c9b-7e49-4c0c-92d7-dc4a21509195', 
        'unique_id': 'https://feeds.simplecast.com/54nAGcIl-https://www.nytimes.com/the-daily', 
        'authors': [{'name': 'The New York Times'}, {'name': 'The New York Times'}], 'author': 'The New York Times', 'author_detail': {'name': 'The New York Times'}, 'credit': None, 'media_credit': None, 'title': 'The New State of the War in Gaza', 'link': 'https://www.nytimes.com/the-daily', 'links': [{'rel': 'alternate', 'type': 'text/html', 'href': 'https://www.nytimes.com/the-daily'}, {'rel': 'enclosure', 'type': 'audio/mpeg', 'href': 'https://dts.podtrac.com/redirect.mp3/chrt.fm/track/8DB4DB/pdst.fm/e/pfx.vpixl.com/6qj4J/nyt.simplecastaudio.com/03d8b493-87fc-4bd1-931f-8a8e9b945d8a/episodes/53d6fff6-6590-4ad0-8e75-26467fe8d88d/audio/128/default.mp3?aid=rss_feed&awCollectionId=03d8b493-87fc-4bd1-931f-8a8e9b945d8a&awEpisodeId=53d6fff6-6590-4ad0-8e75-26467fe8d88d&feed=54nAGcIl'}], 
        'published': 'Thu, 21 Dec 2023 10:45:00 +0000', 
        'tags': None, 
        'media_content': None, 
        'summary_detail': {
            'base': 'https://feeds.simplecast.com/54nAGcIl', 
            'language': None, 
            'type': 'text/plain', 
            'value': 'The accidental killing of three hostages by Israel’s military has shocked Israelis and is raising new questions about the way Israel is conducting its war against Hamas. Afterward, Israel’s defense minister appeared to announce a shift in strategy, giving the clearest indication to date that Israel may slow down its military operation in Gaza after weeks of pressure. Patrick Kingsley, Jerusalem bureau chief for The Times, and Hiba Yazbek, a reporter for The Times, discuss Israel’s military campaign and the ensuing humanitarian crisis.'}, 
            'flag': <PropCategory.UN_CATEGORIZED: 'UN_CATEGORIZED'>, 
            'topic': <Topic.UN_ASSIGNED: 'UN_ASSIGNED'>, 
            'is_sorted': False, 
            'rss_url': 'https://feeds.simplecast.com/54nAGcIl'
        }
    ), 
    ('multi', False), ('upsert', True)])}], 
    'writeConcernErrors': [], 'nInserted': 0, 'nUpserted': 0, 'nMatched': 137, 'nModified': 0, 'nRemoved': 0, 'upserted': []
}
'''
@pytest.mark.asyncio
class TestRssWorker:
    async def test_rss_worker(self):
        data = await get_rss()
        # pprint(data)
        assert data, 'result list empty'
