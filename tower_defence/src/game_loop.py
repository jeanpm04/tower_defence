# src/game_loop.py

import pygame
import sys
import math
from settings import *
from map import Map
from tower import Tower
from projectile import Projectile
from wave_manager import WaveManager

def is_valid_position(x, y, towers, game_map):
    for tower in towers:
        dist = math.hypot(tower.x - x, tower.y - y)
        if dist < 50:
            return False
    for point in game_map.path:
        dist = math.hypot(point[0] - x, point[1] - y)
        if dist < 40:
            return False
    return True

def run_game():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    game_map = Map()
    towers = []
    projectiles = []
    wave_manager = WaveManager(game_map.path)
    money = STARTING_MONEY
    lives = STARTING_LIVES
    invalid_position = False

    running = True
    game_over = False
    victory = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if not game_over and not victory:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if not invalid_position and money >= TOWER_COST:
                        towers.append(Tower(mouse_x, mouse_y))
                        money -= TOWER_COST

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and wave_manager.is_wave_clear():
                        if wave_manager.wave_number < wave_manager.max_rounds:
                            wave_manager.next_wave()
                        else:
                            victory = True

        screen.fill(WHITE)
        game_map.draw(screen)

        if not game_over and not victory:
            wave_manager.update()

            new_enemies = []
            for enemy in wave_manager.enemies:
                previous_alive = enemy.alive
                enemy.move()
                if not enemy.alive and previous_alive and enemy.current_point + 1 >= len(enemy.path):
                    lives -= 1
                elif enemy.alive:
                    new_enemies.append(enemy)
                else:
                    money += REWARD_PER_KILL

                enemy.draw(screen)

            wave_manager.enemies = new_enemies

            for tower in towers:
                tower.attack(wave_manager.enemies, projectiles)
                tower.draw(screen)

            for projectile in projectiles:
                projectile.move()
                projectile.draw(screen)

            projectiles = [p for p in projectiles if p.alive]

            mouse_x, mouse_y = pygame.mouse.get_pos()
            invalid_position = not is_valid_position(mouse_x, mouse_y, towers, game_map)

            color = (255, 0, 0) if invalid_position or money < TOWER_COST else (0, 255, 0)
            pygame.draw.circle(screen, color, (mouse_x, mouse_y), 20, 2)

            font = pygame.font.SysFont(None, 30)
            text_wave = font.render(f"Wave: {wave_manager.wave_number}", True, BLACK)
            text_money = font.render(f"Money: ${money}", True, BLACK)
            text_lives = font.render(f"Lives: {lives}", True, BLACK)

            screen.blit(text_wave, (10, 10))
            screen.blit(text_money, (10, 40))
            screen.blit(text_lives, (10, 70))

            if lives <= 0:
                game_over = True

        if game_over:
            game_over_font = pygame.font.SysFont(None, 60)
            game_over_text = game_over_font.render("GAME OVER", True, (200, 0, 0))
            screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 30))
            pygame.display.flip()
            pygame.time.delay(3000)
            running = False

        if victory:
            victory_font = pygame.font.SysFont(None, 60)
            victory_text = victory_font.render("VICTORY!", True, (0, 150, 0))
            screen.blit(victory_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 30))
            pygame.display.flip()
            pygame.time.delay(3000)
            running = False

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()
