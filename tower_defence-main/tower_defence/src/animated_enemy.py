# src/animated_enemy.py

import pygame
import math

class AnimatedEnemy:
    def __init__(self, path, sprite_sheet_path, frame_width, frame_height, num_frames, health, speed):
        self.path = path
        self.health = health
        self.max_health = health
        self.speed = speed
        self.alive = True
        self.current_point = 0
        self.x, self.y = path[0]

        # Animación
        self.sprite_sheet = pygame.image.load(sprite_sheet_path).convert_alpha()
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.num_frames = num_frames
        self.frames = []
        self.current_frame = 0
        self.frame_timer = 0
        self.frame_delay = 5  # velocidad de la animación

        self.load_frames()

    def load_frames(self):
        for i in range(self.num_frames):
            frame = self.sprite_sheet.subsurface((i * self.frame_width, 0, self.frame_width, self.frame_height))
            self.frames.append(frame)

    def move(self):
        if not self.alive or self.current_point >= len(self.path) - 1:
            return

        target_x, target_y = self.path[self.current_point + 1]
        dx, dy = target_x - self.x, target_y - self.y
        distance = math.hypot(dx, dy)

        if distance < self.speed:
            self.x, self.y = target_x, target_y
            self.current_point += 1
            if self.current_point >= len(self.path) - 1:
                self.alive = False  # Llega al final
        else:
            self.x += self.speed * dx / distance
            self.y += self.speed * dy / distance

        # Actualizar frame de animación
        self.frame_timer += 1
        if self.frame_timer >= self.frame_delay:
            self.frame_timer = 0
            self.current_frame = (self.current_frame + 1) % self.num_frames

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.alive = False

    def draw(self, screen):
        frame = self.frames[self.current_frame]
        screen.blit(frame, (self.x - self.frame_width // 2, self.y - self.frame_height // 2))

        # Dibujar barra de vida
        bar_width = self.frame_width
        bar_height = 5
        health_ratio = self.health / self.max_health
        pygame.draw.rect(screen, (255, 0, 0), (self.x - bar_width // 2, self.y - self.frame_height // 2 - 10, bar_width, bar_height))
        pygame.draw.rect(screen, (0, 255, 0), (self.x - bar_width // 2, self.y - self.frame_height // 2 - 10, bar_width * health_ratio, bar_height))
