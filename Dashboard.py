import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.dashboard_objs as dashboard
import numpy as np
import re

#https://plot.ly/python/create-online-dashboard/
#Set credentials to online account changing username and api_key
plotly.tools.set_credentials_file(username='richard.anderson13', api_key='O1Tj3r0RDAftvHgsgzwH')

#initialize a dashboard
my_dboard = dashboard.Dashboard()
my_dboard.get_preview()

#data = Cryptobase? auto_open will bring the dashboard up once we run the script
data = [trace1, trace2, trace3]
url_1 = py.plot(data, filename = 'Cryptocurrency Dashboard', auto_open=True)

#Not sure if necessary. In Ipython this actually calls the pyplot
#py.iplot(data, filename='Cryptocurrency Dashboard') 

#Extract the file ID from a url. Used to get dashboard file ID
def fileId_from_url(url):
    """Return fileId from a url."""
    raw_fileId = re.findall("~[A-z]+/[0-9]+", url)[0][1: ]
    return raw_fileId.replace('/', ':')

#return sharekey from a url. May not be useful as we are keeping everything public
'''def sharekey_from_url(url):
    if 'share_key=' not in url:
        return "This url is not 'sercret'. It does not have a secret key."
    return url[url.find('share_key=') + len('share_key='):]'''

fileId_1 = fileId_from_url(url_1)
fileId_2 = fileId_from_url(url_2)

#Plot box into dashboard (useful for prices or Sabrina's number of hashtags used)
box_a = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': 'fileId_1',
    'title': 'Scatter Plot of Crypto Prices'
}

#Plot text into dashboard (useful for Krista's news data or word cloud)
box_b = {
    'type': 'box',
    'boxType': 'text',
    'text': 'Crypto Baby',
    'title': 'Markdown Options for Text Box'
}

#Plot into the second File ID, test to see if dashboard works
box_c = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': 'fileId_2',
    'title': 'box-for-dashboard',
}

#Insert the boxes
my_dboard.insert(box_a)

#insert a box above
my_dboard.insert(box_b, 'above', 1)

#insert a box beside
my_dboard.insert(box_c, 'left', 2)

#Box title
my_dboard['settings']['title'] = 'Cryptobase Title'

