# src/main.py

import pygame
from menu import Menu
from game_loop import run_game
from settings import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(GAME_TITLE)

    while True:
        menu = Menu(screen)
        menu.run()

        result = run_game(screen)
        if result == "menu":
            continue  # Regresa al menú principal
        elif result == "exit":
            break

    pygame.quit()

if __name__ == "__main__":
    main()
