import io
import json

import numpy as np
from fastapi import FastAPI, File, Response, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from gradio_client import Client

app = FastAPI()
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


@app.post("/detect_objects")
async def asd():
    return 1
    # image_file: bytes = await image.read()

    # if image.filename == "":
    #     raise ValueError("No image Selected")

    # if (
    #     "." not in image.filename
    #     and image.filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    # ):
    #     raise ValueError("Wrong filename format")

    # image_bytes = io.BytesIO(image_file).read()
    # list_encoded_image = np.frombuffer(image_bytes, dtype=np.uint8).tolist()

    # client = Client("https://gastonamengual-object-detection-app.hf.space/")
    # result = client.predict(
    #     json.dumps(list_encoded_image),
    #     api_name="/predict",
    # )

    # bytes_image = bytes(json.loads(result))
    # response = Response(content=bytes_image, media_type="image/png")
    # return response
