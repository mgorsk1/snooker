from dataclasses import dataclass

from dataclasses_json import dataclass_json

from snooker.models import JsonModel


@dataclass_json
@dataclass
class Player(JsonModel):
    ID: int
    Type: int
    FirstName: str
    MiddleName: str
    LastName: str
    TeamName: str
    TeamNumber: int
    TeamSeason: int
    ShortName: str
    Nationality: str
    Sex: str
    BioPage: str
    Born: str
    Twitter: str
    SurnameFirst: bool
    License: str
    Club: str
    URL: str
    Photo: str
    PhotoSource: str
    FirstSeasonAsPro: int
    LastSeasonAsPro: int
    Info: str
