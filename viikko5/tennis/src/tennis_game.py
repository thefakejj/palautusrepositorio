from player import Player
class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.players = {
            player1_name: self.player1,
            player2_name: self.player2
        }

        self.score_names = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }

    def won_point(self, player_name):
        player = self.players[player_name]
        player.score()

    def get_score(self):

        if self.player1.get_score() == self.player2.get_score():
            if self.player1.get_score() >= 3:
                score = "Deuce"
            else:
                points = self.score_names[self.player1.get_score()]
                score = f"{points}-All"

        elif self.player1.get_score() >= 4 or self.player2.get_score() >= 4:
            advantage_info = self.get_player_advantage_and_size()

            if advantage_info["ahead_by"] >= 2:
                return f"Win for {advantage_info['player_name']}"
            return f"Advantage {advantage_info['player_name']}"

        else:
            player1_score = self.score_names[self.player1.get_score()]
            player2_score = self.score_names[self.player2.get_score()]
            score = f"{player1_score}-{player2_score}"

        return score

    def get_player_advantage_and_size(self):
        player_stack = []
        if self.player1.get_score() > self.player2.get_score():
            player_stack.append(self.player2)
            player_stack.append(self.player1)
        else:
            player_stack.append(self.player1)
            player_stack.append(self.player2)

        ahead = player_stack.pop()
        behind = player_stack.pop()

        advantage_size = ahead.get_score() - behind.get_score()

        advantage_info = {
            "player_name": ahead.get_name(),
            "ahead_by": advantage_size
        }

        return advantage_info
