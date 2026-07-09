from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from config import settings
app = FastAPI()


# all allowed origin (front-end)
origin =settings.ORIGINS # using 'ORIGINS' value from .env file

app.add_middleware(
    CORSMiddleware,
    allow_origins=origin, # frontend 
    allow_credentials=True,
    allow_methods=["*"], # '*' means to allow for all CURD Operations
    allow_headers=["*"] 
)

@app.get("/")  # this api (in backend) will bw accessed by frontend
def home():
    return {
        "message":"CORS ENABLED API"
    }