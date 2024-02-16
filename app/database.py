# Python built-in modules import
# import time

# from mysql.connector import connect, Error
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import settings

SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{settings.db_user_name}:{settings.db_password}@{settings.db_host_name}:{settings.db_port}/{settings.db_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
# while True:
#     try:
#         connection = connect(host="localhost", user="root", password="firebasedb", database="firebase")
#         cursor = connection.cursor()
#         print("MySQL Database connection successful")
#         break
#     except Error as e:
#         print(f"Error while connecting to MySQL: {e}")
#         print("Retrying in 2 seconds...")
#         time.sleep(2)
        
