# import FastAPI from fastapi
from fastapi import FastAPI

# create an instance of fastapi application
app = FastAPI()

# create a list 
Books = [
    {
        "id": 1,
        "title": "The Hunger Games",
        "author": "Suzanne Collins"
    },
    {
        "id": 2,
        "title": "Harry Potter",
        "author": "J.K. Rowling"
    }
]
# using app.get decorator to define a get route
@app.get('/')
async def get_books():
    return Books
@app.get('/{id}')
async def get_books(id: int,a: str,b: str):
    print(a,b)
    return {"message": f"Hello, FastAPI! {id} {a} {b}"}

@app.post('/')
def add_book():
    return {"message": "ADD PI!"}