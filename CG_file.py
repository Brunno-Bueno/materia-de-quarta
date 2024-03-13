import sys
import pygame
import random

pygame.init()

# Configuração da tela
largura = 800
altura = 600

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pygame")

cor_texto = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
ROXO = (128, 0, 128)
VERDE = (0, 255, 0)
AMARELO = (255, 255, 0)

tamanho_fonte = 50
fonte = pygame.font.SysFont(None, tamanho_fonte)
palavra = "Bruno"
texto = fonte.render(palavra, True, cor_texto)

texto_rect = texto.get_rect(center=(largura / 2, altura / 2))
clock = pygame.time.Clock()  # Relogio para controlar a velocidade do jogo

# velocidade_x = 1
# velocidade_y = -1



velocidade_x = random.randint(-1, 1)
velocidade_y = random.randint(-1, 1)

while velocidade_x == 0:
    velocidade_x = random.randint(-1, 1)
while velocidade_y == 0:
    velocidade_y = random.randint(-1, 1)

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    texto_rect.x += velocidade_x
    texto_rect.y += velocidade_y

    if texto_rect.left <= 0:
        velocidade_x = random.randint(0, 1)
        velocidade_y = random.randint(-1, 1)
        cor_texto = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        texto = fonte.render(palavra, True, cor_texto)

    if texto_rect.right >= 800:
        velocidade_x = random.randint(-1, 0)
        velocidade_y = random.randint(-1, 1)
        cor_texto = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        texto = fonte.render(palavra, True, cor_texto)

    if texto_rect.top <= 0:
        velocidade_x = random.randint(-1, 1)
        velocidade_y = random.randint(0, 1)
        cor_texto = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        texto = fonte.render(palavra, True, cor_texto)

    if texto_rect.bottom >= 600:
        velocidade_x = random.randint(-1, 1)
        velocidade_y = random.randint(-1, 0)
        cor_texto = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        texto = fonte.render(palavra, True, cor_texto)


    clock.tick(120)
    tela.fill(PRETO)
    tela.blit(texto, texto_rect)
    pygame.display.flip()