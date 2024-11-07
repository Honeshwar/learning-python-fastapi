# import FastAPI from fastapi
from fastapi import FastAPI,Query,Path,HTTPException
from fastapi import Body
from pydantic import BaseModel,Field # while fastapi installation we get this, fastapi use it internallt
from typing import Optional
from starlette import status
# create an instance of fastapi application
app = FastAPI()


#create class for book, and also crud operations
class Book:
    # define properties or attributes
    id: int
    title: str
    author: str

    # create a constructor
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author

    # define behaviour or methods


# create pydantic model/class/object for data modeling, data parsing(coming from frontend) and data validation
class BookRequest(BaseModel):
    # define properties or attributes
    id: Optional[int]=None 
    title: str=Field(min_length=3)
    author: str=Field(min_length=1)
    # publish_date: int = Field(ge=1900, le=2022)


# create a list 
Books = [
   Book(1, "The Hunger Games", "Suzanne Collins"),
   Book(2, "Harry Potter", "J.K. Rowling"),
   Book(3,'The Lord of the Rings', 'J.R.R Tolkein')
]


@app.get('/',status_code=status.HTTP_200_OK)
def get_books():
    if(len(Books) == 0):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Books not found")
    return Books

@app.post('/create', status_code=status.HTTP_201_CREATED)
def create_book(book_request:BookRequest):#newBook is type of BookRequest
    print(type(book_request))
    new_book = Book(**book_request.model_dump())

    Books.append(new_book)
    return {
        "status":200,
        "Books":Books
        }


@app.post('/update',status_code=status.HTTP_204_ACCEPTED)
def update_book(new_book=Body()):
    findIndex = Books.index(new_book)
    if(findIndex):
        Books.pop(findIndex)
        Books.append(findIndex)
    



@app.post('/delete')#/{id} id:int=Path(gt=0)
def delete_book(id:int=Query(gt=0)):
    # findIndex = Books.index(new_book)
    # if(findIndex):
    #     Books.pop(findIndex)
    # Books.remove(new_book)
    return {
        "status":200,
        Books:Books
    }