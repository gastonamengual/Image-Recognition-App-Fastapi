import json
from dataclasses import dataclass

from fastapi import Response
from gradio_client import Client

from app.model_interfaces.abstract_model_interface import AbstractModelInterface
from app.request_models.models import ImageData


@dataclass
class HuggingFaceInterface(AbstractModelInterface):
    model_api_url: str = "https://gastonamengual-object-detection-app.hf.space/"

    @property
    def _client(self):
        return Client(self.model_api_url)

    def predict(self, image_data: ImageData):
        try:
            result = self._client.predict(
                json.dumps(image_data.list_encoded_image),
                api_name="/predict",
            )
            bytes_image = bytes(json.loads(result))
            return Response(content=bytes_image, media_type="image/png")
        except Exception as ex:
            raise ValueError(f"API Error: {ex}")
