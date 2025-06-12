# src/wave_manager.py

from enemy import Enemy

class WaveManager:
    def __init__(self, path):
        self.path = path
        self.wave_number = 1
        self.enemies_to_spawn = self.wave_number * 5
        self.spawn_timer = 0
        self.spawn_delay = 30
        self.enemies = []
        self.max_rounds = 5  # Máximo 5 rondas

    def update(self):
        self.spawn_timer += 1
        if self.spawn_timer >= self.spawn_delay and self.enemies_to_spawn > 0:
            self.spawn_enemy()
            self.spawn_timer = 0

    def spawn_enemy(self):
        enemy = Enemy(
            self.path,
            health=50 + (self.wave_number * 10),
            speed=1 + (self.wave_number * 0.1)
        )
        self.enemies.append(enemy)
        self.enemies_to_spawn -= 1

    def next_wave(self):
        self.wave_number += 1
        self.enemies_to_spawn = self.wave_number * 5

    def is_wave_clear(self):
        return self.enemies_to_spawn == 0 and all(not e.alive for e in self.enemies)
