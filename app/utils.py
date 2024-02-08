from passlib.context import CryptContext

pwd_contex = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password):
    return pwd_contex.hash(password)


def verify_password(password, hashed_password):
    return pwd_contex.verify(password, hashed_password)

