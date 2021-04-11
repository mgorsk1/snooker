from abc import ABC
from typing import Any, Dict, List


class JsonModel(ABC):
    @staticmethod
    def schema(*args: List[Any], **kwargs: Dict[Any, Any]) -> Any:
        pass
