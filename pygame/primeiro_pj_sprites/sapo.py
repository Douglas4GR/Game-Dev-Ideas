import pygame
from pygame.locals import *
from sys import exit
pygame.init()

#TELA DO JOGO
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Sapo")

#CORES DO JOGO
branco = (255, 255, 255)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
amarelo = (255, 255, 0)
azul = (0, 0, 255)
preto = (0, 0, 0)

class Sapo(pygame.sprite.Sprite): #nome da classe tem que começar com letra maiúscula
    def __init__(self): #método construtor
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('pygame/primeiro_pj_sprites/sapos/attack_1.png'))
        self.sprites.append(pygame.image.load('pygame/primeiro_pj_sprites/sapos/attack_2.png'))
        self.sprites.append(pygame.image.load('pygame/primeiro_pj_sprites/sapos/attack_3.png'))
        self.sprites.append(pygame.image.load('pygame/primeiro_pj_sprites/sapos/attack_4.png'))
        self.sprites.append(pygame.image.load('pygame/primeiro_pj_sprites/sapos/attack_5.png'))
        self.sprites.append(pygame.image.load('pygame/primeiro_pj_sprites/sapos/attack_6.png'))
        self.sprites.append(pygame.image.load('pygame/primeiro_pj_sprites/sapos/attack_7.png'))
        self.sprites.append(pygame.image.load('pygame/primeiro_pj_sprites/sapos/attack_8.png'))
        self.sprites.append(pygame.image.load('pygame/primeiro_pj_sprites/sapos/attack_9.png'))
        self.sprites.append(pygame.image.load('pygame/primeiro_pj_sprites/sapos/attack_10.png'))
        self.atual = 0
        self.image = self.sprites[self.atual] #imagem inicial
        self.image = pygame.transform.scale(self.image, (128*3, 64*3)) #tamanho da imagem
        
        self.rect = self.image.get_rect() #pega o retângulo da imagem
        self.rect.topleft = 50, 50

    def update(self): #método que atualiza a imagem
        self.atual += 0.05
        '''quanto maior o número acima, mais rápido a animação,
        detalhe: esse número vai equivaler ao índice, logo se for menor que 1,
        vai dar erro, pois não existe índice 0.5, por exemplo. '''
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        ''' ^^^ atualiza a imagem ^^^
        (para evitar o erro relatado anteriormente, é só converter o número para inteiro)'''
        self.image = pygame.transform.scale(self.image, (128*3, 64*3)) #o tamanho da imagem deve ser mantido no loop

#Objeto que irá armazenar todas as sprites do jogo (sapo, mosca, etc)
todos_sprites = pygame.sprite.Group()

#instanciando o sapo a partir da classe Sapo
sapo = Sapo()
todos_sprites.add(sapo)


while True:
    tela.fill(preto)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit() #fecha o jogo
            exit() #fecha o console

    todos_sprites.draw(tela)
    todos_sprites.update()
    pygame.display.flip() #o flip é melhor que o update