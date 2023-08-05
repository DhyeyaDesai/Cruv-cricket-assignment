# team.py

import random

class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.captain = None
        self.batsmen = []
        self.bowlers = []

    def select_captain(self):
        self.captain = random.choice(self.players)

    def set_batting_order(self):
        self.batsmen = self.players

    def set_bowling_order(self):
        self.bowlers = self.players

    def get_next_batsman(self):
        return self.batsmen.pop(0)

    def get_next_bowler(self):
        return self.bowlers.pop(0)
