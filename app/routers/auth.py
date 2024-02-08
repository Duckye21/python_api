# pkg import
from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session

# Local imports
from .. import models, schemas, utils
from ..database import get_db


router = APIRouter(prefix="/login", tags=["users"])


@router.post("/", status_code=status.HTTP_200_OK)
def login(user_credentials: schemas.UserLogin, db: Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.email == user_credentials.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
    if not utils.verify_password(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
    
    return {"token": "token"}
    