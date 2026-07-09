from fastapi import FastAPI,HTTPException
import requests
from bs4 import BeautifulSoup
import time

app=FastAPI()

# cache storage

cache_data=[]
last_fetch=0


@app.get("/news")
def get_news():
    global cache_data,last_fetch

    start=time.time()
    if time.time() - last_fetch>60:
        print("Fetching fresh data")
        url="https://news.ycombinator.com/"  # website from where wewill crawl/get/fetch data

        response=requests.get(url) # fetching data and saving in response variable
        soup=BeautifulSoup(response.text,"html.parser")
        cache_data=[
            item.text for item in soup.find_all("span",class_="titleline")
        ]

        last_fetch=time.time()
    else:
        print("Using cached data")
    
    end=time.time()
    time_taken=round(end-start,4)
    print("Time Taken: ",time_taken)

    return {
        "time_taken":time_taken,
        "data":cache_data[:5]
    }