import pygame

class Chao(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet, largura_tela, altura_tela, posic_X):
        pygame.sprite.Sprite.__init__(self)
        self.largura, self.altura = largura_tela, altura_tela
        indice_X_no_sprite_sheet = 6 #a chao está na setima posicao da imagem
        self.image = sprite_sheet.subsurface((32 * indice_X_no_sprite_sheet, 0), (32, 32))
        self.image = pygame.transform.scale(self.image, (64, 64))
        
        self.rect = self.image.get_rect()
        self.rect.y = self.altura - 64
        self.rect.x = posic_X * 64
    
    def update(self):
        #se a posição X do topo da direita 
        if self.rect.topright[0] < 0:
            self.rect.x = self.largura
        self.rect.x -= 10 
