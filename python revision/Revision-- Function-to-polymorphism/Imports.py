'''
When you run this file/module/program where we import this students, Python will:

1. Compile this file.py into bytecode (filename.cpython-<version>.pyc).
2. Save the compiled file in the __pycache__ directory.
3.Use the compiled file for faster execution.
'''

'''
only __pycache__ directory is created when  we import custom modules that we have created

2. __pycache__ directory  will update inside file once new code is added or new export is added and we import in other module , automatically
'''

'''
Two way to do import , 
 -  project folder corresponding we import, eg from filename import when you file at outermost folder and your are inside very nested folder structure(only for file at root)

 - an folder inside files access by relative ,from foldername.file import(only for file at nested folders)
'''

students = [
    {"name": "John", "age": 20},
    {"name": "Jane", "age": 21},
    {"name": "Bob", "age": 22},
]

def returnDictionary(name: str, age: int)->dict:
    # return {name, age}# set 
    return {"name": "John", "age": age} # dictionary

