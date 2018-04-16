import requests
import json
from bs4 import BeautifulSoup


for y in range(2010, 2018):
	print y
	year = (y * 1000000) + 20000
	game = 1
	url = 'http://statsapi.web.nhl.com/api/v1/game/' + str(year+game) + '/feed/live'
	r = requests.get(url)
	data = json.loads(r.text)

	try:
		while (data['gamePk'] != None):
			if game % 123 == 0:
				print '%d of %d season complete' % (game/12, y)
			with open('games/game-' + str(year+game) + '.txt', 'w') as outfile:
				json.dump(data, outfile)
			game = game+1
			url = 'http://statsapi.web.nhl.com/api/v1/game/' + str(year+game) + '/feed/live'
			r = requests.get(url)
			data = json.loads(r.text)
	except KeyError, e:
		print 'End of season'

print '%d data' % game
