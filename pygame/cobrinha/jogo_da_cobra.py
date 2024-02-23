import pygame
from pygame.locals import *
from random import randint
pygame.init()

#SONS DO JOGO
pygame.mixer.music.set_volume(0.5)
musica_fundo = pygame.mixer.music.load('pygame/projeto_com_sons/elevator-music.mp3')
pygame.mixer.music.play(-1)
som_colisao = pygame.mixer.Sound('pygame/projeto_com_sons/colisao.wav')

#TELA DO JOGO
largura, altura = 800, 600 #tamanho da tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Meu Jogo Pygame")
relogio = pygame.time.Clock()

#TEXTOS DO JOGO
pontuacao = 0
fonte = pygame.font.SysFont('arial', 48, True, False)

#CORES DO JOGO
branco = (255, 255, 255)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
preto = (0, 0, 0)

#posição inicial da cobra
x_cobra = int(largura /2)
y_cobra = int(altura /2)
velocidade = 20 #velocidade da cobra
lista_cobra = [] #lista que vai armazenar a posição da cobra


#posição inicial da maçã
x_vermelho = randint(40, 760)
y_vermelho = randint(40, 560)



#função que aumenta a cobra
def aumenta_cobra(lista_cobra, cobraXY):
    for XY in lista_cobra:
        #XY = [x, y]
        #XY[0] = x
        #XY[1] = y
        pygame.draw.rect(tela, verde, (XY[0], XY[1], 20, 20))



#todo jogo deve rodar num loop
running = True 
while running:
    relogio.tick(30) #quantidade de frames por segundo
    mensagem = f'Pontuação: {pontuacao}'
    texto_formatado = fonte.render(mensagem, True, branco) #false é para suavizar as bordas

    for event in pygame.event.get(): #pega todos os eventos que aconteceram desde a última vez que o comando foi chamado
        if event.type == pygame.QUIT:
            running = False

        if pygame.key.get_pressed()[K_a]: #move para a esquerda
            x_cobra -= velocidade
        if pygame.key.get_pressed()[K_d]: #move para a direita
            x_cobra += velocidade
        if pygame.key.get_pressed()[K_w]: #move para cima
            y_cobra -= velocidade
        if pygame.key.get_pressed()[K_s]: #move para baixo
            y_cobra += velocidade
        
        
        tela.fill(preto) #preenche a cor de fundo


        cobra = pygame.draw.rect(tela, verde, (x_cobra,y_cobra,20,20)) #os parametros são organizados da seguinte maneira: onde vai ficar, qual cor vai ter, depois em qual posição ele começa (X e Y) e por fim seu tamanho
        maca = pygame.draw.rect(tela, vermelho, (x_vermelho,y_vermelho,30,30))


        if cobra.colliderect(maca): #se a cobra colidir com a maçã
            x_vermelho = randint(40, 760)
            y_vermelho = randint(40, 560)
            pontuacao += 1
            som_colisao.play()

        lista_cabeca = [] #lista que vai armazenar a posição da cabeça da cobra
        lista_cabeca.append(x_cobra) 
        lista_cabeca.append(y_cobra)
        lista_cobra.append(lista_cabeca) #adiciona a cabeça da cobra na lista da cobra
        aumenta_cobra(lista_cobra, cobra)
        if len(lista_cobra) > pontuacao:
            del lista_cobra[0]

        tela.blit(texto_formatado, (10,10))
        pygame.display.update()
    pygame.display.flip()
pygame.quit()