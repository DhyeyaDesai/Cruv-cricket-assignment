# commentator.py

class Commentator:
    def __init__(self):
        pass

    def provide_commentary(self, umpire, batsman, bowler, outcome):
        if batsman and bowler:
            print(f"{umpire.overs}.{umpire.balls} {bowler.name} to {batsman.name}: {outcome}")
        else:
            print(f"{umpire.overs}.{umpire.balls} {outcome}")