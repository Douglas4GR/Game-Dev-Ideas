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

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Meu Jogo Pygame")
relogio = pygame.time.Clock()

#todo jogo deve rodar num loop
running = True 
while running:
    relogio.tick(30) #quantidade de frames por segundo
    for event in pygame.event.get():
        
        tela.fill((255, 255, 255)) #preenche a cor de fundo


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



        ret_vermelho = pygame.draw.rect(tela, (255,0,0), (x,y,50,60)) #os parametros são organizados da seguinte maneira: onde vai ficar, qual cor vai ter, depois em qual posição ele começa (X e Y) e por fim seu tamanho
        ret_verde = pygame.draw.rect(tela, (0,255,0), (x_verde,y_verde,40,50))
        if ret_vermelho.colliderect(ret_verde):
            x_verde = randint(40, 760)
            y_verde = randint(40, 560)
        
        pygame.display.update()
    pygame.display.flip()

pygame.quit()