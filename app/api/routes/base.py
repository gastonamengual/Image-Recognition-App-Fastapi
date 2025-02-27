from fastapi import APIRouter, Depends, Response

from app.auth.token import TokenGenerator
from app.data.user_manager import UserManager
from app.database_connector.firebase import FirestoreConnector
from app.model_services import ModelService, get_ai_model_interface
from app.models import ImageData, User

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "access the /detect_objects endpoint"}


@router.post("/token")
async def token(user: User):
    token_generator = TokenGenerator()
    _token = token_generator.get_token(user)
    return {"token": _token, "type": "BEARER"}


@router.post("/detect_objects")
async def detect_objects(
    image_data: ImageData,
    current_user: User = Depends(TokenGenerator().get_user_from_token),
    user_manager: UserManager = Depends(UserManager(db_connector=FirestoreConnector())),  # type: ignore
) -> Response:
    user_manager.validate_user_exists(current_user)
    model_interface = get_ai_model_interface(
        ModelService[image_data.ai_model_interface]
    )
    image_response = model_interface().predict(image_data=image_data)  # type: ignore

    return image_response.response
