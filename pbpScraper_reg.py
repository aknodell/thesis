import requests
import json

for y in range(2010, 2018):
	print y
	year = (y * 1000000) + 20000
	game = 1
	url = 'http://statsapi.web.nhl.com/api/v1/game/' + str(year+game) + '/feed/live'
	r = requests.get(url)
	data = json.loads(r.text)

	try:
		while (data['gamePk'] != None):
			with open('games/game-' + str(year+game) + '.json', 'w') as outfile:
				json.dump(data, outfile)
			game = game+1
			url = 'http://statsapi.web.nhl.com/api/v1/game/' + str(year+game) + '/feed/live'
			r = requests.get(url)
			data = json.loads(r.text)
	except KeyError, e:
		True

