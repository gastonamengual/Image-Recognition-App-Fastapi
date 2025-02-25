import base64
import json

import numpy as np
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from gradio_client import Client
from pydantic import BaseModel

from app.validations.validations import validate_filename

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class ImageData(BaseModel):
    filename: str
    image_bytes: bytes


MODEL_API_URL = "https://gastonamengual-object-detection-app.hf.space/"


@app.get("/")
async def root():
    return {"message": "access the /detect_objects endpoint"}


@app.post("/detect_objects")
async def detect_objects(image_data: ImageData) -> Response:

    image_bytes = base64.b64decode(image_data.image_bytes)

    validate_filename(image_data.filename)

    list_encoded_image = np.frombuffer(image_bytes, dtype=np.uint8).tolist()

    try:
        client = Client(MODEL_API_URL)
        result = client.predict(
            json.dumps(list_encoded_image),
            api_name="/predict",
        )
        bytes_image = bytes(json.loads(result))
        response = Response(content=bytes_image, media_type="image/png")
        return response

    except Exception as ex:
        raise ValueError(f"API Error: {ex}")
