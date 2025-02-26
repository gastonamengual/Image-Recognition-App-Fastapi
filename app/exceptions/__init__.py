from app.exceptions.exception_handlers import (
    hugging_face_api_exception_handler,
    token_not_decoded_exception_handler,
    user_blank_incorrect_exception_handler,
    user_not_exists_exception_handler,
)
from app.exceptions.exceptions import (
    HuggingFaceException,
    TokenNotDecoded,
    UserBlank,
    UserNotExists,
)

ERROR_TO_HANDLER_MAPPING = [
    [UserNotExists, user_not_exists_exception_handler],
    [UserBlank, user_blank_incorrect_exception_handler],
    [TokenNotDecoded, token_not_decoded_exception_handler],
    [HuggingFaceException, hugging_face_api_exception_handler],
]
