from fastapi import Depends, FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

from app.ai_model_interfaces import ModelInterface, get_ai_model_interface
from app.auth.auth import TokenGenerator
from app.exceptions import ERROR_TO_HANDLER_MAPPING
from app.models import ImageData, User

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


@app.post("/token")
async def token(user: User):
    token_generator = TokenGenerator(user)
    token = token_generator.get_token()
    return {"token": token, "type": "BEARER"}


@app.post("/detect_objects")
async def detect_objects(
    image_data: ImageData,
    current_user: User = Depends(TokenGenerator().get_user_from_token),
) -> Response:
    model_interface = get_ai_model_interface(
        ModelInterface[image_data.ai_model_interface]
    )
    image_response = model_interface().predict(image_data=image_data)

    return image_response.response
