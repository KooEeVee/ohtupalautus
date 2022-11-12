import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = requests.get(url).json()
    headers = requests.get(url).headers

    #print("JSON-muotoinen vastaus: ")
    #print(response)
    #print(headers)

    players = []
    date = headers["Date"]

    for player_dict in response:
        player = Player(
            player_dict["name"],
            player_dict["team"],
            player_dict["goals"],
            player_dict["assists"]
        )
        if player_dict["nationality"] == "FIN":
            players.append(player)

    print(f"Players from FIN {date}")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
