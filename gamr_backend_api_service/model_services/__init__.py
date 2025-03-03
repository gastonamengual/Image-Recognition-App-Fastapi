from enum import StrEnum, auto
from typing import assert_never

from .abstract_model_service import AbstractModelService
from .hugging_face.service import HuggingFaceInterface


class ModelService(StrEnum):
    HuggingFace = auto()


def get_ai_model_interface(interface: ModelService) -> AbstractModelService:
    match interface:
        case ModelService.HuggingFace:
            return HuggingFaceInterface  # type: ignore
        case _:
            assert_never(interface)


__all__ = ["AbstractModelService", "HuggingFaceInterface"]
