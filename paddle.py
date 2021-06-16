# paddle.py
import pygame
from constants import *

BLUE = (0, 0, 255)

class Paddle:
    MOVE_SPEED = 10

    def __init__(self):
        self.rect = pygame.Rect(0, SCREEN_HEIGHT // 2, 20, 200)

    def move_up(self):
        self.rect.y -= self.MOVE_SPEED
        self._keep_in_bounds()

    def move_down(self):
        self.rect.y += self.MOVE_SPEED
        self._keep_in_bounds()

    def _keep_in_bounds(self):
        self.rect.y = max(self.rect.y, 0)
        self.rect.y = min(self.rect.y, SCREEN_HEIGHT - self.rect.height)

    def draw(self, screen):
        pygame.draw.rect(
            screen, BLUE, self.rect,
        )