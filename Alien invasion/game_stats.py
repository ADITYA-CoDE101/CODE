class Gamestats:

    def __init__(self, ai_game):
        """Initializing statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initializing statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit