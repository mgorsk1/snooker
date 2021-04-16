from typing import List, Optional, Type  # noqa

from snooker.api.base import BaseApi
from snooker.models.snooker_org.event import Event
from snooker.models.snooker_org.match import Match
from snooker.models.snooker_org.player import Player
from snooker.models.snooker_org.ranking import Ranking
from snooker.models.snooker_org.round import Round
from snooker.models.snooker_org.seeding import Seeding


class SnookerOrgApi(BaseApi):
    @property
    def base_url(self) -> str:
        return 'http://api.snooker.org'

    def event(self, event_id: int) -> Optional[Event]:
        model = Event
        params = {'e': event_id}

        return self._get_one_dimensional(params, model)

    def match(self, event_id: int, round_id: int, match_no: int) -> Optional[Match]:
        model = Match
        params = {'e': event_id, 'r': round_id, 'n': match_no}

        return self._get_one_dimensional(params, model)

    def player(self, player_id: int) -> Optional[Player]:
        model = Player
        params = {'p': player_id}

        return self._get_one_dimensional(params, model)

    # Note: All seasons: -1
    def season_events(self, season: int) -> Optional[List[Event]]:
        params = {'t': 5, 's': season}
        model = Event

        return self._get_two_dimensional(params, model)

    def event_matches(self, event_id: int) -> Optional[List[Match]]:
        params = {'t': 6, 'e': event_id}
        model = Match

        return self._get_two_dimensional(params, model)

    def ongoing_matches(self) -> Optional[List[Match]]:
        params = {'t': 7}
        model = Match

        return self._get_two_dimensional(params, model)

    # Note: All seasons: -1
    def player_matches(self, player_id: int, season: int) -> Optional[List[Match]]:
        params = {'t': 8, 'p': player_id, 's': season}
        model = Match

        return self._get_two_dimensional(params, model)

    def event_players(self, event_id: int) -> Optional[List[Player]]:
        params = {'t': 9, 'e': event_id}
        model = Player

        return self._get_two_dimensional(params, model)

    # Note: All seasons: -1
    def players(self, status: Optional[str], season: Optional[int]) -> Optional[List[Player]]:
        params = {'t': 10, 'st': status, 's': season}
        model = Player

        return self._get_two_dimensional(params, model)

    # Available ranking types: http://api.snooker.org/help.html#RankingTypes
    def rankings(self, ranking_type: str, season: int) -> Optional[List[Ranking]]:
        params = {'rt': ranking_type, 's': season}
        model = Ranking

        return self._get_two_dimensional(params, model)

    def round_info(self, event_id: int) -> Optional[List[Round]]:
        params = {'t': 12, 'e': event_id}
        model = Round

        return self._get_two_dimensional(params, model)

    def event_seeding(self, event_id: int) -> Optional[List[Seeding]]:
        params = {'t': 13, 'e': event_id}
        model = Seeding

        return self._get_two_dimensional(params, model)
