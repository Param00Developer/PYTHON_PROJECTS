from turtle import title
from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='cc6eb629c73c476b8c0e2ab37f879c16')

def fetch_lnews(title,category):
    top_headlines = newsapi.get_top_headlines(q=title, category=category,language='en',country='in')
    print(f"Here are top 5 latest news {category} category...")
    
    for i in range(top_headlines["totalResults"]):
        news=str(top_headlines["articles"][i]["title"])+" : "+str(top_headlines["articles"][i]["content"])
        print(f"News {i+1}\n{news}")
        if i==4:
            break

cat = input("Enter category you want ( business,entertainment,general,health,science,sports,technology ) :")
title=input("Enter the topic : ")
fetch_lnews(title,cat)
# /v2/everything
# all_articles = newsapi.get_everything(q='bitcoin',
#                                       sources='bbc-news,the-verge',
#                                       domains='bbc.co.uk,techcrunch.com',
#                                       from_param='2017-12-01',
#                                       to='2017-12-12',
#                                       language='en',
#                                       sort_by='relevancy',
#                                       page=2)

# /v2/top-headlines/sources
# sources = newsapi.get_sources()