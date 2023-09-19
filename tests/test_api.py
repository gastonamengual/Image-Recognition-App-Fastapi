import asyncio
import io
import os

import pytest
from fastapi import UploadFile

from api.api import detect_objects


@pytest.fixture
def sample_img_url() -> str:
    current_dir = os.getcwd()
    return f"{current_dir}/tests/sample_images/computer.jpg"


def test_detect_objects(sample_img_url: str):
    with open(sample_img_url, "rb") as image_file:
        image_bytes = io.BytesIO(image_file.read())

    upload_file = UploadFile(filename="computer.jpg", file=image_bytes)

    predicted_image = asyncio.run(detect_objects(upload_file), debug=True)

    assert isinstance(predicted_image, list)
