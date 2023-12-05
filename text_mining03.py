# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 08:57:38 2023

@author: SHRI
"""

from bs4 import BeautifulSoup as bs
import requests
link='https://www.flipkart.com/msi-gf63-intel-core-i7-11th-gen-11800h-16-gb-1-tb-hdd-256-gb-ssd-windows-11-home-4-graphics-nvidia-geforce-rtx-3050-144-hz-thin-11uc-1294in-gaming-laptop/p/itm1692c348d09ef?pid=COMGZ4PNC67EXXDH&lid=LSTCOMGZ4PNC67EXXDHCUPWJM&marketplace=FLIPKART&store=6bo%2Fb5g&srno=b_1_1&otracker=browse&fm=organic&iid=en_oZhD68mKPKov75xiOFFRLgWnV8ROaWY3KTq4JzVE55m2pYYq2-F90tPzs2GNWobkPpbNr5JG12jqzA30APbBCw%3D%3D&ppt=hp&ppn=homepage&ssid=8a5tywg8qo0000001701746949003'
page=requests.get(link)
page
page.content
soup=bs(page.content,'html.parser')
print(soup.prettify())
title=soup.find_all('p', class_='_2-N8zT')
title
review_title=[]
for i in range(0,len(title)):
    review_title.append(title[i].get_text())
review_title

len(review_title)
##we got 10 review titles

## Now lets us scrap rating
rating=soup.find_all('div',class_='_3LWZlK _1BLPMq')
rating
rate=[]

for i in range(0,len(rating)):
    rate.append(rating[i].get_text())
rate
len(rate)
rate.append('')

len(rate)


##Now let us scarp the review body

review=soup.find_all('div',class_='t-ZTky')
review

review_body=[]
for i in range(0, len(review)):
    review_body.append(review[i].get_text())

review_body
len(review_body)

#we got 10 review body
#now we have to save the data in ,csv file

import pandas as pd
df=pd.DataFrame()
df['Review_Title']=review_title
df['rate']=rating
df['Review_body']=review_body
df
 


#to create .csv file 
df.to_csv('flipkart_review.csv',index=True)

#sentiment analysis
import pandas as pd
from textblob import TextBlob
sent="This is very excellent garden"

pol=TextBlob(sent).sentiment.polarity
pol
df=pd.read_csv('flipkart_reviews.csv')
df.head()
df['polarity']=df['Review'].apply(lambda x:TextBlob(str(x)).sentiment.polarity)
df['polarity']

