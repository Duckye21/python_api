# Python built-in modules import
import time

# pkg import
from fastapi import FastAPI
from mysql.connector import connect, Error

# Local imports
from . import models
from .routers import user, post, auth
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


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
        
        
app.include_router(user.router)
app.include_router(post.router)
app.include_router(auth.router)

