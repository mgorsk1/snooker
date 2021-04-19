from typing import List, Optional, Type  # noqa

from snooker.api.base import BaseApi
from snooker.models.snooker_org.event import Event
from snooker.models.snooker_org.match import Match
from snooker.models.snooker_org.player import Player
from snooker.models.snooker_org.ranking import Ranking
from snooker.models.snooker_org.round import Round
from snooker.models.snooker_org.seeding import Seeding


class SnookerOrgApi(BaseApi):
    """
    Class serving as interface for snooker.org API.
    """

    @property
    def base_url(self) -> str:
        """
        Parameter describing snooker.org API URL.

        :return: snooker.org API URL
        """
        return 'http://api.snooker.org'

    def event(self, event_id: int) -> Optional[Event]:
        """
        Retrieve info regarding specific event.

        :param event_id: ID of an event
        :return: Event info (if available)
        """
        model = Event
        params = {'e': event_id}

        return self._get_one_dimensional(params, model)

    def match(self, event_id: int, round_id: int, match_no: int) -> Optional[Match]:
        """
        Retrieve info regarding specific match.

        :param event_id: Event within which match took place
        :param round_id: Event round id
        :param match_no: Match number
        :return: Match info (if available)
        """
        model = Match
        params = {'e': event_id, 'r': round_id, 'n': match_no}

        return self._get_one_dimensional(params, model)

    def player(self, player_id: int) -> Optional[Player]:
        """
        Retrieve info regarding a player.

        :param player_id: ID of a player
        :return: Player info (if available)
        """
        model = Player
        params = {'p': player_id}

        return self._get_one_dimensional(params, model)

    def season_events(self, season: int) -> Optional[List[Event]]:
        """
        Retrieve list of all events within a season.

        :param season: ID of a season. It is a year the given season has started. Use -1 for all seasons.
        :return: List of events (if available)
        """
        params = {'t': 5, 's': season}
        model = Event

        return self._get_two_dimensional(params, model)

    def event_matches(self, event_id: int) -> Optional[List[Match]]:
        """
        Retrieve list of matches in the event.

        :param event_id: ID of the event
        :return: List of matches (if available)
        """
        params = {'t': 6, 'e': event_id}
        model = Match

        return self._get_two_dimensional(params, model)

    def ongoing_matches(self) -> Optional[List[Match]]:
        """
        Retrieve ongoing matches. It returns also matches that are currently on break.

        :return: List of ongoing matches (if available)
        """
        params = {'t': 7}
        model = Match

        return self._get_two_dimensional(params, model)

    def player_matches(self, player_id: int, season: int) -> Optional[List[Match]]:
        """
        Retrieve list of all player matches within particular season.

        :param player_id: ID of a player
        :param season: ID of a season. Use -1 value to list player matches from all seasons
        :return: List of matches (if available)
        """
        params = {'t': 8, 'p': player_id, 's': season}
        model = Match

        return self._get_two_dimensional(params, model)

    def event_players(self, event_id: int) -> Optional[List[Player]]:
        """
        Retrieve list of all players participating in an event.

        :param event_id: ID of an event
        :return: List of players (if available)
        """
        params = {'t': 9, 'e': event_id}
        model = Player

        return self._get_two_dimensional(params, model)

    def players(self, status: Optional[str], season: Optional[int]) -> Optional[List[Player]]:
        """
        Retrieve list of all players in the tour in given season.

        :param status: Status of a player. Use a for amateur and p for professional
        :param season: Season for which data is collected. Use -1 for all seasons
        :return: List of players (if available)
        """
        params = {'t': 10, 'st': status, 's': season}
        model = Player

        return self._get_two_dimensional(params, model)

    def rankings(self, ranking_type: str, season: int) -> Optional[List[Ranking]]:
        """
        Retrieve rankings for particular season.

        :param ranking_type: Type of ranking. Available ranking types: http://api.snooker.org/help.html#RankingTypes
        :param season: ID of a season for which data will be collected
        :return: List of rankings (if available)
        """
        params = {'rt': ranking_type, 's': season}
        model = Ranking

        return self._get_two_dimensional(params, model)

    def round_info(self, event_id: int) -> Optional[List[Round]]:
        """
        Retrieve round info for particular event.

        :param event_id: ID of an event
        :return: List of rounds (if available)
        """
        params = {'t': 12, 'e': event_id}
        model = Round

        return self._get_two_dimensional(params, model)

    def event_seeding(self, event_id: int) -> Optional[List[Seeding]]:
        """
        Retrieve info regarding player seedings for an event.

        :param event_id: ID of an event
        :return: List of player seedings (if available)
        """
        params = {'t': 13, 'e': event_id}
        model = Seeding

        return self._get_two_dimensional(params, model)
