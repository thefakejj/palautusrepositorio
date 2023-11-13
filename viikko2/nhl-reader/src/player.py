class Player:
    def __init__(self, dict):
        
        if dict['nationality'] == 'FIN':
            #print("suomi")
            self.name = dict['name']
            self.nationality = dict['nationality']
            self.assists = dict['assists']
            self.goals = dict['goals']
            self.penalties = dict['penalties']
            self.team = dict['team']
            self.games = dict['games']
            print(self)
        else:
            #print("none")
            return


    def __str__(self):
        return f"{self.name} team {self.team}  goals {self.goals} assists {self.assists}"
