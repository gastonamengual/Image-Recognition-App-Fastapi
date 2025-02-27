from app.auth.exceptions import (
    TokenNotDecoded,
    UserNotExists,
)
from app.model_services.hugging_face.errors import HuggingFaceException
from app.models.errors import UserBlank

from .exception_handlers import (
    hugging_face_api_exception_handler,
    token_not_decoded_exception_handler,
    user_blank_incorrect_exception_handler,
    user_not_exists_exception_handler,
)

ERROR_TO_HANDLER_MAPPING = [
    [UserNotExists, user_not_exists_exception_handler],
    [UserBlank, user_blank_incorrect_exception_handler],
    [TokenNotDecoded, token_not_decoded_exception_handler],
    [HuggingFaceException, hugging_face_api_exception_handler],
]
