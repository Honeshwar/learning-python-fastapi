# import FastAPI from fastapi
from fastapi import FastAPI

# create an instance of fastapi application
app = FastAPI()

# using app.get decorator to define a get route
@app.get('/')
async def get_books():
    return {"message": "Hello, FastAPI!"}

print('hi')