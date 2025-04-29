class Player:
    def __init__(self, name: str, symbol: str):
        self.name = name
        self.symbol = symbol
        self.score = 0

    def increment_score(self):
        """Increment player's score."""
        self.score += 1

    def get_score(self) -> int:
        """Get player's current score."""
        return self.score
