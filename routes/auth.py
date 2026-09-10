from fastapi import APIRouter,Depends
from database.database import getDB
from sqlalchemy.orm import Session
from controllers.auth.LoginController import LoginHandler 
from controllers.auth.SignupController import RegisterHandler 
router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

router.add_api_route("/login",LoginHandler,methods=["GET"])

router.add_api_route("/register",RegisterHandler,methods=["POST"])
