import json
from dataclasses import dataclass

from gradio_client import Client

from gamr_backend_api_service.model_services.abstract_model_service import AbstractModelService
from gamr_backend_api_service.model_services.hugging_face.errors import HuggingFaceException
from gamr_backend_api_service.models import ImageData
from gamr_backend_api_service.models.image_response import ImageResponse


@dataclass
class HuggingFaceInterface(AbstractModelService):
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
