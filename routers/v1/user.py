from fastapi import APIRouter
 



router = APIRouter(prefix="/user",tags=['user'])

 

# using that instance create routes and defines its actions
@router.get('/')
def root():
    return {"root":"success"}