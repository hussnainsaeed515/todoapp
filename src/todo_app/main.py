from fastapi import FastAPI
from todo_app.database import Base, engine
from todo_app import models
from todo_app.routers.auth import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Authentication routes include karna
app.include_router(auth_router)

@app.get("/")
def home():
    return {"message": "Todo API chal rahi hai"} 