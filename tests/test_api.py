import asyncio
import io
import os

import pytest
from fastapi import Response, UploadFile

from api.api import detect_objects


@pytest.fixture
def sample_img_url() -> str:
    current_dir = os.getcwd()
    return f"{current_dir}/tests/sample_images/computer.jpg"


def test_detect_objects(sample_img_url: str):
    with open(sample_img_url, "rb") as image_file:
        image_bytes = io.BytesIO(image_file.read())

    upload_file = UploadFile(filename="computer.jpg", file=image_bytes)

    response = asyncio.run(detect_objects(upload_file), debug=True)

    assert isinstance(response, Response)


def test_detect_objects_incorrect_extension(sample_img_url: str):
    with open(sample_img_url, "rb") as image_file:
        image_bytes = io.BytesIO(image_file.read())

    upload_file = UploadFile(filename="computer.pdf", file=image_bytes)

    with pytest.raises(ValueError) as ex:
        asyncio.run(detect_objects(upload_file), debug=True)
        assert ex == "Wrong filename format"


def test_detect_objects_no_filename(sample_img_url: str):
    with open(sample_img_url, "rb") as image_file:
        image_bytes = io.BytesIO(image_file.read())

    upload_file = UploadFile(filename="", file=image_bytes)

    with pytest.raises(ValueError) as ex:
        asyncio.run(detect_objects(upload_file), debug=True)
        assert ex == "No image Selected"
