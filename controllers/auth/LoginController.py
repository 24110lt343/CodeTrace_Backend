from database.database import getDB
from fastapi import Depends
from sqlalchemy.orm import Session
def LoginHandler(db:Session = Depends(getDB)):
    return {
        "msg":"Login router is working fine"
    }


def RegisterHandler(db:Session = Depends(getDB)):
    return {
        "msg":"Registeration Handler"
    }
