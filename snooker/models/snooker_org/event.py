from dataclasses import dataclass

from dataclasses_json import dataclass_json

from snooker.models import JsonModel


@dataclass_json
@dataclass
class Event(JsonModel):
    ID: int
    Name: str
    StartDate: str
    EndDate: str
    Sponsor: str
    Season: int
    Type: str
    Num: int
    Venue: str
    City: str
    Country: str
    Discipline: str
    Main: int
    Sex: str
    AgeGroup: str
    Url: str
    Related: str
    Stage: str
    ValueType: str
    ShortName: str
    WorldSnookerId: int
    RankingType: str
    EventPredictionID: int
    Team: bool
    Format: int
    Twitter: str
    HashTag: str
    ConversionRate: int
    AllRoundsAdded: bool
    PhotoURLs: str
    NumCompetitors: int
    NumUpcoming: int
    NumActive: int
    NumResults: int
    Note: str
    CommonNote: str
    DefendingChampion: int
    PreviousEdition: int
