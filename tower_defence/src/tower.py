# src/tower.py

import pygame
import math
from projectile import Projectile

class Tower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.range = 150
        self.damage = 25
        self.fire_rate = 60  # frames
        self.timer = 0
        self.target = None

        # Cargar imagen de la torre
        self.image_original = pygame.image.load("assets/tower.png").convert_alpha()
        self.image_original = pygame.transform.scale(self.image_original, (64, 64))

    def find_target(self, enemies):
        closest_enemy = None
        closest_dist = float('inf')
        for enemy in enemies:
            if enemy.alive:
                dist = math.hypot(enemy.x - self.x, enemy.y - self.y)
                if dist < closest_dist and dist <= self.range:
                    closest_dist = dist
                    closest_enemy = enemy
        self.target = closest_enemy

    def attack(self, enemies, projectiles):
        self.timer += 1
        self.find_target(enemies)
        if self.target and self.timer >= self.fire_rate:
            projectile = Projectile(self.x, self.y, self.target, self.damage)
            projectiles.append(projectile)
            self.timer = 0

    def draw(self, screen):
        if self.target:
            dx = self.target.x - self.x
            dy = self.target.y - self.y
            angle = math.degrees(math.atan2(-dy, dx)) - 90  # compensación por sprite hacia arriba
        else:
            angle = 0

        rotated_image = pygame.transform.rotate(self.image_original, angle)
        rect = rotated_image.get_rect(center=(self.x, self.y))
        screen.blit(rotated_image, rect.topleft)
