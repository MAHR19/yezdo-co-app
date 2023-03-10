from pydantic import BaseModel

class UserSignIn(BaseModel):
    username: str
    email:str
    password:str

class LogIn(BaseModel):
    email:str
    password:str