import asyncio
import io
from fastapi import UploadFile, Response
from server.api.api import detect_objects

def test_detect_objects():
    with open("/Users/gaston/Documents/repos/ImageRecognitionApp/Image-Recognition-App-Fastapi/tests/api/sample_images/computer.jpg", "rb") as image_file:
        image_bytes = io.BytesIO(image_file.read())
    
    upload_file = UploadFile(filename="computer.jpg", file=image_bytes)

    img_bytes_response = asyncio.run(detect_objects(upload_file), debug=True)

    assert isinstance(img_bytes_response, Response)