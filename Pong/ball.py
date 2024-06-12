# ball.py
import pygame
from settings import BRANCO, TAMANHO_BOLA, LARGURA, ALTURA, VEL_BOLA

class Ball:
    def __init__(self):
        self.rect = pygame.Rect(LARGURA // 2 - TAMANHO_BOLA // 2, ALTURA // 2 - TAMANHO_BOLA // 2, TAMANHO_BOLA, TAMANHO_BOLA)
        self.vx = VEL_BOLA
        self.vy = VEL_BOLA

    def move(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

        if self.rect.top <= 0 or self.rect.bottom >= ALTURA:
            self.vy = -self.vy

    def draw(self, screen):
        pygame.draw.ellipse(screen, BRANCO, self.rect)

    def reset_position(self):
        self.rect.x = LARGURA // 2 - TAMANHO_BOLA // 2
        self.rect.y = ALTURA // 2 - TAMANHO_BOLA // 2
        self.vx = -self.vx
