from fastapi import APIRouter
from fastapi import  Depends,Path,Query,HTTPException,Body
 
from models import Todos
from typing import Annotated
from sqlalchemy.orm import Session
from database import   LocalSession
from starlette import status

from pydantic import BaseModel, Field
 

 
router = APIRouter()


# create db session

def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()

# create dependency injection
db_dependency = Annotated[Session, Depends(get_db)]#Depends = t takes a single "dependable" callable (like a function).
# Don't call it directly, FastAPI will call it for you 
# mostly use to get db before calling route controller


# create a route
@router.get('/',status_code=status.HTTP_200_OK)
async def get_all_todos(db: db_dependency):#python fastapi pass sb at here after calling get_db
    return db.query(Todos).all()



@router.get("/{todo_id}",status_code=status.HTTP_200_OK)
def get_todo_by_id(db:db_dependency, todo_id:int=Path(gt=0)):
    # try:
        todo = db.query(Todos).filter(Todos.id == todo_id).first()#here we are telling sqlalchemy that take/return first row that matches this condition

        if todo is not None:
            return todo
        
        raise HTTPException(status_code=404,detail='no todo found by this id')
    # except Exception as e:
    #     print(e)
    #     raise HTTPException(status_code=500, detail='internal server error')


# pydantic req
class TodoRequest(BaseModel):
    title:str=Field(min_length=3)
    description:str=Field(min_length=3, max_length=200)
    priority:int=Field(gt=0,lt=6)
    completed:bool=False

@router.post('/create_todo',status_code=status.HTTP_201_CREATED)
async def create_todo(db:db_dependency,todoReq:TodoRequest):
     print(todoReq)

     todo = Todos(**todoReq.model_dump())
     print(todo)

     db.add(todo)
     db.commit()#commit transition


@router.patch('/update_todo/{todo_id}',status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(db:db_dependency,todoReq:TodoRequest,todo_id:int=Path(lt=0)):
     print(todoReq)

     existing_todo = db.query(Todos).filter(Todos.id == todo_id).first()     
     print(todo)

     if existing_todo is None:
          raise HTTPException(status_code=404,detail="id not exist")
     
     existing_todo.title = todoReq.title
     existing_todo.description = todoReq.description
     existing_todo.priority = todoReq.priority
     existing_todo.completed = todoReq.completed

     db.add(existing_todo)
     db.commit()#commit transition



@router.delete('/delete_todo/{todo_id}',status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db:db_dependency,todoReq:TodoRequest,todo_id:int=Path(lt=0)):
     print(todoReq)

     existing_todo = db.query(Todos).filter(Todos.id == todo_id).first()     
     print(todo)

     if existing_todo is None:
          raise HTTPException(status_code=404,detail="id not exist")
     
     db.query(Todos).filter(Todos.id == todo_id).delete() 
     db.commit()#commit transition