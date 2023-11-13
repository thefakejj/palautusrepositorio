import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url, timeout=10).json()

    print("JSON-muotoinen vastaus:")
    print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        if player is not None:
            players.append(player)
            #print(players)
    print(players)
    print("Oliot:")

    # for player in players:
    #     print(player)
    print(players[0])

if __name__ == "__main__":
    main()
