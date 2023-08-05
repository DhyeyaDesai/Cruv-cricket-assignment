# match.py

import random
from player import Player
from team import Team
from field import Field
from umpire import Umpire
from commentator import Commentator
from main import wickets_per_inning

class Match:
    def __init__(self, team1, team2, field):
        self.team1 = team1
        self.team2 = team2
        self.field = field
        self.innings = 1
        self.current_batting_team = None
        self.current_bowling_team = None
        self.umpire = Umpire(self)
        self.commentator = Commentator()
        self.team1_runs = 0
        self.team2_runs = 0

    def toss_and_choose(self):
        self.current_batting_team = random.choice([self.team1, self.team2])
        self.current_bowling_team = self.team1 if self.current_batting_team == self.team2 else self.team2

    def simulate_innings(self, batting_team, bowling_team):
        while batting_team.batsmen and self.umpire.wickets < wickets_per_inning:
            self.umpire.balls += 1
            batsman = batting_team.get_next_batsman()
            if not batsman:
                break  # No more batsmen, end the inning
            bowler = bowling_team.get_next_bowler()

            print(f"{self.umpire.overs}.{self.umpire.balls} - {batsman.name} on strike, {bowler.name} bowling")
            self.simulate_ball(batsman, bowler)
            if self.umpire.balls == 6:
                self.umpire.balls = 0
                self.umpire.overs += 1
                print(f"End of over {self.umpire.overs}")

        self.umpire.overs += self.umpire.balls // 6
        self.umpire.balls %= 6

    def switch_innings(self):
        self.umpire.balls = 0
        self.umpire.overs = 0
        self.umpire.wickets = 0
        self.current_batting_team, self.current_bowling_team = self.current_bowling_team, self.current_batting_team

        self.update_commentary_and_innings()

        self.simulate_innings(self.current_batting_team, self.current_bowling_team)

    def update_commentary_and_innings(self):
        if self.current_batting_team.batsmen:
            batsman_name = self.current_batting_team.batsmen[0].name
        else:
            batsman_name = "No batsman"

        if self.current_bowling_team.bowlers:
            bowler_name = self.current_bowling_team.bowlers[0].name
        else:
            bowler_name = "No bowler"

        self.commentator.provide_commentary(self.umpire, self.current_batting_team, self.current_bowling_team, f"Innings switch! {self.current_batting_team.name} to bat. {batsman_name} on strike. {bowler_name} to bowl.")


    def simulate_innings_pair(self, team1, team2):
        self.simulate_innings(team1, team2)
        self.switch_innings()

        if self.current_batting_team == team1:
            batsman_name = team1.batsmen[0].name if team1.batsmen else "No batsman"
            bowler_name = team2.bowlers[0].name if team2.bowlers else "No bowler"
        else:
            batsman_name = team2.batsmen[0].name if team2.batsmen else "No batsman"
            bowler_name = team1.bowlers[0].name if team1.bowlers else "No bowler"
        
        self.commentator.provide_commentary(self.umpire, None, None, f"Innings switch! {self.current_batting_team.name} to bat. {batsman_name} on strike. {bowler_name} to bowl.")
        self.simulate_innings(self.current_batting_team, self.current_bowling_team)


    def start_match(self):
        self.team1.select_captain()
        self.team2.select_captain()
        self.team1.set_batting_order()
        self.team2.set_batting_order()
        self.team1.set_bowling_order()
        self.team2.set_bowling_order()
        self.toss_and_choose()
        self.simulate_innings_pair(self.team1, self.team2)
        self.end_match()

    def simulate_ball(self, batsman, bowler):
        self.umpire.predict_outcome(batsman, bowler, self.field)
        if self.umpire.check_wicket(self):
            self.commentator.provide_commentary(self.umpire, batsman, bowler, "OUT!")

    def end_match(self):
        if self.team1_runs > self.team2_runs:
            winner = self.team1
        elif self.team2_runs > self.team1_runs:
            winner = self.team2
        else:
            winner = None
        print(f"Match Ended: {self.team1.name} - {self.team1_runs}/{self.umpire.wickets} in {self.umpire.overs} overs")
        print(f"{self.team2.name} needs {self.team1_runs + 1} runs to win.")
        if winner:
            print(f"{winner.name} won the match!")
        else:
            print("The match ended in a draw.")