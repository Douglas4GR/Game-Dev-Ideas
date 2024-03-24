import pygame

class Cacto(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet, largura_tela, altura_tela):
        pygame.sprite.Sprite.__init__(self)
        self.largura, self.altura = largura_tela, altura_tela
        indice_X_no_sprite_sheet = 5 #o  está na posicao 5 da imagem
        self.image = sprite_sheet.subsurface((32 * indice_X_no_sprite_sheet, 0), (32, 32))
        self.image = pygame.transform.scale(self.image, (64, 64))
        
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = [largura_tela, altura_tela - 64]
    
    def update(self):
        #se a posição X do topo da direita 
        if self.rect.topright[0] < 0:
            self.rect.x = self.largura
        self.rect.x -= 10 

