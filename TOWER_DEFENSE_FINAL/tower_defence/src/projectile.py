# src/projectile.py

import pygame
import math
from settings import *

class Projectile:
    def __init__(self, x, y, target, damage=20, speed=5):
        self.x = x
        self.y = y
        self.target = target
        self.damage = damage
        self.speed = speed
        self.radius = 5
        self.color = (255, 0, 0)
        self.alive = True

    def move(self):
        if not self.target.alive:
            self.alive = False
            return

        dir_vector = (self.target.x - self.x, self.target.y - self.y)
        distance = math.hypot(*dir_vector)

        if distance == 0:
            self.hit()
            return

        dir_vector = (dir_vector[0]/distance, dir_vector[1]/distance)
        self.x += dir_vector[0] * self.speed
        self.y += dir_vector[1] * self.speed

        if distance < self.speed:
            self.hit()

    def hit(self):
        self.target.take_damage(self.damage)
        self.alive = False

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
