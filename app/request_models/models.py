from pydantic import BaseModel


class ImageData(BaseModel):
    filename: str
    image_bytes: bytes


class TokenRequest(BaseModel):
    username: str
