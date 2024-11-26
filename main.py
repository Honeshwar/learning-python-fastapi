# import FastAPI application from fastapi 
from fastapi import FastAPI

import models
from config.database import engine,Base

from routers.v1 import index,user

# create an instance of fastapi application
app = FastAPI()

# models.Base.metadata.create_all(bind=engine)

# using base obj to create table using models with help of base obj instance and engine
Base.metadata.create_all(bind=engine)

app.include_router(index.router,prefix='/api')

# # using that instance create routes and defines its actions
# @app.get('/')
# def root():
#     return {"root":"success"}