# src/map.py

import pygame
import random
from settings import *

class Map:
    def __init__(self):
        self.path = [
            (50, 100),
            (250, 100),
            (250, 200),
            (100, 200),
            (100, 300),
            (300, 300),
            (300, 400),
            (150, 400),
            (150, 500),
            (400, 500),
            (400, 150),
            (550, 150),
            (550, 350),
            (700, 350),
            (700, 450),
            (500, 450),
            (500, 550),
            (750, 550),  # salida
        ]

        # Generar detalles del pasto: arbustos y piedras
        self.bushes = [(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)) for _ in range(30)]
        self.rocks = [(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)) for _ in range(20)]

    def draw(self, screen):
        screen.fill((34, 139, 34))  # fondo verde pradera

        for bush in self.bushes:
            pygame.draw.circle(screen, (0, 100, 0), bush, 10)

        for rock in self.rocks:
            pygame.draw.circle(screen, (169, 169, 169), rock, 5)

        pygame.draw.lines(screen, (139, 69, 19), False, self.path, 40)
        pygame.draw.lines(screen, (160, 82, 45), False, self.path, 44)

        for point in self.path:
            pygame.draw.circle(screen, (255, 0, 0), point, 5)
