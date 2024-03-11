import pygame

class Dino(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet, largura_tela, altura_tela):
        pygame.sprite.Sprite.__init__(self)
        self.largura, self.altura = largura_tela, altura_tela
        self.imagens_dinossauro = []
        self.indice_lista = 0
        proporcoes_dino = 3
        posic_inicial_X, posic_inicial_Y = 100, self.altura - 90

        for i in range(3):
            frame_atual = sprite_sheet.subsurface(((i * 32), 0), (32, 32))
            frame_atual = pygame.transform.scale(frame_atual, (32 * proporcoes_dino, 32 * proporcoes_dino))
            self.imagens_dinossauro.append(frame_atual)

        self.image = self.imagens_dinossauro[self.indice_lista]
        self.rect = self.image.get_rect()
        self.rect.center = (posic_inicial_X, posic_inicial_Y)

    def update(self):
        if self.indice_lista > 2:
            self.indice_lista = 0

        self.indice_lista += 0.25
        self.image = self.imagens_dinossauro[int(self.indice_lista)]
