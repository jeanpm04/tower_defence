# src/enemy.py

import pygame
import math
from tower_defence.src.settings import *


class Enemy:
    def __init__(self, path, health=100, speed=2):
        self.path = path
        self.current_point = 0
        self.x, self.y = self.path[self.current_point]
        self.speed = speed
        self.radius = 15
        self.color = (0, 0, 255)
        self.alive = True
        self.health = health
        self.max_health = health
        self.angle = 0

    def move(self):
        if self.current_point + 1 >= len(self.path):
            self.alive = False
            return

        target_x, target_y = self.path[self.current_point + 1]
        dir_vector = (target_x - self.x, target_y - self.y)
        distance = math.hypot(*dir_vector)

        if distance == 0:
            self.current_point += 1
            return

        dir_vector = (dir_vector[0]/distance, dir_vector[1]/distance)
        self.x += dir_vector[0] * self.speed
        self.y += dir_vector[1] * self.speed

        if distance < self.speed:
            self.current_point += 1

        self.angle = math.degrees(math.atan2(-dir_vector[1], dir_vector[0]))

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

        bar_width, bar_height = 40, 5
        pygame.draw.rect(screen, (255, 0, 0), (self.x - bar_width // 2, self.y - 30, bar_width, bar_height))
        health_width = bar_width * (self.health / self.max_health)
        pygame.draw.rect(screen, (0, 255, 0), (self.x - bar_width // 2, self.y - 30, health_width, bar_height))

    def take_damage(self, amount):
        if not self.alive:
            return
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            self.alive = False
