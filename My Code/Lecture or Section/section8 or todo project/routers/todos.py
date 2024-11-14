from fastapi import APIRouter
from fastapi import  Depends,Path,Query,HTTPException,Body
 
from models import Todos
from typing import Annotated
from sqlalchemy.orm import Session
from database import   LocalSession
from starlette import status

from pydantic import BaseModel, Field
from .auth import get_current_user

 
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

# create dependency injection for checking is user logged in or authenticated
user_dependency =Annotated[dict,Depends(get_current_user)]

# create a route
@router.get('/',status_code=status.HTTP_200_OK)
async def get_all_todos(user:user_dependency,db: db_dependency):#python fastapi pass sb at here after calling get_db

    if user is None:
          raise HTTPException(status_code=404,detail="user not Authenticated")
    
    todos  = db.query(Todos).filter(Todos.owner_id == user['user_id']).all()
    return todos



@router.get("/{todo_id}",status_code=status.HTTP_200_OK)
def get_todo_by_id(user:user_dependency,db:db_dependency, todo_id:int=Path(gt=0)):
    # try:

    if user is None:
          raise HTTPException(status_code=404,detail="user not Authenticated")
    
    
    todo = db.query(Todos).filter(Todos.id == todo_id).filter(Todos.owner_id == user.get['user_id']).first()#here we are telling sqlalchemy that take/return first row that matches this condition

    # if user['user_id'] != todo_id.owner_id:
    #       raise HTTPException(status_code=404,detail="Invalid todo id for this user")
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
async def create_todo(user:user_dependency,db:db_dependency,todoReq:TodoRequest):
     
     if user is None:
          raise HTTPException(status_code=404,detail="user not Authenticated")
     
     print(todoReq)

     todo = Todos(**todoReq.model_dump(),owner_id=user['user_id'])
     print(todo)

     db.add(todo)
     db.commit()#commit transition


@router.patch('/update_todo/{todo_id}',status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(user:user_dependency,db:db_dependency,todoReq:TodoRequest,todo_id:int=Path(lt=0)):
     if user is None:
          raise HTTPException(status_code=404,detail="user not Authenticated")
     

     print(todoReq)

     existing_todo = db.query(Todos).filter(Todos.id == todo_id).filter(Todos.owner_id == user['user_id']).first()     
     print(todo)

     if existing_todo is None:
          raise HTTPException(status_code=404,detail="id not exist or id not belong to this user")
     
     existing_todo.title = todoReq.title
     existing_todo.description = todoReq.description
     existing_todo.priority = todoReq.priority
     existing_todo.completed = todoReq.completed

     db.add(existing_todo)
     db.commit()#commit transition



@router.delete('/delete_todo/{todo_id}',status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(user:user_dependency,db:db_dependency,todoReq:TodoRequest,todo_id:int=Path(lt=0)):
     
     if user is None:
          raise HTTPException(status_code=404,detail="user not Authenticated")
     
     print(todoReq)

     existing_todo = db.query(Todos).filter(Todos.id == todo_id)\
        .filter(Todos.owner_id == user['user_id']).first()    #separate code in line by using \ to make it readable
     print(todo)

     if existing_todo is None:
          raise HTTPException(status_code=404,detail="id not exist or id not belong to this user")
     
     db.query(Todos).filter(Todos.id == todo_id).delete() 
     db.commit()#commit transition