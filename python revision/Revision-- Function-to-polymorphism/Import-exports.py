
from Imports import students
from Imports import returnDictionary
for student in students:
    print(student)


# two way to import file,
#1. import files from folder (new python files also we can import)
#2. import files content methods, obj,.. directly from file
from routers.v1.index import  routerV1
# from routers.v1 import  index