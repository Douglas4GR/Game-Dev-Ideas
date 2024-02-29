import pygame
from pygame.locals import *
from sys import exit
pygame.init()

#TELA DO JOGO
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()
pygame.display.set_caption("Roxo")

#CORES DO JOGO
branco = (255, 255, 255)
preto = (0, 0, 0)

class Roxo(pygame.sprite.Sprite): #nome da classe tem que começar com letra maiúscula
    def __init__(self): #método construtor
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('pygame/jogo_do_bonequinho_roxo/andando/roxo_andando_direita_2.png'))
        self.sprites.append(pygame.image.load('pygame/jogo_do_bonequinho_roxo/andando/roxo_andando_direita_3.png'))
        self.sprites.append(pygame.image.load('pygame/jogo_do_bonequinho_roxo/andando/roxo_andando_direita_4.png'))
        self.atual = 0
        self.image = self.sprites[self.atual] #imagem inicial
        self.image = pygame.transform.scale(self.image, (64*3, 64*3)) #tamanho da imagem
        
        self.rect = self.image.get_rect() #pega o retângulo da imagem
        self.rect.topleft = 50, 50

        self.animacao_ataque = False
        self.barulho_ataque = pygame.mixer.Sound('pygame/primeiro_pj_sprites/sapos/barulho.wav')

    def atacar(self):
        self.animacao_ataque = True
        self.barulho_ataque.play()

    def update(self): #método que atualiza a imagem
        if self.animacao_ataque == True:
            self.atual += 1 #velocidade da animação (indice da lista de sprites)
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animacao_ataque = False
            self.image = self.sprites[int(self.atual)] #atualiza a imagem
            self.image = pygame.transform.scale(self.image, (128*3, 64*3)) #o tamanho da imagem deve ser mantido no loop

#Objeto que irá armazenar todas as sprites do jogo (roxo, mosca, etc)
todos_sprites = pygame.sprite.Group()

#instanciando o roxo a partir da classe Roxo
roxo = Roxo()
todos_sprites.add(roxo)


while True:
    relogio.tick(30)
    tela.fill(preto)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit() #fecha o jogo
            exit() #fecha o console
        
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                roxo.atacar()

    todos_sprites.draw(tela)
    todos_sprites.update()
    pygame.display.flip() #o flip é melhor que o update