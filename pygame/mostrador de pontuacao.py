import pygame
from pygame.locals import *
#from sys import exit
from random import randint

pygame.init()


largura, altura = 800, 600
x = largura /2
y = altura /2

x_verde = randint(40, 760)
y_verde = randint(40, 560)

pontuacao = 0

fonte = pygame.font.SysFont('arial', 48, True, False)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Meu Jogo Pygame")
relogio = pygame.time.Clock()

#todo jogo deve rodar num loop
running = True 
while running:
    relogio.tick(30) #quantidade de frames por segundo
    mensagem = f'Pontuação: {pontuacao}'
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255)) #false é para suavizar as bordas

    for event in pygame.event.get(): #pega todos os eventos que aconteceram desde a última vez que o comando foi chamado
        if event.type == pygame.QUIT:
            running = False
        if pygame.key.get_pressed()[K_a]:
            x -= 20
        if pygame.key.get_pressed()[K_d]:
            x += 20
        if pygame.key.get_pressed()[K_w]:
            y -= 20
        if pygame.key.get_pressed()[K_s]:
            y += 20
        
        
        tela.fill((0, 0, 0)) #preenche a cor de fundo


        ret_vermelho = pygame.draw.rect(tela, (255,0,0), (x,y,50,60)) #os parametros são organizados da seguinte maneira: onde vai ficar, qual cor vai ter, depois em qual posição ele começa (X e Y) e por fim seu tamanho
        ret_verde = pygame.draw.rect(tela, (0,255,0), (x_verde,y_verde,40,50))
        if ret_vermelho.colliderect(ret_verde):
            x_verde = randint(40, 760)
            y_verde = randint(40, 560)
            pontuacao += 1


        tela.blit(texto_formatado, (10,10))
        pygame.display.update()
    pygame.display.flip()
pygame.quit()