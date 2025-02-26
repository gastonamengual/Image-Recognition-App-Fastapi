from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class AbstractModelInterface(ABC):

    @abstractmethod
    def predict(self): ...
