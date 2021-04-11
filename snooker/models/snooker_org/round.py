from dataclasses import dataclass

from dataclasses_json import dataclass_json

from snooker.models import JsonModel


@dataclass_json
@dataclass
class Round(JsonModel):
    Round: int
    RoundName: str
    EventID: int
    MainEvent: int
    Distance: int
    NumLeft: int
    NumMatches: int
    Note: str
    ValueType: str
    Rank: int
    Money: float
    SeedGetsHalf: int
    ActualMoney: float
    Currency: str
    ConversionRate: int
    Points: int
    SeedPoints: int
