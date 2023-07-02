import numpy as np
from fastapi import FastAPI, File, Response, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from numpy.typing import ArrayLike

from api.api import router
from api.models import Model, ModelConfig

app = FastAPI()
app.include_router(router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

ALLOWED_EXTENSIONS = ["png", "jpg", "jpeg"]


@app.get("/")
async def root():
    return {"message": "access the /detect_objects endpoint"}


@app.post("/detect_objects/")
async def detect_objects(image: UploadFile = File()):
    image_file: bytes = await image.read()

    image_filename: str = image.filename

    validate_image_filename(image_filename)
    validate_correct_extension(image_filename)

    processed_image = process_image(image_file)

    model = Model(config=ModelConfig())
    img_bytes = model.detect_object(processed_image)

    response = Response(content=img_bytes.getvalue(), media_type="image/png")

    return response


def validate_image_filename(image_filename: str):
    if image_filename == "":
        raise ValueError("No image Selected")


def validate_correct_extension(image_filename: str):
    if (
        "." not in image_filename
        and image_filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    ):
        raise ValueError("Wrong filename format")


def process_image(image_file: bytes) -> ArrayLike:
    processed_image = np.frombuffer(image_file, dtype=np.uint8)
    return processed_image
