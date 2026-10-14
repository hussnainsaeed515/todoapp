from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from todo_app import models, schemas
from todo_app.dependencies import get_db, get_current_user

router = APIRouter(tags=["Todos"])


# Todo Create Route - sirf logged-in / registered user hi todo bana sakta hai
@router.post("/todocreate", response_model=schemas.TodoResponse, status_code=status.HTTP_201_CREATED)
def todocreate(
    todo_data: schemas.TodoCreate,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Naya todo create karta hai.
    Sirf wahi user todo bana sakta hai jo login ya registered hai (valid token chahiye).
    """
    new_todo = models.Todo(
        title=todo_data.title,
        description=todo_data.description,
        user_id=current_user.id,
    )
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)

    return new_todo
