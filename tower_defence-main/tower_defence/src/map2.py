# src/map2.py

import pygame
import random
from settings import *

class Map2:
    def __init__(self):
        self.path = [
            (0, 300), (200, 300), (200, 500), (600, 500), (600, 100), (800, 100)
        ]
        self.cactus = [(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)) for _ in range(15)]
        self.rocks = [(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)) for _ in range(25)]

    def draw(self, screen):
        screen.fill((237, 201, 175))  # color arena

        for c in self.cactus:
            pygame.draw.rect(screen, (34, 139, 34), (*c, 5, 20))

        for rock in self.rocks:
            pygame.draw.circle(screen, (120, 110, 100), rock, 6)

        pygame.draw.lines(screen, (194, 178, 128), False, self.path, 40)
        pygame.draw.lines(screen, (160, 140, 100), False, self.path, 44)

        for point in self.path:
            pygame.draw.circle(screen, (255, 0, 0), point, 5)
