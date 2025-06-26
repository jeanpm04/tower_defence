# src/wave_manager.py

try:
    from src.animated_enemy import AnimatedEnemy
except ImportError:
    from animated_enemy import AnimatedEnemy


class WaveManager:
    def __init__(self, path):
        self.path = path
        self.wave_number = 1
        self.enemies_to_spawn = self.wave_number * 5
        self.spawn_timer = 0
        self.spawn_delay = 30
        self.enemies = []
        self.max_rounds = 5

        self.boss_spawned = False
        self.total_enemies = self.enemies_to_spawn + 1  # +1 boss

    def update(self):
        self.spawn_timer += 1
        if self.spawn_timer >= self.spawn_delay:
            if self.enemies_to_spawn > 0:
                self.spawn_enemy()
                self.spawn_timer = 0
            elif not self.boss_spawned:
                self.spawn_boss()
                self.boss_spawned = True
                self.spawn_timer = 0

    def spawn_enemy(self):
        base_health = 50
        base_speed = 1.0
        scale = self.wave_number

        enemy = AnimatedEnemy(
            self.path,
            "assets/Bat.png",
            frame_width=64,
            frame_height=64,
            num_frames=4,
            health=base_health + (scale * 15),      # cada ronda +15 de vida
            speed=base_speed + (scale * 0.05)       # un poquito más rápido
        )
        self.enemies.append(enemy)
        self.enemies_to_spawn -= 1

    def spawn_boss(self):
        boss = AnimatedEnemy(
            self.path,
            "assets/Bat.png",  # sprite para el boss
            frame_width=64,
            frame_height=64,
            num_frames=4,
            health=300 + (self.wave_number * 100),
            speed=0.7
        )
        self.enemies.append(boss)

    def next_wave(self):
        self.wave_number += 1
        self.enemies_to_spawn = self.wave_number * 5
        self.boss_spawned = False
        self.total_enemies = self.enemies_to_spawn + 1

    def is_wave_clear(self):
        return self.enemies_to_spawn == 0 and self.boss_spawned and all(not e.alive for e in self.enemies)
