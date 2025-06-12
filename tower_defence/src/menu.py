# src/menu.py

import pygame
import sys
from settings import *

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font_title = pygame.font.SysFont("Arial", 60)
        self.font_button = pygame.font.SysFont("Arial", 40)
        self.buttons = {
            "start": pygame.Rect(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2, 200, 60),
            "quit": pygame.Rect(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 + 80, 200, 60)
        }

    def draw(self):
        self.screen.fill((30, 30, 30))
        title_surface = self.font_title.render("Tower Defense", True, (255, 215, 0))
        self.screen.blit(title_surface, (SCREEN_WIDTH//2 - title_surface.get_width()//2, 150))

        for name, rect in self.buttons.items():
            pygame.draw.rect(self.screen, (50, 50, 50), rect)
            pygame.draw.rect(self.screen, (200, 200, 200), rect, 3)
            text = "Iniciar Juego" if name == "start" else "Salir"
            text_surface = self.font_button.render(text, True, (255, 255, 255))
            self.screen.blit(text_surface, (rect.x + rect.width//2 - text_surface.get_width()//2, rect.y + 10))

        pygame.display.flip()

    def run(self):
        while True:
            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.buttons["start"].collidepoint(mouse_pos):
                        return  # Sale del menú y empieza el juego
                    if self.buttons["quit"].collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()
