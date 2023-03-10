from fastapi import FastAPI
import os


app = FastAPI()

#DB_HOST = os.environ.get('DB_HOST')
#DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('POSTGRES_USER')
DB_PASSWORD = os.environ.get('POSTGRES_PASSWORD')


@app.get('/')
def isworking():
    return {'pass': DB_PASSWORD,
            'user' : DB_USER
            }