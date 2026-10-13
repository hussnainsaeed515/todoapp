from fastapi import FastAPI
from todo_app.database import Base, engine
from todo_app import models

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Todo API chal rahi hai"}