# src/menu.py

import pygame
import sys
from settings import *

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font_title = pygame.font.SysFont("Arial", 60)
        self.font_button = pygame.font.SysFont("Arial", 40)
        self.font_instructions = pygame.font.SysFont("Arial", 30)
        self.buttons = {
            "start": pygame.Rect(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2, 200, 60),
            "instructions": pygame.Rect(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 + 80, 200, 60),
            "quit": pygame.Rect(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 + 160, 200, 60)
        }

    def draw(self):
        self.screen.fill((30, 30, 30))
        title_surface = self.font_title.render("Tower Defense", True, (255, 215, 0))
        self.screen.blit(title_surface, (SCREEN_WIDTH//2 - title_surface.get_width()//2, 150))

        for name, rect in self.buttons.items():
            pygame.draw.rect(self.screen, (50, 50, 50), rect)
            pygame.draw.rect(self.screen, (200, 200, 200), rect, 3)
            text = {
                "start": "Iniciar Juego",
                "instructions": "Instrucciones",
                "quit": "Salir"
            }[name]
            text_surface = self.font_button.render(text, True, (255, 255, 255))
            self.screen.blit(text_surface, (rect.x + rect.width//2 - text_surface.get_width()//2, rect.y + 10))

        pygame.display.flip()

    def show_instructions(self):
        showing = True
        while showing:
            self.screen.fill((20, 20, 20))
            title_surface = self.font_title.render("Instrucciones", True, (255, 215, 0))
            self.screen.blit(title_surface, (SCREEN_WIDTH//2 - title_surface.get_width()//2, 100))

            instructions = [
                "ESPACIO - Iniciar siguiente oleada",
                "P - Pausar / Reanudar",
                "F - Aumentar velocidad (x3)",
                "CLICK IZQUIERDO - Colocar torre",
                "Cada ola incluirá un puzzle: si lo resuelves, ganarás $100",
                "",
                "Presione ESC para volver al menú"
            ]

            for i, line in enumerate(instructions):
                text_surface = self.font_instructions.render(line, True, (255, 255, 255))
                self.screen.blit(text_surface, (SCREEN_WIDTH//2 - text_surface.get_width()//2, 200 + i * 40))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    showing = False

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
                    if self.buttons["instructions"].collidepoint(mouse_pos):
                        self.show_instructions()
                    if self.buttons["quit"].collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()
