from HTMLParser import HTMLParser
import requests

class MLStripper(HTMLParser):
	def __init__(self):
		self.reset()
		self.fed = []
	def handle_data(self, d):
		self.fed.append(d)
	def getData(self):
		return ''.join(self.fed)

for season in xrange(20102011, 20172019, 10001):
	baseUrl = 'http://nhl.com/scores/htmlreports/'+str(season)+'/T'
	lastGame = 21231
	if season == 20122013:
		lastGame = 20721
	elif season == 20172018:
		lastGame = 21272
	for game in range(20001, lastGame):
		s = MLStripper()

		visURL = baseUrl+'V0'+str(game)+'.HTM'
		r = requests.get(visURL)
		s.feed(r.text)

		homeURL = baseUrl+'H0'+str(game)+'.HTM'
		r = requests.get(homeURL)
		s.feed(r.text)
		data = s.getData().encode("utf-8")

		s.reset()

		f = open('shifts/shifts-'+str(season)[:4]+'0'+str(game)+'.txt', 'w')
		f.write(data)		
		f.close()

