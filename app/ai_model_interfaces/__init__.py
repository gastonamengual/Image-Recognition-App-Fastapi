from enum import Enum, auto
from typing import assert_never

from app.ai_model_interfaces.abstract_model_interface import AbstractModelInterface
from app.ai_model_interfaces.hugging_face_interface import HuggingFaceInterface


class ModelInterface(Enum):
    HuggingFace = auto()


def get_ai_model_interface(interface: ModelInterface) -> AbstractModelInterface:
    match interface:
        case ModelInterface.HuggingFace:
            return HuggingFaceInterface
        case _:
            assert_never(interface)
