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

        # self.player1_name = player1_name
        # self.player2_name = player2_name
        self.player_1_scolre = 0
        self.player_2_scolre = 0

        # maybe like this
        # define player1 and player2 in main program by calling this class
        # return self.player1, self.player2


    def won_point(self, player_name):
        player = self.players[player_name]
        player.score()

    def get_score(self):
        score = ""
        temp_score = 0

        if self.player1.get_score() == self.player2.get_score():
            if self.player1.get_score() >= 3:
                score = "Deuce"
            else:
                points = self.score_names[self.player1.get_score()]
                score = f"{points}-All"
            # if self.player1.get_score() == 0:
            #     score = "Love-All"
            # elif self.player1.get_score() == 1:
            #     score = "Fifteen-All"
            # elif self.player1.get_score() == 2:
            #     score = "Thirty-All"
            # else:
            #     score = "Deuce"





        elif self.player1.get_score() >= 4 or self.player2.get_score() >= 4:
            advantage_info = self.get_player_advantage_and_size()

            if advantage_info["ahead_by"] >= 2:
                return f"Win for {advantage_info['player_name']}"
            return f"Advantage {advantage_info['player_name']}"

            # minus_result = self.player1.get_score() - self. player2.get_score()

            # if minus_result == 1:
            #     score = "Advantage player1"
            # elif minus_result == -1:
            #     score = "Advantage player2"
            # elif minus_result >= 2:
            #     score = "Win for player1"
            # else:
            #     score = "Win for player2"
        else:
            player1_score = self.score_names[self.player1.get_score()]
            player2_score = self.score_names[self.player2.get_score()]
            score = f"{player1_score}-{player2_score}"
            # for i in range(1, 3):
            #     if i == 1:
            #         temp_score = self.player1.get_score()
            #     else:
            #         score = score + "-"
            #         temp_score = self.player1.get_score()

            #     if temp_score == 0:
            #         score = score + "Love"
            #     elif temp_score == 1:
            #         score = score + "Fifteen"
            #     elif temp_score == 2:
            #         score = score + "Thirty"
            #     elif temp_score == 3:
            #         score = score + "Forty"

        return score

    def get_player_advantage_and_size(self):
        # player_stack = [self.player1, self.player2]
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

        # elif self.player1.get_score() >= 4 or self.player2.get_score() >= 4:
        #     advantage_for = 
        #     minus_result = self.player1.get_score() - self.player2.get_score()

        #     if minus_result == 1:
        #         score = "Advantage player1"
        #     elif minus_result == -1:
        #         score = "Advantage player2"
        #     elif minus_result >= 2:
        #         score = "Win for player1"
        #     else:
        #         score = "Win for player2"
        return advantage_info
