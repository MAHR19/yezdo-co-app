from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
#from pydantic import BaseModel
from db import models
from db.database import engine
from v1.router import catalogos_get


app = FastAPI()
app.include_router(catalogos_get.router)
models.Base.metadata.create_all(engine)

origins = [
    'http://localhost:3000',
    'http://172.16.103.79:3000/'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)