from osint_tools.db import *
from osint_tools.api import *
from osint_tools.settings import get_settings

mon_db = MongoCrud(settings.MONGO_URI, settings.MONGO_DB_NAME)
db = mon_db.get_mongo_db()



