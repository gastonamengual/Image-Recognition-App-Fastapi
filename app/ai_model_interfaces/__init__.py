from enum import Enum, auto

from app.ai_model_interfaces.hugging_face_interface import HuggingFaceInterface


class ModelInterface(Enum):
    HuggingFace = auto()


ai_model_interfaces = {
    ModelInterface.HuggingFace: HuggingFaceInterface,
}
