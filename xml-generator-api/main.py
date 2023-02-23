from fastapi import FastAPI
from xml_generator.main import GenereDocument


app = FastAPI()


@app.get('/')
def root():
    return {'hello'}


@app.post('/genera')
def generate_doc():
    response = GenereDocument.selectdoc('fe')
    return { 'xml' : response}