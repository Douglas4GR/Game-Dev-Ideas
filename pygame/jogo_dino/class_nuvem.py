import pygame

class Nuvem(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet, largura_tela, altura_tela):
        pygame.sprite.Sprite.__init__(self)
        self.largura, self.altura = largura_tela, altura_tela
        proporcoes_nuvem = 3
        posic_inicial_X, posic_inicial_Y = 50, 50
        indice_X_no_sprite_sheet = 7 #a nuvem está na setima posicao da imagem
        self.image = sprite_sheet.subsurface((32 * indice_X_no_sprite_sheet, 0), (32, 32))
        self.image = pygame.transform.scale(self.image, (32 * proporcoes_nuvem, 32 * proporcoes_nuvem))
        
        self.rect = self.image.get_rect()
        self.rect.center = (posic_inicial_X, posic_inicial_Y)

    def update(self):
        #se a posição X do topo da direita 
        if self.rect.topright[0] < 0:
            self.rect.x = self.largura
        self.rect.x -= 10 
