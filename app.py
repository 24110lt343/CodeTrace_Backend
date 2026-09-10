from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from database.database import Base,engine
from models.UserModel import UserModel
from routes.auth import router as auth_router
Base.metadata.create_all(bind=engine)

# Initializing fastAPI Backend
app = FastAPI()
# Handling api routes
app.include_router(auth_router)


# API 

@app.get("/")
def home():
    return {"msg":"Working fine"}