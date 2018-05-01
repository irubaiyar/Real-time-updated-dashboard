import pprint
import sqlite3

pp = pprint.PrettyPrinter()

conn = sqlite3.connect('cryptobase.db') #connection
c = conn.cursor()  #get a cursor object, all SQL commands are processed by it
c.execute('CREATE TABLE coinsNews(description TEXT, title TEXT, url TEXT, author TEXT, published TEXT)') #create a table
c.executemany('INSERT INTO coinsNews VALUES(?,?,?,?,?)', articlesList)

c.execute('SELECT * FROM coinsNews')
pp.pprint(c.fetchall()) 

conn.commit() #save the changes
conn.close()

