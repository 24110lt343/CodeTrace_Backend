from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from database.database import Base,engine
from models.UserModel import UserModel
from routes.auth import router as auth_router
from dotenv import load_dotenv
Base.metadata.create_all(bind=engine)
load_dotenv()
# Initializing fastAPI Backend
app = FastAPI()
# Handling api routes
app.include_router(auth_router)


# API 

@app.get("/")
def home():
    return {"msg":"Working fine"}