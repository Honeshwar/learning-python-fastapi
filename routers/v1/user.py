from fastapi import APIRouter,status,Depends
from pydantics.user import CreateUserRequest
from config.database import CreateLocalSessionInstance
from typing import Annotated
from models.users import User


router = APIRouter(prefix="/user",tags=['user'])

'''
What yield does:
Creates a generator:
The yield keyword transforms the get_db function into a generator function. Instead of returning a single value and terminating, a generator can produce a series of values over time.
Pauses execution:
When the yield statement is reached, the function's execution is paused, and the yielded value is returned. The function's state is preserved, allowing it to resume from where it left off the next time it's called.
'''
def get_db():
   db = CreateLocalSessionInstance()
   try:
       yield db
   finally:
       db.close()
#    injection create
db_dependency = Annotated[CreateLocalSessionInstance, Depends(get_db)]

# using that instance create routes and defines its actions
@router.get('/root')
def root():
    return {"root":"success"}

@router.post('/',status_code=status.HTTP_201_CREATED)
def create_user(db:db_dependency,userReq:CreateUserRequest):
    print(userReq)
    print(db.query(User).all())

    if db.query(User).filter(User.mobile == userReq.mobile).first():
        return {"message":"user already exist"}
    

    user = User(**userReq.model_dump())#user class constructor dump data
    db.add(user)
    db.commit()
    return {"message":"user created"}

@router.get('/')
def get_users(db:db_dependency):
    return db.query(User).all()