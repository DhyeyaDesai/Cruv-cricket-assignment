# field.py

import random

class Field:
    def __init__(self, field_size, fan_ratio, pitch_conditions, home_advantage):
        self.field_size = field_size
        self.fan_ratio = fan_ratio
        self.pitch_conditions = pitch_conditions
        self.home_advantage = home_advantage

    def calculate_boundary_probability(self, batsman):
        return batsman.batting * random.uniform(0.8, 1.2)
