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
        self.sprites_parado = []
        self.sprites_parado.append(pygame.image.load('pygame/jogo_do_bonequinho_roxo/andando/roxo_andando_direita_0.png'))
        self.sprites_parado.append(pygame.image.load('pygame/jogo_do_bonequinho_roxo/andando/roxo_andando_direita_1.png'))
        self.sprites_andando = []
        self.sprites_andando.append(pygame.image.load('pygame/jogo_do_bonequinho_roxo/andando/roxo_andando_direita_1.png'))
        self.sprites_andando.append(pygame.image.load('pygame/jogo_do_bonequinho_roxo/andando/roxo_andando_direita_2.png'))
        self.sprites_andando.append(pygame.image.load('pygame/jogo_do_bonequinho_roxo/andando/roxo_andando_direita_3.png'))
        self.sprites_andando.append(pygame.image.load('pygame/jogo_do_bonequinho_roxo/andando/roxo_andando_direita_4.png'))
        self.atual = 0
        self.image = self.sprites_parado[self.atual] #imagem inicial
        self.image = pygame.transform.scale(self.image, (64*3, 64*3)) #tamanho da imagem
        
        self.rect = self.image.get_rect() #pega o retângulo da imagem
        self.rect.topleft = 50, 50

        self.barulho_andando = pygame.mixer.Sound('pygame/primeiro_pj_sprites/sapos/barulho.wav')
        

    def andar_dir(self):
        self.animacao_direita = True
        self.barulho_andando.play()

    def update(self): #método que atualiza a imagem
        self.atual += 0.05 #velocidade da animação (indice da lista de sprites)
        if self.atual >= len(self.sprites_parado):
            self.atual = 0
        self.image = self.sprites_parado[int(self.atual)] #atualiza a imagem
        self.image = pygame.transform.scale(self.image, (64*3, 64*3)) #o tamanho da imagem deve ser mantido no loop

#Objeto que irá armazenar todas as sprites do jogo (roxo, mosca, etc)
todos_sprites = pygame.sprite.Group()

#instanciando o roxo a partir da classe Roxo
roxo = Roxo()
todos_sprites.add(roxo)
imagem_fundo = pygame.image.load('pygame/jogo_do_bonequinho_roxo/andando/campo.jpg').convert()
imagem_fundo = pygame.transform.scale(imagem_fundo, (largura, altura))

while True:
    relogio.tick(30)
    tela.fill(preto)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit() #fecha o jogo
            exit() #fecha o console
        
        if event.type == KEYDOWN:
            if event.key == K_d:
                roxo.andar_dir()
    tela.blit(imagem_fundo, (0, 0))
    todos_sprites.draw(tela)
    todos_sprites.update()
    pygame.display.flip() #o flip é melhor que o update