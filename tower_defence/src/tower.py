# src/tower.py

import pygame
import math
from settings import *
from projectile import Projectile

class Tower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.range = 100  # distancia máxima a la que puede atacar
        self.color = (0, 200, 0)
        self.radius = 20
        self.fire_rate = 60  # 1 disparo por segundo (si el juego corre a 60 FPS)
        self.cooldown = 0  # frames restantes antes de poder disparar nuevamente

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        # Visualización del rango de ataque (opcional pero útil para el jugador)
        pygame.draw.circle(screen, (0, 200, 200), (self.x, self.y), self.range, 1)

    def is_in_range(self, enemy):
        # Calcula si el enemigo está dentro del rango
        dist = math.hypot(self.x - enemy.x, self.y - enemy.y)
        return dist <= self.range

    def attack(self, enemies, projectiles):
        if self.cooldown > 0:
            self.cooldown -= 1
            return

        for enemy in enemies:
            if self.is_in_range(enemy):
                # Dispara un proyectil hacia el primer enemigo que esté en rango
                projectile = Projectile(self.x, self.y, enemy)
                projectiles.append(projectile)
                self.cooldown = self.fire_rate
                break
