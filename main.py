from fastapi import FastAPI
from db.database import Base,engine

app = FastAPI()

# connect once and create all tables in the database
Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Hello World"}