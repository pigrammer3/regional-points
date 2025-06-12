import requests_cache
import os

session = requests_cache.CachedSession("tba_cache")

HEADERS = {
    "X-TBA-Auth-Key": os.getenv("TBA_API_KEY", ""),
}

ROOT_URL = "https://www.thebluealliance.com/api/v3"

TEAM_PAGES = 22

session.headers.update(HEADERS)