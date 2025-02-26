import json
from dataclasses import dataclass

from gradio_client import Client

from app.ai_model_interfaces.abstract_model_interface import AbstractModelInterface
from app.exceptions.exceptions import HuggingFaceException
from app.image_response.image_response import ImageResponse
from app.models import ImageData


@dataclass
class HuggingFaceInterface(AbstractModelInterface):
    model_api_url: str = (
        "https://gastonamengual-object-detection-app.hf.space/"  # TODO save as secret
    )

    @property
    def _client(self):
        return Client(self.model_api_url)

    def predict(self, image_data: ImageData) -> ImageResponse:
        try:
            result = self._client.predict(
                json.dumps(image_data.list_encoded_image),
                api_name="/predict",
            )
            bytes_image = bytes(json.loads(result))
            image_response = ImageResponse(bytes_image)
            return image_response

        except Exception as ex:
            raise HuggingFaceException(message=f"HuggingFace API Error: {ex}")
