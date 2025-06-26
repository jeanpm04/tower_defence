# src/map3.py

import pygame
import random
from settings import *

class Map3:
    def __init__(self):
        self.path = [
            (50, 500), (200, 500), (200, 300), (400, 300), (400, 100), (750, 100)
        ]
        self.trees = [(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)) for _ in range(20)]
        self.snow_patches = [(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)) for _ in range(20)]

    def draw(self, screen):
        screen.fill((230, 240, 255))  # fondo nieve

        for t in self.trees:
            pygame.draw.line(screen, (139, 69, 19), (t[0], t[1]), (t[0], t[1] - 15), 3)

        for snow in self.snow_patches:
            pygame.draw.circle(screen, (255, 255, 255), snow, 8)

        pygame.draw.lines(screen, (200, 200, 200), False, self.path, 40)
        pygame.draw.lines(screen, (180, 180, 180), False, self.path, 44)

        for point in self.path:
            pygame.draw.circle(screen, (0, 0, 255), point, 5)
