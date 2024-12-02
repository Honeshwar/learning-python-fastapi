# Making Python FastAPI
Install python on your system: that give you python, pip, venv ,..
versions: Python 3.12.7, pip     24.2
## Step1 create an environment
```
- create an environment: python -m venv foldername
- run this environment : foldername\Scripts\activate.bat hit enter
- now environment is running, 

```

## Step2 dependencies installation
```
- pip install "uvicorn[standard]" Fastapi sqlalchemy
or 
pip install -r requirement.txt // if you have dependencies files


pip freeze > requirements.txt
```

## Folder Structure 
```
core
db - models , sqlQueries
routers
services

db - database relate files like models(table schemas), connections, sql queries,...
routers - that having all routing files with actions
services - this contain all files of services we use like jwt, crypto, send otp, authentication, file uploads 
core - basic setup like dotenv, error handling classes custom, that we want to run on initialization of application


```