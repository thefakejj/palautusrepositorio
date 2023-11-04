import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_returns_correct_name(self):
        player = self.stats.search("Gretzky")
        self.assertEqual(player.name, "Gretzky")

    def test_wrong_search_returns_none(self):
        player = self.stats.search("Gretski")
        self.assertEqual(player, None)

    def test_team_returns_correct_players(self):
        players_of_EDM = self.stats.team("EDM")
        self.assertEqual(len(players_of_EDM), 3) # len = 3

        players_of_PIT = self.stats.team("PIT")
        self.assertEqual(len(players_of_PIT), 1) # len = 1

    def test_top_players_correct(self):
        top_scorers = self.stats.top(2)
        self.assertEqual(top_scorers[0].name, "Gretzky")
        self.assertEqual(top_scorers[1].name, "Lemieux")
