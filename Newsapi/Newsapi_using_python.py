from turtle import title
from newsapi import NewsApiClient

# Initalize newsapi instance
newsapi = NewsApiClient(api_key='cc6eb629c73c476b8c0e2ab37f879c16')

# Function to fetch latest news based on the title and category provided in the terminal input 
def fetch_lnews(title,category):
    top_headlines = newsapi.get_top_headlines(q=title, category=category,language='en',country='in')
    print(f"Here are top 5 latest news {category} category...")
    
    for i in range(top_headlines["totalResults"]):
        news=str(top_headlines["articles"][i]["title"])+" : "+str(top_headlines["articles"][i]["content"])
        print(f"News {i+1}\n{news}")
        if i==4:
            break

# Input to get parameters for the fetch_lnews function
cat = input("Enter category you want ( business,entertainment,general,health,science,sports,technology ) :")
title=input("Enter the topic : ")
fetch_lnews(title,cat)
