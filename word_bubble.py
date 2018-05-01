import sqlite3
import plotly
import numpy as np
import pprint as pp
import plotly.plotly as py
import plotly.graph_objs as go

def tableFromDatabase(database, table):
    conn = sqlite3.connect(database)  # connection
    c = conn.cursor()  # get a cursor object, all SQL commands are processed by
    c.execute('SELECT * FROM %s' % table)
    tableRows = c.fetchall()
    return tableRows

rows = tableFromDatabase('cryptobase.db', 'sortedTFIDF')

sortKey=[]
sortVal=[]
for i in range(len(rows)):
    sortKey.append(rows[i][0])
    sortVal.append(rows[i][1])

topVal = sortVal[:20]
topKey = sortKey[:20]

# create bubble chart
plotly.tools.set_credentials_file(username='kalidurge', api_key='XA6wRnImtNkMVWtLKilG') #update api key every time
#randomly place x and y values on plot

x = [10,10,10,5,15,5,15,5,15,7.2,12.7,7.2,2.5,17.5,17.5,12.5,12.5,7.5,12.5,7.5]#[5, 6, 7, 8, 9, 10, 11, 12, 0, 1, 2, 3, 4, 13, 14, 15, 16, 17, 18, 19]#[x for x in range(0,20)] #np.array([rand.randrange(0,40) for x in range(0, len(topVal))])
y = [10,16,4,10,10,5,5,15,15,2.5,2.5,17.5,11.8,12.5,7.5,12.5,18,8,8,12.5] #np.array([rand.randrange(0,20) for y in range(0, len(topVal))])
color = sorted(np.random.randn(len(topVal)), reverse=True)

trace1 = go.Scatter(
    x=x,
    y=y,
    text=topKey,
    mode='markers+text',
    marker=dict(color=color, size=topVal, sizemode='area', sizeref=2.*max(topVal)/(150.**2)))

data = [trace1]
layout = go.Layout(title='Today\'s Top 20 Words Based on TF-IDF', titlefont=dict(
            size=32),    xaxis=dict(
        title='Source: Crypto Coins News (www.ccn.com) API: https://newsapi.org/v2/everything?sources=crypto-coins-news&apiKey=1d656ac0916147bf8d28e1dcda71266a',
        autorange=True,
        showgrid=False,
        zeroline=False,
        showline=False,
        autotick=True,
        ticks='',
        showticklabels=False
    ),
    yaxis=dict(
        autorange=True,
        showgrid=False,
        zeroline=False,
        showline=False,
        autotick=True,
        ticks='',
        showticklabels=False
    ))
fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='bubblechart-size')#change to iplot if running within ipython


