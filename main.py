from fastapi import FastAPI, HTTPException

app = FastAPI()
@app.get("/")
def home():
    return{
        "message":"Hello Fatima"
    }
@app.get("/add")
def add(a:int,b:int):
    return{
        "result":a+b
    }
