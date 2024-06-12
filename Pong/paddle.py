# paddle.py
import pygame
from settings import BRANCO, RAQUETE_LARGURA, RAQUETE_ALTURA

class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, RAQUETE_LARGURA, RAQUETE_ALTURA)
        self.speed = 5

    def move(self, dy):
        self.rect.y += dy
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > pygame.display.get_surface().get_height():
            self.rect.bottom = pygame.display.get_surface().get_height()

    def draw(self, screen):
        pygame.draw.rect(screen, BRANCO, self.rect)
