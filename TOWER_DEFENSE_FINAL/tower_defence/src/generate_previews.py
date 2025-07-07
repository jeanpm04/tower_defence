import pygame
import os
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from map1 import Map1
from map2 import Map2
from map3 import Map3

def generate_preview(map_class, filename):
    pygame.init()
    surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_map = map_class()
    game_map.draw(surface)
    preview = pygame.transform.scale(surface, (200, 100))
    pygame.image.save(preview, os.path.join("assets", filename))

if __name__ == "__main__":
    if not os.path.exists("assets"):
        os.makedirs("assets")

    generate_preview(Map1, "preview_map1.png")
    generate_preview(Map2, "preview_map2.png")
    generate_preview(Map3, "preview_map3.png")

    print("Imágenes previas generadas correctamente en la carpeta 'assets'")
    pygame.quit()
