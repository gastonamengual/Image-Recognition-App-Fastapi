from datetime import datetime, timedelta, timezone

import jwt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from app.auth.exceptions import TokenNotDecoded, TokenPayloadIncorrect, UserNotExists

from .model import User

SECRET_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

DATABASE = ["gaston", "ezepiola"]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="generate_token")


def validate_user_exists(user: User):
    if user.username not in DATABASE:
        raise UserNotExists


def get_token(
    username: str,
    expires_delta: timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
):
    user = User(username=username)
    validate_user_exists(user)
    data = {"username": username}
    if not data["username"]:
        raise TokenPayloadIncorrect

    expire = datetime.now(timezone.utc) + expires_delta
    data["exp"] = expire
    token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return token


def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except Exception:
        raise TokenNotDecoded

    user = User(username=payload.get("username"))
    validate_user_exists(user)
    validate_user_exists(user)
    return user
