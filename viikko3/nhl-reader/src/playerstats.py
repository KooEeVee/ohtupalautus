from playerreader import PlayerReader

class PlayerStats:
    def __init__(self, reader : PlayerReader):
        self.reader = reader

    def top_scorers_by_nationality(self, country):
        players = self.reader.get_players()
        players_by_country = [player for player in players if player.nationality == country]
        players_by_country_sorted = sorted(players_by_country, key=lambda player : player.points, reverse=True)

        return players_by_country_sorted
        

        

            