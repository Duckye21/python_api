from fastapi import Depends, HTTPException, Response, status, APIRouter
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import SessionLocal, get_db


router = APIRouter(prefix="/posts", tags=["posts"])


@router.get("/")
def get_post(db: SessionLocal = Depends(get_db)):
    posts = db.query(models.Posts).all()
    return {"message": posts}


@router.get("/{id}")
def get_post_by_id(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Posts).filter(models.Posts.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} was not found")
    return {"message": post}


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_post(post: schemas.Posts, db: Session = Depends(get_db)):
    new_post = models.Posts(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"message": new_post}


@router.put("/{id}")
def update_post(id: int, updated_post: schemas.Posts, db: Session = Depends(get_db)):
    query_post = db.query(models.Posts).filter(models.Posts.id == id)
    if query_post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} was not found")
    
    query_post.update(updated_post.model_dump(), synchronize_session=False)
    db.commit()
    return {"message": query_post.first()}


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Posts).filter(models.Posts.id == id)
    if post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} was not found")
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
