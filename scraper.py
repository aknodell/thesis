import requests
from bs4 import BeautifulSoup

url = 'http://statsapi.web.nhl.com/api/v1/game/2010020001/feed/live'
r = requests.get(url)
data = r.text

print data
