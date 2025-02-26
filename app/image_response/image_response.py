from dataclasses import dataclass

from fastapi import Response


@dataclass
class ImageResponse:
    bytes_image: bytes
    media_type: str = "image/png"

    def response(self):
        return Response(content=self.bytes_image, media_type=self.media_type)
