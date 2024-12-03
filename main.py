from fastapi import FastAPI
from db.database import Base,engine,get_db  
from sqlalchemy.orm import Session
from fastapi import Depends
from typing import Annotated

app = FastAPI()

# connect once and create all tables in the database
Base.metadata.create_all(bind=engine)


db_injection = Annotated[ Session, Depends(get_db)]
@app.get("/")
async def root(db: db_injection):
    items = db.execute("SELECT * FROM items").fetchall()
    return {"message": "Hello World", "items": items}