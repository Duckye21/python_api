# pkg import
from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session

# Local imports
from .. import models, schemas, utils
from ..database import get_db


router = APIRouter(prefix="/users", tags=["users"])


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.UserResponse)
def get_users(id: int, db: Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.id == id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} was not found")
    return user


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
def create_user(user: schemas.Users, db: Session = Depends(get_db)):
    user.password = utils.hash_password(user.password)
    if db.query(models.Users).filter(models.Users.email == user.email).first() is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Email already exist")
    new_user = models.Users(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

