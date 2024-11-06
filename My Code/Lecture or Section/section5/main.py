# import FastAPI from fastapi
from fastapi import FastAPI
from fastapi import Body

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
@app.get('/{id}/{i}')
async def get_books(id,i,a: str,b: str):#we need this all parameters in api otherwise it will throw error field error
    print(id)
    return {"message": f"Hello, FastAPI! {id} {i} {a} {b}"}

@app.post('/')
def add_book(newBook=Body()):#if i don't specify the type of parameter it will consider newBook as query parameter and throw error not pass in api
    #=Body() also restrict api to pass body
    #default argument always be the last argument in function
    return {"message": newBook,"j":a}

@app.put('/update')
def update_book(newBook=Body()):
    for i in range(len(Books)):
        book = Books[i]
        if(book['id'] == newBook['id']):
            Books[i] = newBook
    return Books

@app.delete('/delete/{id}')
def delete_book(id:int):
    for i in range(len(Books)):
        book = Books[i]
        if(book['id'] == id):
            del Books[i]
            break
    return Books

print('SSShi'.casefold())