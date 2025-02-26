from enum import Enum, auto

from app.model_interfaces.hugging_face_interface import HuggingFaceInterface


class ModelInterface(Enum):
    HuggingFace = auto()


model_interfaces = {
    ModelInterface.HuggingFace: HuggingFaceInterface,
}
