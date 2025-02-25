import json
from typing import TypedDict

import numpy as np
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from gradio_client import Client

from app.validations import validate_filename

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class ImageData(TypedDict):
    filename: str
    image_bytes: bytes


@app.get("/")
async def root():
    return {"message": "access the /detect_objects endpoint"}


@app.post("/detect_objects")
async def detect_objects(data: ImageData) -> Response:

    filename = data["filename"]
    image_bytes = data["image_bytes"]

    validate_filename(filename)

    list_encoded_image = np.frombuffer(image_bytes, dtype=np.uint8).tolist()

    client = Client("https://gastonamengual-object-detection-app.hf.space/")
    result = client.predict(
        json.dumps(list_encoded_image),
        api_name="/predict",
    )

    bytes_image = bytes(json.loads(result))
    response = Response(content=bytes_image, media_type="image/png")
    return response
