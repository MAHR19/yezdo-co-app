from fastapi import APIRouter
from fastapi.security.oauth2 import OAuth2AuthorizationCodeBearer
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from db.database import get_db


router = APIRouter(
    tags=['auth']
)

@router.get('/token')
def get_token(request: OAuth2AuthorizationCodeBearer, db:Session = Depends(get_db)):
    pass
