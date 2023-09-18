from fastapi import FastAPI, File, Response, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from object_detection_model import model_files as model_files
from object_detection_model.model import Model

from api.aux import (
    get_model_config,
    process_image,
    validate_correct_extension,
    validate_image_filename,
)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


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

    model_config = get_model_config()
    model = Model(model_config)
    img_bytes = model.detect_object(processed_image)

    response = Response(content=img_bytes.getvalue(), media_type="image/png")

    return response
