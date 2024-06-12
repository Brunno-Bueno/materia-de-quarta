# menu.py
import pygame
import sys
from settings import PRETO, BRANCO, FONT_FILE, LARGURA, ALTURA

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(FONT_FILE, 36)

    def main_menu(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return

            self.screen.fill(PRETO)
            texto_menu = self.font.render("Pong", True, BRANCO)
            text_menu_rect = texto_menu.get_rect(center=(LARGURA // 2, ALTURA // 2))
            self.screen.blit(texto_menu, text_menu_rect)

            tempo = pygame.time.get_ticks()
            if tempo % 2000 < 1000:
                texto_iniciar = self.font.render("Pressione Espaço", True, BRANCO)
                texto_iniciar_rect = texto_iniciar.get_rect(center=(LARGURA // 2, 450))
                self.screen.blit(texto_iniciar, texto_iniciar_rect)

            pygame.display.flip()

    def game_over(self, winner):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return

            self.screen.fill(PRETO)
            texto_fim = self.font.render(f"Vencedor: {winner}", True, BRANCO)
            text_fim_rect = texto_fim.get_rect(center=(LARGURA // 2, ALTURA // 2))
            self.screen.blit(texto_fim, text_fim_rect)

            pygame.display.flip()
