from dataclasses import dataclass

from fastapi import status


@dataclass
class UserNotExists(Exception):
    status_code: int = status.HTTP_403_FORBIDDEN
    message: str = "User Not Allowed"


@dataclass
class TokenNotDecoded(Exception):
    status_code: int = status.HTTP_401_UNAUTHORIZED
    message: str = "Authentication failed: could not decode JWT token correctly"
