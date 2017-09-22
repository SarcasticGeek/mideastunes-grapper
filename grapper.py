import json, requests, MySQLdb

db = MySQLdb.connect("localhost","root","","mideastunes")
cursor = db.cursor()


def get_next(first_one):
	url = 'https://mideastunes.com/api/v2/artists/' + first_one + '/recommended?limit=1'
	header = {'x-requested-with': 'XMLHttpRequest'}
	try:
		t = requests.get(url, headers=header).json()
	except:
		pass
	return t['data'][0]['id']


#first_id = '171405134797285706577463214293552248230'

first_id = '3619879954412152075967840827752410287'
#print(get_next(first_id))

for x in xrange(0,200):
	sql = "INSERT INTO test(artistid) VALUES ("+ first_id +") WHERE NOT EXIST (SELECT * FROM `test` WHERE artistid='"+ first_id +"') LIMIT 1 "
	first_id = get_next(first_id)
	try:
	   cursor.execute(sql)
	   db.commit()
	except:
	   db.rollback()

