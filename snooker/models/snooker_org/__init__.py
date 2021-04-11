from abc import ABC
from typing import Any, Dict, List


class JsonModel(ABC):
    def schema(self, *args: List[Any], **kwargs: Dict[Any, Any]) -> Any:
        pass
