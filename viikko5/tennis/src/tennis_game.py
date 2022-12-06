class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        love = 0
        fifteen = 1
        thirty = 2
        forty = 3
        win_or_advantage = 4
        result = ""
        

        def even():
            if self.player1_score == love:
                result_even = "Love-All"
            elif self.player1_score == fifteen:
                result_even = "Fifteen-All"
            elif self.player1_score == thirty:
                result_even = "Thirty-All"
            elif self.player1_score == forty:
                result_even = "Forty-All"
            else:
                result_even = "Deuce"
            return result_even

        def advantage_or_win():
            if self.player1_score - self.player2_score == 1:
                result_win = "Advantage player1"
            elif self.player1_score - self.player2_score == -1:
                result_win = "Advantage player2"
            elif self.player1_score - self.player2_score >= 2:
                result_win = "Win for player1"
            else:
                result_win = "Win for player2"
            return result_win

        def play_round():
            temp_score = 0
            result_round = ""
            for round in range(1, 3):
                if round == 1:
                    temp_score = self.player1_score
                else:
                    result_round = result_round + "-"
                    temp_score = self.player2_score

                if temp_score == love:
                    result_round = result_round + "Love"
                elif temp_score == fifteen:
                    result_round = result_round + "Fifteen"
                elif temp_score == thirty:
                    result_round = result_round + "Thirty"
                elif temp_score == forty:
                    result_round = result_round + "Forty"
            return result_round


        if self.player1_score == self.player2_score:
            result = even()

        elif self.player1_score >= win_or_advantage or self.player2_score >= win_or_advantage:
            result = advantage_or_win()

        else:
            result = play_round()

        return result
