import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Definindo as dimensões da tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Personagem de Anime")

# Definindo as cores
branco = (255, 255, 255)
preto = (0, 0, 0)
azul = (0, 0, 255)
rosa = (255, 182, 193)
verde = (0, 255, 0)

# Loop principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Desenhar a personagem
    tela.fill(branco)  # Preencher a tela com fundo branco

    # Cabeça
    pygame.draw.circle(tela, rosa, (400, 300), 50)

    # Olhos
    pygame.draw.circle(tela, preto, (385, 290), 5)
    pygame.draw.circle(tela, preto, (415, 290), 5)

    # Boca
    pygame.draw.arc(tela, preto, (385, 290, 30, 20), 0.7, 2.4, 2)

    # Cabelo
    pygame.draw.polygon(tela, azul, [(400, 250), (370, 280), (430, 280)])

    # Corpo
    pygame.draw.rect(tela, verde, (380, 320, 40, 80))

    # Braços
    pygame.draw.line(tela, azul, (380, 330), (350, 360), 5)
    pygame.draw.line(tela, azul, (420, 330), (450, 360), 5)

    # Pernas
    pygame.draw.line(tela, azul, (400, 400), (370, 450), 5)
    pygame.draw.line(tela, azul, (400, 400), (430, 450), 5)

    pygame.display.flip()
