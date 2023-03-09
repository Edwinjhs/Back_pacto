from sqlalchemy import Column, ForeignKey ,Integer, String, Float,Date, Boolean
from sqlalchemy.orm import relationship

from config.user import Base

from sqlalchemy.ext.declarative import declarative_base

class User(Base):

    __tablename__ = "user"

    id= Column(Integer,primary_key=True, index=True)
    name= Column(String)
    lastname= Column(String)
    email= Column(String)
    username= Column(String)
    password= Column(String)
    cohabitation_agreement= Column(Boolean)
    status= Column(Integer, index=True)
    description= Column(String)
    knowledge_interest= Column(String)
    create_at= Column(Date)
    update_at= Column(Date)
    forgot_password= Column(Boolean)
    image_profile=  Column(String)
    phone_number= Column(String)







