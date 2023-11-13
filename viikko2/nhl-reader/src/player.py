class Player:
    def __init__(self, dict):
        
        #print("eka")
        if dict['nationality'] == 'FIN':
            print(dict)
            #print("toka")
            self.name = dict['name']
            self.nationality = dict['nationality']
            self.assists = dict['assists']
            self.goals = dict['goals']
            self.penalties = dict['penalties']
            self.team = dict['team']
            self.games = dict['games']

    # def team(self, nationality):
    #     players_of_nationality = filter(
    #         lambda player: player.team == nationality,
    #         self._players
    #     )

    def __str__(self):
        return f"{self.name} team {self.team}  goals {self.goals} assists {self.assists}"
