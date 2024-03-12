import pygame

class Dino(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet, largura_tela, altura_tela):
        pygame.sprite.Sprite.__init__(self)
        self.largura, self.altura = largura_tela, altura_tela
        self.imagens_dinossauro = []
        self.indice_lista = 0
        proporcoes_dino = 3
        posic_inicial_X, posic_inicial_Y = 100, self.altura - 64

        self.pulo = False

        for i in range(3):
            frame_atual = sprite_sheet.subsurface(((i * 32), 0), (32, 32))
            frame_atual = pygame.transform.scale(frame_atual, (32 * proporcoes_dino, 32 * proporcoes_dino))
            self.imagens_dinossauro.append(frame_atual)

        self.image = self.imagens_dinossauro[self.indice_lista]
        self.rect = self.image.get_rect()
        self.rect.center = (posic_inicial_X, posic_inicial_Y)

    def pular(self):
        self.pulo = True

    def update(self):
        if self.pulo == True:
            self.rect.y -= 20
        if self.rect.y == self.altura - 90:
            self.rect.y += 30
            if self.rect.y == self.altura - 64:
                self.pulo = False

        if self.indice_lista > 2:
            self.indice_lista = 0

        self.indice_lista += 0.25
        self.image = self.imagens_dinossauro[int(self.indice_lista)]