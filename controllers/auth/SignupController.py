from database.database import getDB
from fastapi import Depends,Request
from sqlalchemy.orm import Session
from pydantic import BaseModel,Field,EmailStr
from fastapi.responses import JSONResponse
from pwdlib import PasswordHash
from models.UserModel import UserModel

password_hash = PasswordHash.recommended()


class RegisterationModel(BaseModel):
    name:str = Field(description="Full name of the user.")
    email:EmailStr = Field(description="Correct and valid email address of the user.")
    password:str = Field(description="Password of the user",min_length=8)

def RegisterHandler(data:RegisterationModel,db:Session = Depends(getDB)):
    check = db.query(UserModel).filter(UserModel.email == data.email).all();
    if(len(check) == 0):
        user_data = UserModel(name=data.name,email=data.email,password=password_hash.hash(data.password))
        try:
            db.add(user_data)
            db.commit()
            db.refresh(user_data)
        finally:
            return JSONResponse({"success":True,"msg":"User created successfully"})
    else:
        return JSONResponse({
            "msg":"User already exists with this information",
            "success:":False
        })                                           
