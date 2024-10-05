from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from config import database  # Import from config folder
from model import models     # Import models from model folder

#create an instance of FastAPI, server also start this code
app = FastAPI()

# Create the database tables if they don't exist
models.Base.metadata.create_all(bind=database.engine)

print("hi")

# create route
@app.get("/")
def get_route():
    return {
        "message":"hi i send json by default"
    }

@app.get("/user/{user_id}")
def user(user_id:int=None,q:str=None):
    return{
        "userId":user_id,
        "query":q
    }

# Custom handler for 404 errors
@app.exception_handler(StarletteHTTPException)
async def custom_404_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        return JSONResponse(
            status_code=404,
            content={"message": "This endpoint does not exist. Please check the URL."},
        )
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )
