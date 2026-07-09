from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware import CORSMiddleware

app = FastAPI()

# all allowed origin (front-end)
origin =[
    "http://localhost:5173" # front end url
]

app.add_middleware(
    
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