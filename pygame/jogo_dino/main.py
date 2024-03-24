import pygame
from pygame.locals import *
from sys import exit
import os
from class_dino import Dino
from class_nuvem import Nuvem
from class_chao import Chao

pygame.init()
pygame.mixer.init()


#controlando os arquivos
diretorio_main = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_main, 'imagens')
diretorio_sons = os.path.join(diretorio_main, 'sons')

# tela
LARGURA, ALTURA = 640, 480
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Dino')
todas_as_sprites = pygame.sprite.Group()
relogio = pygame.time.Clock()

# cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

# spritesheets
sprite_sheet_1 = pygame.image.load(os.path.join(diretorio_imagens, 'dinoSpritesheet.png')).convert_alpha()

# dino
dinossauro = Dino(sprite_sheet_1, LARGURA, ALTURA)  # Cria uma instância da classe Dino
todas_as_sprites.add(dinossauro)

#chao 
for i in range(20):
    chao = Chao(sprite_sheet_1, LARGURA, ALTURA, i)
    todas_as_sprites.add(chao)

#nuvem
for i in range (3):
    nuvem = Nuvem(sprite_sheet_1, LARGURA, ALTURA)
    todas_as_sprites.add(nuvem)

# loop principal
while True:
    relogio.tick(30)
    tela.fill(BRANCO)
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            exit()
        if evento.type == KEYDOWN:
            if evento.key == K_SPACE:
                if dinossauro.rect.y != dinossauro.posic_inicial_Y:
                    pass
                else:
                    dinossauro.pular()
                
    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    pygame.display.flip()
