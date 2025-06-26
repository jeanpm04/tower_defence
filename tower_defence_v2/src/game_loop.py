import pygame
import sys
import math
import time
import random
from settings import *
from map import Map
from tower import Tower
from projectile import Projectile
from wave_manager import WaveManager

def distance_point_to_segment(px, py, x1, y1, x2, y2):
    line_mag = math.hypot(x2 - x1, y2 - y1)
    if line_mag == 0:
        return math.hypot(px - x1, py - y1)
    u = ((px - x1)*(x2 - x1) + (py - y1)*(py - y1)) / (line_mag**2)
    u = max(min(u, 1), 0)
    ix = x1 + u * (x2 - x1)
    iy = y1 + u * (y2 - y1)
    return math.hypot(px - ix, py - iy)

def is_valid_position(x, y, towers, game_map):
    for tower in towers:
        dist = math.hypot(tower.x - x, tower.y - y)
        if dist < 50:
            return False
    for i in range(len(game_map.path)-1):
        x1, y1 = game_map.path[i]
        x2, y2 = game_map.path[i+1]
        dist = distance_point_to_segment(x, y, x1, y1, x2, y2)
        if dist < 50:
            return False
    return True

def play_sequence_puzzle(screen):
    font = pygame.font.SysFont("Segoe UI Symbol", 80)
    directions = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
    symbols = {
        pygame.K_LEFT: "←",
        pygame.K_RIGHT: "→",
        pygame.K_UP: "↑",
        pygame.K_DOWN: "↓"
    }

    # Generar secuencia aleatoria
    sequence = random.choices(directions, k=4)

    # Mostrar la secuencia con pausas visibles
    for key in sequence:
        screen.fill(BLACK)

        # Dibujar símbolo
        symbol_text = font.render(symbols[key], True, (255, 255, 0))
        screen.blit(
            symbol_text,
            (
                SCREEN_WIDTH // 2 - symbol_text.get_width() // 2,
                SCREEN_HEIGHT // 2 - symbol_text.get_height() // 2
            )
        )
        pygame.display.flip()

        # Mostrar por 700 ms
        pygame.time.delay(700)

        # Pausa entre símbolos (pantalla negra)
        screen.fill(BLACK)
        pygame.display.flip()
        pygame.time.delay(300)

    # Esperar input del usuario
    index = 0
    waiting = True
    while waiting:
        screen.fill(BLACK)
        prompt = font.render("Repite la secuencia...", True, WHITE)
        screen.blit(prompt, (SCREEN_WIDTH // 2 - prompt.get_width() // 2, 100))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "exit"
            if event.type == pygame.KEYDOWN:
                if event.key == sequence[index]:
                    index += 1
                    if index == len(sequence):
                        return "success"
                else:
                    return "fail"

def run_game(screen):
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
    paused = False
    speed_multiplier = 1
    total_start_time = time.time()
    floating_texts = []
    enemies_killed = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "exit"

            if not game_over and not victory:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not paused:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if not invalid_position and money >= TOWER_COST:
                        towers.append(Tower(mouse_x, mouse_y))
                        money -= TOWER_COST

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and wave_manager.is_wave_clear() and not paused:
                        result = play_sequence_puzzle(screen)
                        if result == "exit":
                            return "exit"
                        elif result == "success":
                            money += 100
                            floating_texts.append({"text": "+100 BONUS", "x": 300, "y": 300, "timer": 60})
                        if wave_manager.wave_number < wave_manager.max_rounds:
                            wave_manager.next_wave()
                        else:
                            victory = True
                    if event.key == pygame.K_p:
                        paused = not paused
                    if event.key == pygame.K_f:
                        speed_multiplier = 3 if speed_multiplier == 1 else 1

        screen.fill(WHITE)
        game_map.draw(screen)

        if not game_over and not victory and not paused:
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
                    enemies_killed += 1
                    floating_texts.append({"text": "+25", "x": enemy.x, "y": enemy.y, "timer": 30})
                enemy.draw(screen)
            wave_manager.enemies = new_enemies

            for tower in towers:
                tower.attack(wave_manager.enemies, projectiles)
                tower.draw(screen)

            for projectile in projectiles:
                projectile.move()
                projectile.draw(screen)

            projectiles = [p for p in projectiles if p.alive]

            for text in floating_texts:
                font = pygame.font.SysFont(None, 20)
                surf = font.render(text["text"], True, (255, 255, 0))
                screen.blit(surf, (text["x"], text["y"] - (30 - text["timer"])))
                text["timer"] -= 1
            floating_texts = [t for t in floating_texts if t["timer"] > 0]

            mouse_x, mouse_y = pygame.mouse.get_pos()
            invalid_position = not is_valid_position(mouse_x, mouse_y, towers, game_map)

            color = (255, 0, 0) if invalid_position or money < TOWER_COST else (0, 255, 0)
            pygame.draw.circle(screen, color, (mouse_x, mouse_y), 20, 2)

            font = pygame.font.SysFont(None, 30)
            screen.blit(font.render(f"Wave: {wave_manager.wave_number}", True, BLACK), (10, 10))
            screen.blit(font.render(f"Money: ${money}", True, BLACK), (10, 40))
            screen.blit(font.render(f"Lives: {lives}", True, BLACK), (10, 70))
            screen.blit(font.render(f"Speed: x{speed_multiplier}", True, (0, 0, 255)), (10, 100))

            if wave_manager.total_enemies > 0:
                spawned = wave_manager.total_enemies - wave_manager.enemies_to_spawn
                progress = spawned / wave_manager.total_enemies
                pygame.draw.rect(screen, (0, 0, 0), (200, 10, 400, 20))
                pygame.draw.rect(screen, (0, 255, 0), (200, 10, int(400 * progress), 20))

            if lives <= 0:
                game_over = True

        elif paused:
            font = pygame.font.SysFont(None, 60)
            pause_text = font.render("PAUSADO", True, (255, 0, 0))
            screen.blit(pause_text, (SCREEN_WIDTH // 2 - pause_text.get_width() // 2, 150))
            menu_button = pygame.Rect(SCREEN_WIDTH // 2 - 120, 250, 240, 50)
            pygame.draw.rect(screen, (50, 50, 50), menu_button)
            pygame.draw.rect(screen, (255, 255, 255), menu_button, 2)
            btn_font = pygame.font.SysFont(None, 32)
            btn_text = btn_font.render("Volver al Menú", True, (255, 255, 255))
            screen.blit(btn_text, (menu_button.x + 120 - btn_text.get_width() // 2, menu_button.y + 10))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "exit"
                if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    paused = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if menu_button.collidepoint(pygame.mouse.get_pos()):
                        return "menu"

        if game_over or victory:
            total_time = int(time.time() - total_start_time)
            font = pygame.font.SysFont(None, 50)
            result = "VICTORY!" if victory else "GAME OVER"
            result_color = (0, 150, 0) if victory else (200, 0, 0)
            result_text = font.render(result, True, result_color)
            screen.blit(result_text, (SCREEN_WIDTH // 2 - result_text.get_width() // 2, 150))

            score_font = pygame.font.SysFont(None, 35)
            screen.blit(score_font.render(f"Tiempo total: {total_time}s", True, BLACK), (200, 250))
            screen.blit(score_font.render(f"Dinero final: ${money}", True, BLACK), (200, 300))
            screen.blit(score_font.render(f"Enemigos eliminados: {enemies_killed}", True, BLACK), (200, 350))
            screen.blit(score_font.render(f"Vidas restantes: {lives}", True, BLACK), (200, 400))
            screen.blit(score_font.render("Presiona R para reiniciar", True, (50, 50, 50)), (200, 480))
            pygame.display.flip()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                return run_game(screen)

        pygame.display.flip()
        clock.tick(FPS * speed_multiplier)

    return "exit"
