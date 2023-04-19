from fastapi import APIRouter, File, UploadFile, Response

import numpy as np
from server.models.model import Model, ModelConfig

router = APIRouter()

ALLOWED_EXTENSIONS = ["png", "jpg", "jpeg"]

@router.post("/detect_objects/")
async def detect_objects(image: UploadFile = File()):
    image_file = await image.read()

    image_filename = image.filename
    if image_filename is None or image_filename is "":
        raise ValueError("No image Selected")

    if (
        not "." in image_filename
        and image_filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    ):
        raise ValueError("Wrong filename format")

    processed_image = np.frombuffer(image_file, dtype=np.uint8)

    model = Model(config=ModelConfig())
    img_bytes = model.detect_object(processed_image)

    response = Response(content=img_bytes.getvalue(), media_type="image/png")

    return response
