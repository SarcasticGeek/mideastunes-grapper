 # -*- coding: UTF-8 -*-

import json, requests, MySQLdb

f = open('output.json','a')


db = MySQLdb.connect("localhost","root","","mideastunes")
cursor = db.cursor()


def get_artist_info(artist_id):
	artist = {}
	url = 'https://mideastunes.com/api/v2/artists/' + artist_id + '/'
	header = {'x-requested-with': 'XMLHttpRequest' , 'Content-type': 'application/json', 'charset': 'utf-8'}
	try:
		t = requests.get(url, headers=header).json()
	except:
		pass
	artist['genres'] = t['data'][0]['genres']
	artist['name'] = t['data'][0]['metadata']['name']
	artist['country'] = t['data'][0]['metadata']['country']['name']
	return  json.dumps(artist)



f.write(get_artist_info('293645299853512635857334967308633966888'))

f.close()