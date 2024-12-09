from fastapi import APIRouter
# file import 
import routers.v1.users as userRouters

# content import
from routers.v1.users import router as userRouters

routerV1 = APIRouter() #( prefix='/v1')#path in api end with /v1. so, use below routes


routerV1.include_router(userRouters,prefix="/users",tags=["users"])# prefix = say after current router prefix if next path is /users then call userRouters router methods 

# if i include prefix while APIRouter then it must have that prefix in path
# APIRouter() prefix is also add in path and app.include_router() prefix is also add in path, both are optional
'''
eg: app.include_router(userRouters.router,prefix="/api/v1")
and index.py files ma:
APIRouter(prefix="/v1")


end path is /api/v1/v1
'''