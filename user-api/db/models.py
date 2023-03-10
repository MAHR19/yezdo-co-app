from db.database import Base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String

class User_Data(Base):
    __table_name__ = 'users_db',
    id_user = Column(Integer,primary_key =True, index=True),
    mail = Column(String),
    password = Column(String)