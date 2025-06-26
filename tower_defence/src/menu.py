import pygame
import sys
import math
import random
from settings import *
from map1 import Map1  # usamos Map1 como fondo
from enemy import Enemy

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.font_title = pygame.font.SysFont("Arial", 60, bold=True)
        self.font_button = pygame.font.SysFont("Arial", 35)
        self.font_instructions = pygame.font.SysFont("Arial", 28)
        self.map = Map1()  # reemplaza al antiguo Map
        self.enemies = [Enemy(path=self.map.path, health=30, speed=0.5) for _ in range(6)]
        self.title_y_offset = 0
        self.title_direction = 1

        self.buttons = {
            "start": pygame.Rect(SCREEN_WIDTH//2 - 120, SCREEN_HEIGHT//2 + 30, 240, 55),
            "instructions": pygame.Rect(SCREEN_WIDTH//2 - 120, SCREEN_HEIGHT//2 + 110, 240, 55),
            "quit": pygame.Rect(SCREEN_WIDTH//2 - 120, SCREEN_HEIGHT//2 + 190, 240, 55)
        }

    def draw_background(self):
        self.map.draw(self.screen)
        for enemy in self.enemies:
            enemy.move()
            enemy.draw(self.screen)

        dark_overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        dark_overlay.set_alpha(180)
        dark_overlay.fill((0, 0, 0))
        self.screen.blit(dark_overlay, (0, 0))

    def draw_title(self):
        title = "Tower Defense"
        color = (255, 215, 0)
        title_surface = self.font_title.render(title, True, color)
        self.title_y_offset += self.title_direction * 0.2
        if self.title_y_offset > 5 or self.title_y_offset < -5:
            self.title_direction *= -1
        x = SCREEN_WIDTH//2 - title_surface.get_width()//2
        y = 100 + int(self.title_y_offset)
        self.screen.blit(title_surface, (x, y))

    def draw_buttons(self, mouse_pos):
        for name, rect in self.buttons.items():
            hovering = rect.collidepoint(mouse_pos)
            scale = 1.05 if hovering else 1
            scaled_width = int(rect.width * scale)
            scaled_height = int(rect.height * scale)
            scaled_rect = pygame.Rect(
                rect.centerx - scaled_width // 2,
                rect.centery - scaled_height // 2,
                scaled_width,
                scaled_height
            )

            bg_color = (100, 100, 100, 230) if hovering else (60, 60, 60, 160)
            button_surface = pygame.Surface((scaled_rect.width, scaled_rect.height), pygame.SRCALPHA)
            button_surface.fill(bg_color)
            self.screen.blit(button_surface, (scaled_rect.x, scaled_rect.y))

            pygame.draw.rect(self.screen, (200, 200, 200), scaled_rect, 2)

            text = {
                "start": "Iniciar Juego",
                "instructions": "Instrucciones",
                "quit": "Salir"
            }[name]
            text_surface = self.font_button.render(text, True, (255, 255, 255))
            self.screen.blit(text_surface, (
                scaled_rect.centerx - text_surface.get_width() // 2,
                scaled_rect.centery - text_surface.get_height() // 2
            ))

    def show_instructions(self):
        showing = True
        while showing:
            self.draw_background()
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
                self.screen.blit(text_surface, (SCREEN_WIDTH//2 - text_surface.get_width()//2, 200 + i * 35))

            pygame.display.flip()
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    showing = False

    def run(self):
        while True:
            mouse_pos = pygame.mouse.get_pos()
            self.draw_background()
            self.draw_title()
            self.draw_buttons(mouse_pos)

            pygame.display.flip()
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.buttons["start"].collidepoint(mouse_pos):
                        return
                    elif self.buttons["instructions"].collidepoint(mouse_pos):
                        self.show_instructions()
                    elif self.buttons["quit"].collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()
