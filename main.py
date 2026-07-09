from fastapi import FastAPI,HTTPException
import requests
from bs4 import BeautifulSoup

app=FastAPI()

@app.get("/news")
def get_news(page:int =1,limit:int=5 ):
    url="https://news.ycombinator.com/"  # website from where wewill crawl/get/fetch data
    response=requests.get(url) # fetching data and saving in response variable
    soup=BeautifulSoup(response.text,"html.parser")
    title=[]
    for item in soup.find_all("span",class_="titeLine"):
        title.append(item.text)
    
    #pagination logic
    start=(page-1) * limit
    end=start+limit
    return {
        "Page":page,
        "limit":limit,
        "lenght":len(title),
        "data":title[start:end]
    }