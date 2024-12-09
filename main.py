from fastapi import FastAPI
from db.database import engine
from db.base_class import Base #Custom declarative class


# two way to import file,
#1. import files from folder (new,  python ma files also we can import)
#2. import files content methods, obj,.. directly from file
from routers.v1.index import  routerV1
# from routers.v1 import  index

app = FastAPI()

# connect once and create all tables in the database
Base.metadata.create_all(bind=engine)

# include routes
# app.include_router(userRouters.router,prefix="/api/v1")
app.include_router(routerV1,prefix="/api/v1")#this prefix add before routerV1 prefix (if defined in routerV1=APIRouter(prefix="/v1"))

# db_injection = Annotated[ Session, Depends(get_db)]


# @app.post("/")
# async def root(db: db_injection, AddLeaderReq: AddTeamLeader):
#     # items = db.execute("SELECT * FROM items").fetchall()
#     return {"message": "Hello World", "items": AddLeaderReq}