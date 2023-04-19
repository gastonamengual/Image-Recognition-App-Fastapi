import asyncio
import io
from fastapi import UploadFile, Response
import pytest
from server.api.api import detect_objects


@pytest.fixture
def sample_img_url() -> str:
    return "/Users/gaston/Documents/repos/ImageRecognitionApp/Image-Recognition-App-Fastapi/tests/api/sample_images/computer.jpg"


def test_detect_objects(sample_img_url: str):
    with open(sample_img_url, "rb") as image_file:
        image_bytes = io.BytesIO(image_file.read())

    upload_file = UploadFile(filename="computer.jpg", file=image_bytes)

    img_bytes_response = asyncio.run(detect_objects(upload_file), debug=True)

    assert isinstance(img_bytes_response, Response)
