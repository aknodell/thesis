import requests
import json
import math

for y in range(2010, 2018):
	print y
	year = (y * 1000000) + 30000
	for rnd in range(1, 5):
		for series in range(1, int(math.pow(2, 4-rnd)+1)):
			game = 1
			url = 'http://statsapi.web.nhl.com/api/v1/game/' + str(year+(rnd*100)+(series*10)+game) + '/feed/live'
			r = requests.get(url)
			data = json.loads(r.text)

			try:
				while (data['gamePk'] != None):
					with open('games/game-' + str(year+(rnd*100)+(series*10)+game) + '.json', 'w') as outfile:
						json.dump(data, outfile)
					game = game+1
					url = 'http://statsapi.web.nhl.com/api/v1/game/' + str(year+(rnd*100)+(series*10)+game) + '/feed/live'
					r = requests.get(url)
					data = json.loads(r.text)
			except KeyError, e:
				True

