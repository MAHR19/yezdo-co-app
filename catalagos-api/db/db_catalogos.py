#####-----      IMPORTS     -----#####

from sqlalchemy.orm.session import Session
#####-----  IMPORTING ALL MODELS-----#####
from db.models import * 
#from pdb import set_trace

#####-----  query to database -----#####


###### USED FOR LONG CATALOGS #####
def get_catalog_query(db:Session, filter:str, Model):
    items = db.query(Model).filter(Model.name.contains(filter.capitalize()))[:10]
    return [item for item in items]


###### USED FOR SHORT CATALOGS #####
def get_full_catalog(db:Session, Model):
    items = db.query(Model).all()
    return [item for item in items]