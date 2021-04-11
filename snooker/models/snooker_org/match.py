from dataclasses import dataclass

from dataclasses_json import dataclass_json

from snooker.models import JsonModel


@dataclass_json
@dataclass
class Match(JsonModel):
    ID: int
    EventID: int
    Round: int
    Number: int
    Player1ID: int
    Score1: int
    Walkover1: bool
    Player2ID: int
    Score2: int
    Walkover2: bool
    WinnerID: int
    Unfinished: bool
    OnBreak: bool
    WorldSnookerID: int
    LiveUrl: str
    DetailsUrl: str
    PointsDropped: bool
    ShowCommonNote: bool
    Estimated: bool
    Type: int
    TableNo: int
    VideoURL: str
    InitDate: str
    ModDate: str
    StartDate: str
    EndDate: str
    ScheduledDate: str
    FrameScores: str
    Sessions: str
    Note: str
    ExtendedNote: str
