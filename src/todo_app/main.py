from fastapi import FastAPI
from todo_app.database import Base, engine
from todo_app.routers.auth import router as auth_router
from todo_app.routers.todos import router as todos_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Authentication routes include karna
app.include_router(auth_router)

# Todos routes include karna
app.include_router(todos_router, prefix="/todos")

@app.get("/")
def home():
    return {"message": "Todo API chal rahi hai"} 