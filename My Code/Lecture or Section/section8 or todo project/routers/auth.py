from fastapi import APIRouter,HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer
from starlette import status
from pydantic import BaseModel,Field
from models import User
from sqlalchemy.orm import Session
from typing import Annotated
from database import LocalSession
from passlib.context import CryptContext
from jose import jwt,JWTError
from datetime import datetime, timedelta,timezone

router = APIRouter(
    prefix="/auth",#api start from /auth
    tags=["auth section"],#section name at swagger
)

# jwt secret and algo 

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"

oAuth_bearer = OAuth2PasswordBearer(tokenUrl="auth/authenticate-user")#api url path pass here

# create password context
bycrpt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

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



#  create pydantic request model for auth
class AuthRequest(BaseModel):
    name: str=Field(min_length=3)
    email: str=Field(min_length=3)
    password: str=Field(min_length=3)
    role: str=Field(min_length=3)
    mobile: str


@router.post("/authorize",status_code=status.HTTP_201_CREATED)
async def sign_un(db:db_dependency,user_req:AuthRequest):

    new_user = User(
        email=user_req.email,
        name=user_req.name,
         hash_password=bycrpt_context.hash(user_req.password),
        role=user_req.role,
        mobile=user_req.mobile,
        is_active=True
      )
    print(new_user)

    # check if user exist by email
    exist = db.query(User).filter(User.email == user_req.email).first()

    print(exist)

    if exist is not None:
        raise HTTPException(status_code=409,detail=     f"user already exist with email = {exist.email}")

    # add user to database
    db.add(new_user)
    db.commit()


class SignInRequest(BaseModel):
    email: str=Field(min_length=3)
    password: str=Field(min_length=3)

# @router.post('/signin',status_code=status.HTTP_200_OK)
# async def signin(db:db_dependency,user_req:SignInRequest):
#     # check if user exist by email
#     exist = db.query(User).filter(User.email == user_req.email).first()

#     print(exist)

#     if exist is None:
#         raise HTTPException(status_code=404,detail=f"user not found with email = {user_req.email}")

#     if bycrpt_context.verify(user_req.password,exist.hash_password):
#         return exist
#     raise HTTPException(status_code=404,detail=f"incorrect password for user with email = {user_req.email}")


#use  to get current user each time when any api call that user can only use when he/she is logged in or validate if token valid or not
async def get_current_user(token: Annotated[str, Depends(oAuth_bearer)]):

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_id: int = payload.get("user_id")
        role: str = payload.get("role")
        mobile: str = payload.get("mobile")

        #validation check
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='could not validate credentials')

        return {"username": username, "user_id": user_id, "role": role}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='could not validate credentials')

# pydantic response
class TokenResponse(BaseModel):
    access_token: str
    token_type: str

@router.post('/authenticate-user',response_model=TokenResponse,status_code=status.HTTP_200_OK)
async def signIn(form_data:Annotated[OAuth2PasswordRequestForm,Depends()], db:db_dependency):

    is_user = validate_user_signin_details(form_data.username, form_data.password, db)

    if not is_user:
        raise HTTPException(status_code=404,detail="Incorrect username or password")
    
    token=generate_token(is_user.email, is_user.id,is_user.role,15)
    
    return {"access_token": token, "token_type": "bearer"}


def validate_user_signin_details(email: str, password: str, db: Session):
    user = db.query(User).filter(User.email == email).first()

    if not user:
        return False

    if not bycrpt_context.verify(password, user.hash_password):
        return False

    return user

def generate_token(username:str, user_id:int,role:str, expires_delta: int):

    payload = {
        "sub":username,
        "username":username,
        "user_id":user_id,
       
    }
    expire= datetime.now(timezone.utc) + timedelta(minutes=expires_delta)

    payload.update({"exp":expire})

    return jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)



