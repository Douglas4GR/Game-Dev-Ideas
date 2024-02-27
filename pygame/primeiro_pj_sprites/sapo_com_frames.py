import pygame
from pygame.locals import *
from sys import exit
pygame.init()

#TELA DO JOGO
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()
pygame.display.set_caption("Sapo")

#CORES DO JOGO
branco = (255, 255, 255)
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

        self.animacao_ataque = False

    def atacar(self):
        self.animacao_ataque = True

    def update(self): #método que atualiza a imagem
        if self.animacao_ataque == True:
            self.atual += 1 #velocidade da animação (indice da lista de sprites)
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animacao_ataque = False
            self.image = self.sprites[int(self.atual)] #atualiza a imagem
            self.image = pygame.transform.scale(self.image, (128*3, 64*3)) #o tamanho da imagem deve ser mantido no loop

#Objeto que irá armazenar todas as sprites do jogo (sapo, mosca, etc)
todos_sprites = pygame.sprite.Group()

#instanciando o sapo a partir da classe Sapo
sapo = Sapo()
todos_sprites.add(sapo)


while True:
    relogio.tick(30)
    tela.fill(preto)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit() #fecha o jogo
            exit() #fecha o console
        
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                sapo.atacar()

    todos_sprites.draw(tela)
    todos_sprites.update()
    pygame.display.flip() #o flip é melhor que o update