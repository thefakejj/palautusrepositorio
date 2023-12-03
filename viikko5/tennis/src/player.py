class Player:
    def __init__(self, player_name):
        self._name = player_name
        self._score = 0

    def score(self):
        self._score += 1

    def get_score(self):
        return self._score

    def get_name(self):
        return self._name
