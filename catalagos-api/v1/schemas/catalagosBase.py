#####----- RESPONSE MODEL -----#####
from pydantic import BaseModel

 #Allows to return data as we defined above
 
class ProductoDisplay(BaseModel):
    name:str
    descripcion:str
    um:str
    precio_u:str

    class Config():
        orm_mode = True


class catalogoDisplay(BaseModel):
    code : str
    name : str
    description: str|None 
    class Config():
        orm_mode = True

        
class catalogoCP(BaseModel):
    codigo_departamento:str
    nombre_departamento:str
    codigo_municipio:str
    nombre_municipio:str
    name:str
    tipo:str

    class Config():
        orm_mode = True 