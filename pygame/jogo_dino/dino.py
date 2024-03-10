import pygame
from pygame.locals import *
from sys import exit
import os #biblioteca para manipular arquivos

diretorio_main = os.path.dirname(__file__) #diretório do arquivo
diretorio_imagens = os.path.join(diretorio_main, 'imagens')
diretorio_sons = os.path.join(diretorio_main, 'sons')

#tela
LARGURA = 640
ALTURA = 480
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Dino')
todas_as_sprites = pygame.sprite.Group()
relogio = pygame.time.Clock()

#spritesheets
sprite_sheet_1 = pygame.image.load(os.path.join(diretorio_imagens,'dinoSpritesheet.png')).convert_alpha()

#cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

#dino
class Dino(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_dinossauro = []
        for i in range(3):
            frame_atual = sprite_sheet_1.subsurface(((i * 32),0),(32,32))
            self.imagens_dinossauro.append(frame_atual)
        
        self.indice_lista = 0
        self.image = self.imagens_dinossauro[self.indice_lista]
        self.rect = self.image.get_rect()
        self.rect.center = (100,100)

    def update(self):
        if self.indice_lista > 2:
            self.indice_lista = 0

        self.indice_lista += 0.25
        self.image = self.imagens_dinossauro[int(self.indice_lista)]


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