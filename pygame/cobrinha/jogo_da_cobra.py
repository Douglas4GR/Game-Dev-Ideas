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
largura, altura = 800, 800 #tamanho da tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Meu Jogo Pygame")
relogio = pygame.time.Clock()
x_meio = int(largura / 2)
y_meio = int(altura / 2)


#CORES DO JOGO
branco = (255, 255, 255)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
verde_escuro = (0, 100, 0)
amarelo = (255, 255, 0)
azul = (0, 0, 255)
preto = (0, 0, 0)


#TEXTOS DO JOGO
pontuacao = 0
fonte = pygame.font.SysFont('arial', 48, True, False)


#MOVIMENTAÇÃO DA COBRA
velocidade = 50 #velocidade da cobra
x_direcao = velocidade
y_direcao = 0


#OUTROS DETALHES DA COBRA
lista_cobra = [] #lista que vai armazenar a posição da cobra
comprimento_inicial = 10   #comprimento inicial da cobra
morreu = False


#posição inicial da cobra
x_cobra = int(largura /2)
y_cobra = int(altura /2)
#posição inicial da maçã
x_vermelho = randint(40, 760)
y_vermelho = randint(40, 560)



#função que aumenta a cobra
def aumenta_cobra(lista_cobra, cobra):
    for XY in lista_cobra:
        #XY = [x, y]
        #XY[0] = x
        #XY[1] = y
        # o tamanho abaixo é a área visual da cobra
        pygame.draw.rect(tela, verde, (XY[0], XY[1], 100, 100))


#função que detecta se cobra colidiu com a parede
def colisao_parede(x_cobra, y_cobra):
    if x_cobra < 0 or x_cobra > largura - 100:
        return True
    if y_cobra < 0 or y_cobra > altura - 100:
        return True
    return False


#INICIO DO JOGO
def jogo():
    global morreu, pontuacao, x_cobra, y_cobra, x_vermelho, y_vermelho, lista_cobra, comprimento_inicial
    lista_cobra = [] 
    comprimento_inicial = 5
    morreu = False
    x_cobra = x_meio
    y_cobra = y_meio
    x_vermelho = randint(40, 760)
    y_vermelho = randint(40, 560)

#todo jogo deve rodar num loop
running = True
while running:
    relogio.tick(10) #quantidade de frames por segundo
    tela.fill(preto) #preenche a cor de fundo
    mensagem = f'Pontuação: {pontuacao}'
    texto_formatado = fonte.render(mensagem, True, branco) #false é para suavizar as bordas

    for event in pygame.event.get(): #pega todos os eventos que aconteceram desde a última vez que o comando foi chamado
        if event.type == pygame.QUIT:
            running = False


        #movimentação da cobra
        if event.type == pygame.KEYDOWN:
            if event.key == K_a:
                if x_direcao == velocidade:
                    pass
                else:
                    x_direcao = -velocidade
                    y_direcao = 0
            if event.key == K_d:
                if x_direcao == -velocidade:
                    pass
                else:
                    x_direcao = velocidade
                    y_direcao = 0
            if event.key == K_w:
                if y_direcao == velocidade:
                    pass
                else:
                    x_direcao = 0
                    y_direcao = -velocidade
            if event.key == K_s:
                if y_direcao == -velocidade:
                    pass
                else:
                    x_direcao = 0
                    y_direcao = velocidade

    x_cobra += x_direcao
    y_cobra += y_direcao

    #o tamanho abaixo é a área fisica da cobra, o espaço que realmente ocupa
    cobra = pygame.draw.rect(tela, verde, (x_cobra,y_cobra,100,100)) #os parametros são organizados da seguinte maneira: onde vai ficar, qual cor vai ter, depois em qual posição ele começa (X e Y) e por fim seu tamanho
    maca = pygame.draw.rect(tela, vermelho, (x_vermelho,y_vermelho,110,110))


    if cobra.colliderect(maca): #se a cobra colidir com a maçã
        x_vermelho = randint(40, 760)
        y_vermelho = randint(40, 560)
        pontuacao += 1
        som_colisao.play()

    lista_cabeca = [] #lista que vai armazenar a posição da cabeça da cobra
    lista_cabeca.append(x_cobra) 
    lista_cabeca.append(y_cobra)

    lista_cobra.append(lista_cabeca) #adiciona a cabeça da cobra na lista da cobra

    if lista_cobra.count(lista_cabeca) > 1 or colisao_parede(x_cobra,y_cobra) == True: #se a cobra colidir com ela mesma ou com a parede
        # Mensagem de morte
        mensagem_pontuacao = f'Pontuação: {pontuacao}'
        mensagem_aperte_espaco = 'Aperte espaço para jogar novamente'

        # Renderizando as mensagens
        texto_pontuacao = fonte.render(mensagem_pontuacao, True, branco)
        texto_aperte_espaco = fonte.render(mensagem_aperte_espaco, True, branco)
        retang_pontuacao = texto_pontuacao.get_rect()
        retang_aperte_espaco = texto_aperte_espaco.get_rect()

        som_colisao.play()
        morreu = True
        tela.fill(verde_escuro)
        while morreu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    morreu = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_SPACE:
                        jogo()
            # Exibindo as mensagens na tela
            retang_pontuacao.center = (x_meio, y_meio - 60)
            retang_aperte_espaco.center = (x_meio, y_meio)
            tela.blit(texto_pontuacao, retang_pontuacao) 
            tela.blit(texto_aperte_espaco, retang_aperte_espaco)
            pygame.display.update()

    '''
    condições para a cobra atravessar a parede
    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra > altura:
        y_cobra = 0
    if y_cobra < 0:
        y_cobra = altura
    '''
    
    if len(lista_cobra) > pontuacao + comprimento_inicial:
        del lista_cobra[0]
    aumenta_cobra(lista_cobra, cobra)

    tela.blit(texto_formatado, (10,10)) #posição do texto na tela
    pygame.display.update() #atualiza a tela
pygame.quit()