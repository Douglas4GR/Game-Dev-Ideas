import pygame

pygame.init()
pygame.display.set_caption("Meu Jogo Pygame")


largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))

x = largura /2
y = 0

relogio = pygame.time.Clock()

#todo jogo deve rodar num loop
running = True
while running:
    relogio.tick(30) #quantidade de frames por segundo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    tela.fill((255, 255, 255)) #preenche a cor de fundo

    pygame.draw.rect(tela, (255,0,0), (x,y,50,60)) #os parametros são organizados da seguinte maneira: onde vai ficar, qual cor vai ter, depois em qual posição ele começa (X e Y) e por fim seu tamanho
    if y >= altura:
        y = 0
    y = y + 1 
    pygame.draw.rect(tela, (0,255,0), (y,x,40,50))
    pygame.draw.circle(tela, (0,0,120), (300,260), 40)


    pygame.display.flip()

pygame.quit()