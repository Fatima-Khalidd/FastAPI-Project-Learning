"""import requests
response=requests.get("https://jsonplaceholder.typicode.com/posts/1")

data=response.json()

print(data)
print(data[:2]) """


from fastapi import FastAPI,HTTPException
import requests
from bs4 import BeautifulSoup

app=FastAPI()

@app.get("/news")
def get_news():
    url="https://indianexpress.com/"  # website from where wewill crawl/get/fetch data
    response=requests.get(url) # fetching data and saving in response variable
    soup=BeautifulSoup(response.text,"html.parser")
    title=[]
    for item in soup.find_all("a",class_="topblockNews__sidebarLink"):
        title.append(item.text)
    return {
        "News":title
    }

