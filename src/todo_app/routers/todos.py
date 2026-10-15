from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from todo_app import models, schemas
from todo_app.dependencies import get_db, get_current_user

router = APIRouter(tags=["Todos"])


# My Todos Route - logged-in user sirf apne todos dekh sakta hai
@router.get("/", response_model=list[schemas.TodoResponse], status_code=status.HTTP_200_OK)
def get_my_todos(
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Logged-in user ke apne saare todos return karta hai.
    Sirf wohi todos aayenge jinke user_id current user ke id se match kare.
    """
    todos = db.query(models.Todo).filter(models.Todo.user_id == current_user.id).all()
    return todos


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


# Todo Update Route - user apna todo update kar sakta hai
@router.put("/{todo_id}", response_model=schemas.TodoResponse, status_code=status.HTTP_200_OK)
def update_todo(
    todo_id: int,
    todo_data: schemas.TodoUpdate,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Todo update karta hai (title, description, ya is_done status).
    Sirf wahi user update kar sakta hai jiska yeh todo hai.
    """
    todo = (
        db.query(models.Todo)
        .filter(models.Todo.id == todo_id, models.Todo.user_id == current_user.id)
        .first()
    )

    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo nahi mila!",
        )

    # Sirf wahi fields update karna jo request mein pass ki gayi hon
    update_data = todo_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(todo, field, value)

    db.commit()
    db.refresh(todo)

    return todo


# Todo Delete Route - user sirf apna todo delete kar sakta hai
@router.delete("/{todo_id}", status_code=status.HTTP_200_OK)
def delete_todo(
    todo_id: int,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Todo delete karta hai.
    Sirf wahi user delete kar sakta hai jiska yeh todo hai.
    """
    todo = (
        db.query(models.Todo)
        .filter(models.Todo.id == todo_id, models.Todo.user_id == current_user.id)
        .first()
    )

    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo nahi mila!",
        )

    db.delete(todo)
    db.commit()

    return {"message": "Todo kamyabi se delete ho gaya!"}

