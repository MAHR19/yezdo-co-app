from fastapi import APIRouter


router = APIRouter(
    prefix= '/user',
    tags=['user']
)


@router.post('/signin')
def adduser():
    pass