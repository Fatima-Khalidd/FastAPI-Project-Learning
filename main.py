from fastapi import FastAPI, Depends, HTTPException, Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse

app = FastAPI()

#limiter set up
limiter=Limiter(key_func=get_remote_address)
app.state.limiter=limiter


# error handler
@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request:Request,exc:RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={
            "detail":"Too Many requests"
        }

    )
        
# rate limiter api
@app.get("/data")
@limiter.limit("5/minute")

def get_data(request:Request):
    return {
        "message":"Sucess"
    }
    


