class Score(object):
    """Create a scoreboard"""

    def __init__(self) -> None:
        self.score = 0

    def raise_score(self) -> None:
        self.score += 1

    def keep_score(self) -> None:
        self.score += 0

    def __str__(self):
        return self.score
