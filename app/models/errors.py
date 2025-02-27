from dataclasses import dataclass

from fastapi import status


@dataclass
class UserBlank(Exception):
    status_code: int = status.HTTP_422_UNPROCESSABLE_ENTITY
    message: str = "You must provide a {'username': 'username'} json"
