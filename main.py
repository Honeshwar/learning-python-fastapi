from fastapi import FastAPI
from db.database import Base,engine,get_db  
from sqlalchemy.orm import Session
from fastapi import Depends
from typing import Annotated
from db.pydantics.users import AddTeamLeader

app = FastAPI()

# connect once and create all tables in the database
Base.metadata.create_all(bind=engine)


db_injection = Annotated[ Session, Depends(get_db)]
@app.post("/")
async def root(db: db_injection, AddLeaderReq: AddTeamLeader):
    # items = db.execute("SELECT * FROM items").fetchall()
    return {"message": "Hello World", "items": AddLeaderReq}