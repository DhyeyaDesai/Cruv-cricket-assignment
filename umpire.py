# umpire.py

import random
from main import wickets_per_inning

class Umpire:
    def __init__(self):
        self.score = 0
        self.wickets = 0
        self.overs = 0
        self.balls = 0

    def predict_outcome(self, batsman, bowler, field):
        boundary_prob = field.calculate_boundary_probability(batsman)
        wicket_prob = 0.05
        
        outcome = random.uniform(0, 1)
        if outcome < boundary_prob:
            self.score += 4
        else:
            self.score += 1

        if outcome < wicket_prob:
            self.wickets += 1
            if self.wickets == wickets_per_inning:
                self.match.switch_innings()

    def check_wicket(self, match):
        wicket_prob = 0.05
        outcome = random.uniform(0, 1)
        if outcome < wicket_prob:
            self.wickets += 1
            if self.wickets == wickets_per_inning:
                match.switch_innings()
            return True
        return False