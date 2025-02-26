from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

import jwt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from app.exceptions.exceptions import (
    TokenNotDecoded,
    UserNotExists,
)

from ..models import User

DATABASE = ["gaston", "ezepiola"]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="generate_token")


def validate_user_exists(user: User):
    if user.username not in DATABASE:
        raise UserNotExists


@dataclass
class TokenGenerator:
    user: User = None
    expiration_minutes: int = 30
    key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"  # TODO save secret
    algorithm: str = "HS256"  # TODO save secret

    @property
    def expire_data(self):
        return datetime.now(timezone.utc) + timedelta(minutes=self.expiration_minutes)

    def get_token(self):
        if not self.user:
            raise ValueError("user cannot be empty")

        validate_user_exists(self.user)

        payload = {"username": self.user.username, "exp": self.expire_data}

        token = jwt.encode(payload=payload, key=self.key, algorithm=self.algorithm)
        return token

    def get_user_from_token(self, token: str = Depends(oauth2_scheme)) -> User:
        try:
            payload = jwt.decode(token, self.key, algorithms=[self.algorithm])
        except Exception:
            raise TokenNotDecoded

        user = User(username=payload.get("username"))
        validate_user_exists(user)
        return user
