from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/")
async def home():
    await asyncio.sleep(3)
    return {"message": "Asynchronous Programming in FastAPI"}