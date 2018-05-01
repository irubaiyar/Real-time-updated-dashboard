import time
import datetime
import requests
import sqlite3
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html


def historical_data():
	response_his = requests.get("https://min-api.cryptocompare.com/data/histominute?fsym=BTC&tsym=USD&limit=2000")
	a = response_his.json()
	his = []
	for i in range(len(a[u'Data'])):
		data = []
		data.append(time.strftime("%D %H:%M", time.localtime(int(a[u'Data'][i][u'time']))))
		data.append(a[u'Data'][i][u'close'])
		his.append(data)
	return his
def current():
	response_current = requests.get("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD")
	current_row = response_current.json()
	current = current_row[u'USD']
	return current
a = historical_data()
b = current()
d = ['BTC', b]
conn = sqlite3.connect('crypto.db')
c = conn.cursor()
#c.execute('DROP TABLE historical_data')
c.execute('CREATE TABLE historical_data(time TEXT, price FLOAT)')
c.executemany('INSERT INTO historical_data VALUES(?,?)', a)
c.execute('CREATE TABLE current_data(type TEXT, price FLOAT)')
c.execute('INSERT INTO current_data VALUES(?,?)', d)
conn.commit()
#conn.close()
i = 0
while i <10000:
	#conn = sqlite3.connect('crypto.db')
	#c = conn.cursor()
	a_0 = historical_data()
	if a[len(a)-1][0] != a_0[len(a_0)-1][0]:
		a.append(a_0[len(a_0)-1])
		c.execute('INSERT INTO historical_data VALUES(?,?)', a[len(a)-1])
	c.execute('SELECT MAX(time), price FROM historical_data')
	print c.fetchall()
	c.execute('SELECT COUNT(*) FROM historical_data')
	print c.fetchall()
	c.execute('SELECT * FROM historical_data')
	table = c.fetchall()
	print len(table)
	b = current()
	d = ['BTC', b]
	c.execute('DELETE FROM current_data')
	c.execute('INSERT INTO current_data VALUES(?,?)', d)
	c.execute('SELECT * FROM current_data')
	print c.fetchall()
	i = i+1
	time.sleep(10)
	conn.commit()
conn.close()
