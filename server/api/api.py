import numpy as np
from fastapi import APIRouter, File, Response, UploadFile
from numpy.typing import ArrayLike

from server.models.model import Model, ModelConfig

router = APIRouter()

ALLOWED_EXTENSIONS = ["png", "jpg", "jpeg"]


@router.post("/detect_objects/")
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
