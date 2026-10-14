from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from todo_app import models, schemas
from todo_app.dependencies import get_db
from todo_app.security import hash_password, verify_password, create_access_token

router = APIRouter(tags=["Authentication"])


# 1. Signup Endpoint (Naya user create karna aur foran token return karna)
@router.post("/signup", response_model=schemas.Token, status_code=status.HTTP_201_CREATED)
def signup(user_data: schemas.UserCreate, db: Session = Depends(get_db)):
    # Check karein ke email pehle se registered to nahi
    existing_user = db.query(models.User).filter(models.User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Yeh email pehle se registered hai!"
        )

    # Password hash karna
    hashed_pwd = hash_password(user_data.password)

    # Naya user database me add karna
    new_user = models.User(
        name=user_data.name,
        email=user_data.email,
        hashed_password=hashed_pwd
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Signup ke baad foran naya token bana kar return karna
    access_token = create_access_token(data={"sub": new_user.email})
    return {"access_token": access_token, "token_type": "bearer"}


# 2. Login Endpoint (Credentials verify kar ke naya token lena)
@router.post("/login", response_model=schemas.Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    # Email aur password dono ek saath verify karna
    user = db.query(models.User).filter(models.User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ghalat email ya password!"
        )

    # 3. Dono verify hone par naya token generate karna
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
