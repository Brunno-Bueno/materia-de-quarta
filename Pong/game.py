import pygame
from paddle import Paddle
from ball import Ball
import sys

class Game:
    def __init__(self):
        pygame.init()

        self.PRETO = (0, 0, 0)
        self.BRANCO = (255, 255, 255)
        self.largura = 800
        self.altura = 600
        self.screen = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("Pong")

        self.raquete_largura = 10
        self.raquete_altura = 60
        self.tamanho_bola = 10
        self.raquete_player_1_dy = 5
        self.raquete_pc_dy = 5
        self.velocidade_bola_x = 3
        self.velocidade_bola_y = 3
        self.vencedor = ""
        self.controle = False
        self.rodando = True

        self.font_file = "font/PressStart2P-Regular.ttf"
        self.font = pygame.font.Font(self.font_file, 36)
        self.clock = pygame.time.Clock()

        self.pc_paddle = Paddle(10, self.altura // 2 - self.raquete_altura // 2, self.raquete_largura, self.raquete_altura, self.raquete_pc_dy)
        self.player_paddle = Paddle(self.largura - 20, self.altura // 2 - self.raquete_altura // 2, self.raquete_largura, self.raquete_altura, self.raquete_player_1_dy)
        self.balls = [Ball(self.largura // 2 - self.tamanho_bola // 2, self.altura // 2 - self.tamanho_bola // 2, self.tamanho_bola, self.velocidade_bola_x, self.velocidade_bola_y)]

        self.start_time = pygame.time.get_ticks()

    def menu_principal(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.controle = True
                        self.start_time = pygame.time.get_ticks()  # Reiniciar o tempo ao iniciar o jogo
                        return
            self.screen.fill(self.PRETO)
            texto_menu = self.font.render("Pong", True, self.BRANCO)
            text_menu_rect = texto_menu.get_rect(center=(self.largura // 2, self.altura // 2))
            self.screen.blit(texto_menu, text_menu_rect)

            tempo = pygame.time.get_ticks()
            if tempo % 2000 < 1000:
                texto_iniciar = self.font.render("Pressione Espaço", True, self.BRANCO)
                texto_iniciar_rect = texto_iniciar.get_rect(center=(self.largura // 2, 450))
                self.screen.blit(texto_iniciar, texto_iniciar_rect)

            self.clock.tick(60)
            pygame.display.flip()

    def posicao_inicial(self):
        self.pc_paddle.reset_position(self.altura // 2 - self.raquete_altura // 2)
        self.player_paddle.reset_position(self.altura // 2 - self.raquete_altura // 2)
        self.balls = [Ball(self.largura // 2 - self.tamanho_bola // 2, self.altura // 2 - self.tamanho_bola // 2, self.tamanho_bola, self.velocidade_bola_x, self.velocidade_bola_y)]

    def fim_jogo(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.controle = False
                        self.vencedor = ""
                        return
            self.screen.fill(self.PRETO)
            texto_fim = self.font.render(f"Vencedor: {self.vencedor}", True, self.BRANCO)
            text_fim_rect = texto_fim.get_rect(center=(self.largura // 2, self.altura // 2))
            self.screen.blit(texto_fim, text_fim_rect)

            pygame.display.flip()

    def run(self):
        self.menu_principal()
        self.posicao_inicial()

        while self.rodando:
            if self.controle:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.rodando = False

                self.screen.fill(self.PRETO)

                # Movendo as bolas
                for ball in self.balls:
                    ball.move()

                # Adicionar segunda bola após 15 segundos
                current_time = pygame.time.get_ticks()
                if current_time - self.start_time > 15000 and len(self.balls) == 1:
                    self.balls.append(Ball(self.largura // 2 - self.tamanho_bola // 2, self.altura // 2 - self.tamanho_bola // 2, self.tamanho_bola, self.velocidade_bola_x, self.velocidade_bola_y))

                for ball in self.balls:
                    # Retângulos de Colisão
                    ball_rect = pygame.Rect(ball.x, ball.y, ball.size, ball.size)
                    raquete_pc_rect = pygame.Rect(self.pc_paddle.x, self.pc_paddle.y, self.pc_paddle.width, self.pc_paddle.height)
                    raquete_player_1_rect = pygame.Rect(self.player_paddle.x, self.player_paddle.y, self.player_paddle.width, self.player_paddle.height)

                    # Colisão da bola com a raquete do pc e a raquete do player
                    if ball_rect.colliderect(raquete_pc_rect) or ball_rect.colliderect(raquete_player_1_rect):
                        ball.speed_x = -ball.speed_x

                    # Colisão da bola com as bordas da tela
                    if ball.y <= 0 or ball.y >= self.altura - ball.size:
                        ball.speed_y = -ball.speed_y

                    # Posicionar a bola no inicio do jogo
                    if ball.x <= 0:
                        ball.reset_position(self.largura // 2 - self.tamanho_bola // 2, self.altura // 2 - self.tamanho_bola // 2)
                        ball.speed_x = -ball.speed_x
                        self.player_paddle.score += 1
                        if self.player_paddle.score == 5:
                            self.vencedor = "Player 1"
                            self.controle = False

                    if ball.x >= self.largura - ball.size:
                        ball.reset_position(self.largura // 2 - self.tamanho_bola // 2, self.altura // 2 - self.tamanho_bola // 2)
                        ball.speed_x = -ball.speed_x
                        self.pc_paddle.score += 1
                        if self.pc_paddle.score == 5:
                            self.vencedor = "PC"
                            self.controle = False

                # Movendo a raquete do pc para seguir a bola
                self.pc_paddle.move_auto(self.altura, self.balls[0].y)

                # Controle Teclado do Player_1
                keys = pygame.key.get_pressed()
                self.player_paddle.move(keys, self.altura)

                # Mostrando Score no jogo
                fonte_score = pygame.font.Font(self.font_file, 16)
                score_texto = fonte_score.render(f"Score PC: {self.pc_paddle.score}       Score Player_1: {self.player_paddle.score}", True, self.BRANCO)
                score_rect = score_texto.get_rect(center=(self.largura // 2, 30))

                self.screen.blit(score_texto, score_rect)

                # assets (objetos)
                self.pc_paddle.draw(self.screen, self.BRANCO)
                self.player_paddle.draw(self.screen, self.BRANCO)
                for ball in self.balls:
                    ball.draw(self.screen, self.BRANCO)
                pygame.draw.aaline(self.screen, self.BRANCO, (self.largura // 2, 0), (self.largura // 2, self.altura))

                pygame.display.flip()
                self.clock.tick(60)
            else:
                self.fim_jogo()
                self.posicao_inicial()
                self.menu_principal()

        pygame.quit()
        sys.exit()
