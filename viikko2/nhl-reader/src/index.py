import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url, timeout=10).json()

    # print("JSON-muotoinen vastaus:")
    # print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    print("PLAYERS FROM FIN:")
    # for player in players:
    #     print(player)

    # Finnish players
    for player in players:
        if player.nationality == 'FIN':
            print(player)

if __name__ == "__main__":
    main()
