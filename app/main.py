from fastapi import Depends, FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

from app.auth.auth import get_current_user, get_token
from app.auth.model import User
from app.exceptions.exception_handlers import ERROR_TO_HANDLER_MAPPING
from app.model_interfaces import ModelInterface, model_interfaces
from app.request_models.models import ImageData, TokenRequest

interface_name = "HuggingFace"

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

for error_exception, error_handler in ERROR_TO_HANDLER_MAPPING:
    app.add_exception_handler(error_exception, error_handler)


@app.get("/")
async def root():
    return {"message": "access the /detect_objects endpoint"}


@app.post("/generate_token")
async def generate_token(username: TokenRequest):
    access_token = get_token(username.username)
    return {"token": access_token, "type": "BEARER"}


@app.post("/detect_objects")
async def detect_objects(
    image_data: ImageData, current_user: User = Depends(get_current_user)
) -> Response:
    model_interface = model_interfaces[ModelInterface[interface_name]]
    response = model_interface().predict(image_data=image_data)
    return response
