import asyncio
import os

import pytest
from fastapi import Response

from app.main import detect_objects


@pytest.fixture
def sample_img_url() -> str:
    current_dir = os.getcwd()
    return f"{current_dir}/tests/sample_images/computer.jpg"


def test_detect_objects(sample_img_url: str):
    with open(sample_img_url, "rb") as image_file:
        image_bytes = image_file.read()

    data = {
        "filename": "cats.jpg",
        "image_bytes": image_bytes,
    }

    response = asyncio.run(detect_objects(data), debug=True)

    assert isinstance(response, Response)
