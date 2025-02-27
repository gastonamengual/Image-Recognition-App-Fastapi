from abc import ABC, abstractmethod
from dataclasses import dataclass

from app.models.image_data import ImageData


@dataclass
class AbstractModelService(ABC):
    @abstractmethod
    def predict(self, image_data: ImageData): ...
