import asyncio
import json
import httpx
from osint_tools.api import get_catalog, Board
from osint_tools.schemas import EnumRSS
from osint_tools.api import get_catalog, Board, RSSFeed

from pprint import pprint
from pymongo import ReplaceOne
from osint_tools.logs import logger
from ..con_db import mon_db, db

