from dataclasses import dataclass

from dataclasses_json import dataclass_json

from snooker.models import JsonModel


@dataclass_json
@dataclass
class Seeding(JsonModel):
    EventID: int
    PlayerID: int
    Seeding: int
