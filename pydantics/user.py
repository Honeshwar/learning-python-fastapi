from pydantic import BaseModel,Field

class CreateUserRequest(BaseModel):
    name:str=Field(min_length=3,max_length=50)
    mobile:str=Field(min_length=10,max_length=10)

    model_config={
        "json_schema_extra":{
            "examples":[
                {
                    "name":"test",
                    "mobile":"1234567890"
                }
            ]
        }
    }