import pygame

pygame.init()
pygame.display.set_caption("Meu Jogo Pygame")


largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))

x = largura /2
y = altura /2
z = 0

relogio = pygame.time.Clock()

#todo jogo deve rodar num loop
running = True
while running:
    relogio.tick(30) #quantidade de frames por segundo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_a:
                x = x - 20
            if event.key == K_d:
                x = x + 20
            if event.key == K_w:
                y = y - 20
            if event.key == K_s:
                y = y + 20



    tela.fill((255, 255, 255)) #preenche a cor de fundo

    pygame.draw.rect(tela, (255,0,0), (x,y,50,60)) #os parametros são organizados da seguinte maneira: onde vai ficar, qual cor vai ter, depois em qual posição ele começa (X e Y) e por fim seu tamanho
    if z >= altura:
        z = 0
    z = z + 1 
    pygame.draw.rect(tela, (0,255,0), (x,z,40,50))
    pygame.draw.circle(tela, (0,0,120), (300,260), 40)


    pygame.display.flip()

pygame.quit()