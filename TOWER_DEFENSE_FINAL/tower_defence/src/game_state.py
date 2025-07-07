class GameState:
    def __init__(self):
        self.lives = 20
        self.level = 1
        self.max_level = 5
        self.enemies_remaining = 10
        self.enemies_crossed = 0
        self.running = True
        self.status = "playing"  # puede ser: playing, victory, defeat
