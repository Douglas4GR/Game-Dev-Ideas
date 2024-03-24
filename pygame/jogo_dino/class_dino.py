import pygame
import os

diretorio_main = os.path.dirname(__file__)
diretorio_sons = os.path.join(diretorio_main, 'sons')

class Dino(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet, largura_tela, altura_tela):
        pygame.sprite.Sprite.__init__(self)
        self.som_pulo = pygame.mixer.Sound(os.path.join(diretorio_sons, 'sons_jump_sound.wav'))
        self.som_pulo.set_volume(1)
        
        self.largura, self.altura = largura_tela, altura_tela
        self.imagens_dinossauro = []
        self.indice_lista = 0
        proporcoes_dino = 3
        self.posic_inicial_X, self.posic_inicial_Y = 100, self.altura - 64 - 42

        self.pulo = False

        for i in range(3):
            frame_atual = sprite_sheet.subsurface(((i * 32), 0), (32, 32))
            frame_atual = pygame.transform.scale(frame_atual, (32 * proporcoes_dino, 32 * proporcoes_dino))
            self.imagens_dinossauro.append(frame_atual)

        self.image = self.imagens_dinossauro[self.indice_lista]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image) #superfície de colisão
        self.rect.center = (self.posic_inicial_X, self.posic_inicial_Y)

    def pular(self):
        self.pulo = True
        self.som_pulo.play()

    def update(self):
        if self.pulo == True:
            if self.rect.y <= 200:
                self.pulo = False
            self.rect.y -= 20
        else:
            if self.rect.y < self.posic_inicial_Y:
                self.rect.y += 30
            else:
                self.rect.y = self.posic_inicial_Y

        if self.indice_lista > 2:
            self.indice_lista = 0

        self.indice_lista += 0.25
        self.image = self.imagens_dinossauro[int(self.indice_lista)]