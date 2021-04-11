from dataclasses import dataclass

from dataclasses_json import dataclass_json

from snooker.models import JsonModel


@dataclass_json
@dataclass
class Ranking(JsonModel):
    ID: int
    Position: int
    PlayerID: int
    Season: int
    Sum: float
    Type: str
