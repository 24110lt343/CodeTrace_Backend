from database.database import getDB
from fastapi import Depends,HTTPException
from jose import jwt
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from helper.jwtTokenGenerator import jwtGenerator
from pydantic import BaseModel,EmailStr
from models.UserModel import UserModel
from pwdlib import PasswordHash

passHash = PasswordHash.recommended()

class LoginDataFormat(BaseModel):
    email:EmailStr
    password:str

def LoginHandler(data:LoginDataFormat,db:Session = Depends(getDB)):
    try:
        data.password
        check_existence = db.query(UserModel).filter(UserModel.email == data.email).first()
        if check_existence:
            check_password = passHash.verify(data.password,check_existence.password)
            if(check_password):

                token = jwtGenerator({
                    "email":check_existence.email,
                })

                return JSONResponse({
                    "msg":"Login Successfull.",
                    "token":token,
                    "success":True
                })
            
            else:
                return HTTPException(status_code=401,detail="Invalid login credentials.")
        else:
            return JSONResponse({
                "msg":"User doesn't exists with these credentials.",
                "success":False
            })
    except:
        return HTTPException(status_code=501,detail="Internal server error while performing login.")

   

