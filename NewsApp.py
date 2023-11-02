# Use the NewsAPI and the requests module to fetch the daily news related to different topics. Go to: https://newsapi.org/ and explore the various options to build you application

import requests
import json

tesla=input("What type of news you interested in ?")
url=f"https://newsapi.org/v2/everything?q={tesla}&from=2023-09-07&sortBy=publishedAt&apiKey=3e571ba7e96c430990e7724a9fb930eb"
# You copy this api link inside the news api documentation
r=requests.get(url)
news=json.loads(r.text)
# print(news, type(news))
i=1
for article in news["articles"]:
    print(f"{i} no:-> ",article["title"])
    print(article["description"])
    print("--------------------------")
    i+=1