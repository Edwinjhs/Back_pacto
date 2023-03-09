from fastapi import APIRouter,Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder

from fastapi.security import HTTPBearer
from config.user import Session


from service.user import UserService as userService
from schemas.user import User as userSchema

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

user_router = APIRouter()

engine = create_engine("sqlite:///user.sqlite")
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


#@app.get('/user',tags=['user'],response_model=List[user],status_code=200, dependencies=[Depends(JWYBearer())])

@user_router.get('/user',tags=['user'],response_model=List[userSchema],status_code=200)
def get_user() -> user_router:
    db = Session()
    result = userService(db).get_users()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)



@user_router.post('/user',tags=['user'],status_code=201,response_model=dict)
def create_user(user:userSchema)->dict:
    db = Session()
    userService(db).create_user(user)
    return JSONResponse(content={"message":"Se ha registrado un user","status_code":201})


@user_router.put('/user/{id}',tags=['user'])
def update_user(id:int,user:userSchema):
    db =  Session()
    result = userService(db).update_user(id, user)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado ningun user","status_code":"404"})
    userService(db).update_user(id,user)
    return JSONResponse(content={"message":"Se ha modificado el user con id: {id}"})



@user_router.delete('/user/{id}',tags=['user'])
def delete_user(id:int):
        db = Session()
        success = userService(db).delete_user(id)
        if success:
            return JSONResponse(status_code=202,content={"message":"Delete user"})
        else:
            return JSONResponse(content="user not found", status_code=404)
    