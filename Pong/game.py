# game.py
import pygame
import sys
from settings import PRETO, BRANCO, LARGURA, ALTURA, FONT_FILE, VEL_RAQUETE, RAQUETE_ALTURA
from paddle import Paddle
from ball import Ball
from menu import Menu

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption("Pong")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(FONT_FILE, 16)

        self.paddle1 = Paddle(LARGURA - 20, ALTURA // 2 - RAQUETE_ALTURA // 2)
        self.paddle2 = Paddle(10, ALTURA // 2 - RAQUETE_ALTURA // 2)
        self.ball = Ball()
        self.menu = Menu(self.screen)
        self.score1 = 0
        self.score2 = 0

    def reset(self):
        self.paddle1 = Paddle(LARGURA - 20, ALTURA // 2 - RAQUETE_ALTURA // 2)
        self.paddle2 = Paddle(10, ALTURA // 2 - RAQUETE_ALTURA // 2)
        self.ball = Ball()

    def run(self):
        self.menu.main_menu()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] and self.paddle1.rect.top > 0:
                self.paddle1.move(-VEL_RAQUETE)
            if keys[pygame.K_DOWN] and self.paddle1.rect.bottom < ALTURA:
                self.paddle1.move(VEL_RAQUETE)

            self.paddle2.rect.centery = self.ball.rect.centery

            self.ball.move()

            if self.ball.rect.colliderect(self.paddle1.rect) or self.ball.rect.colliderect(self.paddle2.rect):
                self.ball.vx = -self.ball.vx

            if self.ball.rect.left <= 0:
                self.score1 += 1
                self.ball.reset_position()

            if self.ball.rect.right >= LARGURA:
                self.score2 += 1
                self.ball.reset_position()

            if self.score1 == 5:
                self.menu.game_over("Player 1")
                self.reset()
                self.score1, self.score2 = 0, 0
                self.menu.main_menu()

            if self.score2 == 5:
                self.menu.game_over("PC")
                self.reset()
                self.score1, self.score2 = 0, 0
                self.menu.main_menu()

            self.screen.fill(PRETO)
            self.paddle1.draw(self.screen)
            self.paddle2.draw(self.screen)
            self.ball.draw(self.screen)

            score_text = self.font.render(f"Player 1: {self.score1}  PC: {self.score2}", True, BRANCO)
            self.screen.blit(score_text, (LARGURA // 2 - score_text.get_width() // 2, 30))

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()
