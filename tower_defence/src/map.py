# src/map.py

import pygame
from settings import *

class Map:
    def __init__(self):
        self.path = [
            (50, 100),
            (200, 100),
            (200, 300),
            (600, 300),
            (600, 500),
            (750, 500)
        ]

    def draw(self, screen):
        pygame.draw.lines(screen, (150, 75, 0), False, self.path, 20)
        for point in self.path:
            pygame.draw.circle(screen, (255, 0, 0), point, 5)
