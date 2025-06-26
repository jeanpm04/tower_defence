# src/main.py

import pygame
from menu import Menu
from game_loop import run_game
from settings import *
from map1 import Map1
from map2 import Map2
from map3 import Map3
from game_loop import run_game
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(GAME_TITLE)

    while True:
        menu = Menu(screen)
        menu.run()

        selected_map = choose_map(screen)  # <<-- SE AGREGA ESTA LÍNEA
        result = run_game(screen, selected_map)  # <<-- SE MODIFICA ESTA LÍNEA

        if result == "menu":
            continue  # Regresa al menú principal
        elif result == "exit":
            break

    pygame.quit()

def choose_map(screen):
    import pygame
    import sys
    font = pygame.font.SysFont(None, 28)
    running = True

    # Cargar imágenes de los mapas
    img1 = pygame.image.load("assets/preview_map1.png")
    img2 = pygame.image.load("assets/preview_map2.png")
    img3 = pygame.image.load("assets/preview_map3.png")

    # Redimensionar
    img1 = pygame.transform.scale(img1, (160, 100))
    img2 = pygame.transform.scale(img2, (160, 100))
    img3 = pygame.transform.scale(img3, (160, 100))

    # Imagen de “próximamente”
    coming_soon_img = pygame.Surface((160, 100))
    coming_soon_img.fill((60, 60, 60))
    soon_font = pygame.font.SysFont(None, 22)
    soon_text = soon_font.render("Próximamente", True, (200, 200, 200))
    coming_soon_img.blit(soon_text, (
        coming_soon_img.get_width() // 2 - soon_text.get_width() // 2,
        coming_soon_img.get_height() // 2 - soon_text.get_height() // 2
    ))

    map_classes = [Map1, Map2, Map3]
    map_names = ["Mapa 1", "Mapa 2", "Mapa 3"]
    map_imgs = [img1, img2, img3]

    while running:
        screen.fill((30, 30, 30))
        title = font.render("Selecciona un mapa", True, (255, 255, 255))
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 30))

        buttons = []

        # --- Dibujar mapas disponibles ---
        for i in range(3):
            x = 100 + i * 220  # espaciado horizontal
            y = 80
            screen.blit(map_imgs[i], (x, y))

            btn_rect = pygame.Rect(x, y + 110, 160, 40)
            buttons.append((btn_rect, map_classes[i]))
            pygame.draw.rect(screen, (70, 70, 200), btn_rect)
            pygame.draw.rect(screen, (255, 255, 255), btn_rect, 2)

            # Texto centrado dentro del botón
            btn_text = font.render(map_names[i], True, (255, 255, 255))
            screen.blit(btn_text, (
                btn_rect.x + btn_rect.width // 2 - btn_text.get_width() // 2,
                btn_rect.y + btn_rect.height // 2 - btn_text.get_height() // 2
            ))

        # --- Dibujar mapas “próximamente” ---
        for i in range(3):
            x = 100 + i * 220
            y = 270
            screen.blit(coming_soon_img, (x, y))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for btn, map_class in buttons:
                    if btn.collidepoint(event.pos):
                        return map_class()

if __name__ == "__main__":
    main()
