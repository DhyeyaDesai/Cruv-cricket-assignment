import random
from player import Player
from team import Team
from field import Field
from match import Match
# from umpire import Umpire
from commentator import Commentator

def main():
    # Create players, teams, field
    players1 = [
        Player("Player 1", 0.8, 0.1, 0.8, 0.8, 0.8),
        Player("Player 2", 0.7, 0.1, 0.7, 0.7, 0.7),
        Player("Player 3", 0.7, 0.2, 0.7, 0.7, 0.7),
        # Add more players with adjusted skills
    ]

    players2 = [
        Player("Player 4", 0.9, 0.1, 0.9, 0.8, 0.9),
        Player("Player 5", 0.8, 0.1, 0.8, 0.7, 0.8),
        Player("Player 6", 0.7, 0.2, 0.7, 0.6, 0.7),
        # Add more players with adjusted skills
    ]

    # Add more players to complete the squads
    for i in range(4, 12):
        players1.append(Player(f"Player {i}", random.uniform(0.6, 0.9), random.uniform(0.1, 0.4), random.uniform(0.6, 0.9), random.uniform(0.5, 0.8), random.uniform(0.6, 0.9)))
        players2.append(Player(f"Player {i+3}", random.uniform(0.7, 0.9), random.uniform(0.1, 0.4), random.uniform(0.6, 0.9), random.uniform(0.5, 0.8), random.uniform(0.7, 0.9)))

    team1 = Team("Team A", players1)
    team2 = Team("Team B", players2)
    field = Field("large", 0.8, "dry", 0.2)  # Increased home advantage

    match = Match(team1, team2, field)
    match.start_match()

if __name__ == "__main__":
    main()