# Python built-in modules import
# import random
import time
# pkg import
from fastapi import Depends, FastAPI, HTTPException, Response, status
from mysql.connector import connect, Error
from sqlalchemy.orm import Session
# Local imports
from . import models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

while True:
    try:
        connection = connect(host="localhost", user="root", password="firebasedb", database="firebase")
        cursor = connection.cursor()
        print("MySQL Database connection successful")
        break
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        print("Retrying in 2 seconds...")
        time.sleep(2)
        

# Get requests
@app.get("/")
def get_post(db: Session = Depends(get_db)):
    posts = db.query(models.Posts).all()
    return {"message": posts}


@app.get("/posts/{id}")
def get_post_by_id(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Posts).filter(models.Posts.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} was not found")
    return {"message": post}


# Post requests
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: schemas.Posts, db: Session = Depends(get_db)):
    new_post = models.Posts(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"message": new_post}


@app.put("/posts/{id}")
def update_post(id: int, updated_post: schemas.Posts, db: Session = Depends(get_db)):
    query_post = db.query(models.Posts).filter(models.Posts.id == id)
    if query_post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} was not found")
    
    query_post.update(updated_post.model_dump(), synchronize_session=False)
    db.commit()
    return {"message": query_post.first()}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Posts).filter(models.Posts.id == id)
    if post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} was not found")
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

