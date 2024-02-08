from passlib.context import CryptContext

pwd_contex = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password):
    return pwd_contex.hash(password)
