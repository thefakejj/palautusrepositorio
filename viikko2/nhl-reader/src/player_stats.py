from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class PlayerStats:
    def __init__(self, reader: object):
        self._players = reader.get_players()

    def team(self, nationality):
        players_of_team = filter(
            lambda player: player.nationality == nationality,
            self._players
        )

        return list(players_of_team)

    def top_scorers_by_nationality(self, nationality):
        players = self.team(nationality)
        def sort_by_goals(player):
            return player.goals
        sort_key = sort_by_goals
        sorted_players = sorted(
            players,
            reverse=True,
            key=sort_key
        )
        result = []
        for player in sorted_players:
            result.append(player)

        return result
