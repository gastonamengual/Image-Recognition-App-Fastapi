import base64
from typing import Self

import numpy as np
from pydantic import BaseModel, model_validator

ALLOWED_EXTENSIONS = ["png", "jpg", "jpeg"]


class ImageData(BaseModel):
    filename: str
    image_bytes: bytes
    ai_model_interface: str

    @model_validator(mode="after")
    def validate_filename(self) -> Self:
        if self.filename == "":
            raise ValueError("self.filename is empty")

        if (
            "." not in self.filename
            or self.filename.rsplit(".", 1)[1].lower() not in ALLOWED_EXTENSIONS
        ):
            raise ValueError("Wrong filename format")

        return self

    @property
    def list_encoded_image(self) -> list:
        image_bytes_decoded = base64.b64decode(self.image_bytes)
        return np.frombuffer(image_bytes_decoded, dtype=np.uint8).tolist()
