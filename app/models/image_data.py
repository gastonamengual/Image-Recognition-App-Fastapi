import base64
from pathlib import Path
from typing import Self

import numpy as np
from pydantic import BaseModel, Field, model_validator


ALLOWED_EXTENSIONS = ["png", "jpg", "jpeg"]


class ImageData(BaseModel):
    filename: str = Field(min_length=1)
    image_bytes: bytes
    model_service: str

    @model_validator(mode="after")
    def validate_filename(self) -> Self:
        if Path(self.filename).suffix.lower() not in ALLOWED_EXTENSIONS:
            raise ValueError("Wrong filename format")

        return self

    @property
    def list_encoded_image(self) -> list:
        image_bytes_decoded = base64.b64decode(self.image_bytes)
        return np.frombuffer(image_bytes_decoded, dtype=np.uint8).tolist()
