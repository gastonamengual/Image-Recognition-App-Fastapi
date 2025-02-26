from fastapi import Request
from fastapi.responses import JSONResponse

from app.auth.exceptions import TokenNotDecoded, TokenPayloadIncorrect, UserNotExists


def user_not_exists_exception_handler(request: Request, exc: UserNotExists):
    return JSONResponse(status_code=exc.status_code, content={"message": exc.message})


def token_payload_incorrect_exception_handler(request: Request, exc: UserNotExists):
    return JSONResponse(status_code=exc.status_code, content={"message": exc.message})


def token_not_decoded_exception_handler(request: Request, exc: UserNotExists):
    return JSONResponse(status_code=exc.status_code, content={"message": exc.message})


ERROR_TO_HANDLER_MAPPING = [
    [UserNotExists, user_not_exists_exception_handler],
    [TokenPayloadIncorrect, token_payload_incorrect_exception_handler],
    [TokenNotDecoded, token_not_decoded_exception_handler],
]
