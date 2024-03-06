import pygame
from pygame.locals import *
from sys import exit

#tela
LARGURA = 640
ALTURA = 480
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Dino')
todas_as_sprites = pygame.sprite.Group()
relogio = pygame.time.Clock()

#cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

#dino
class Dino(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pass 

dinossauro = Dino()
todas_as_sprites.add(dinossauro)


#loop principal
while True:
    relogio.tick(30)
    tela.fill(BRANCO)
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            exit()


    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    pygame.display.flip()