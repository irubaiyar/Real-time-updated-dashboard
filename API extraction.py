# API key: 1d656ac0916147bf8d28e1dcda71266a

import requests
import pprint
import json
pp = pprint.PrettyPrinter()
import numpy as np


#just get headlines
coinsHeadlinesURL = requests.get("https://newsapi.org/v2/top-headlines?sources=crypto-coins-news&apiKey=1d656ac0916147bf8d28e1dcda71266a")

coinsHeadlines = coinsHeadlinesURL.json()

#pp.pprint(coinsHeadlines)


#get all of the news
coinsNewsURL = requests.get("https://newsapi.org/v2/everything?sources=crypto-coins-news&apiKey=1d656ac0916147bf8d28e1dcda71266a")

coinsNews = coinsNewsURL.json() # this is a dictionary
#keys are: [u'status', u'articles', u'totalResults']

articles = coinsNews['articles']
keys = articles[0].keys() #[u'description',u'title', u'url', u'author', u'publishedAt', u'source', u'urlToImage']

articlesList = []
for i in range(0,len(articles)):
	article = []
	for j in range(0, 5):
		article.append(articles[i][keys[j]])
		#print i, j, article
	articlesList.append(article)
	#print i, articlesList

articlesList = np.array(articlesList)
description = list(articlesList[:,0])
title = list(articlesList[:,1])
url = list(articlesList[:,2])
author = list(articlesList[:,3])
published = list(articlesList[:,4])
