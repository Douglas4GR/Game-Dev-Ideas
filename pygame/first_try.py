import pygame

pygame.init()


largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))

pygame.display.set_caption("Meu Jogo Pygame")

#todo jogo deve rodar num loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    tela.fill((255, 255, 255)) #preenche a cor de fundo

    pygame.draw.rect(tela, (255,0,0), (200,300,40,50)) #os parametros são organizados da seguinte maneira: onde vai ficar, qual cor vai ter, depois em qual posição ele começa (X e Y) e por fim seu tamanho
    pygame.draw.rect(tela, (0,255,0), (210,310,40,50))
    pygame.draw.circle(tela, (0,0,120), (300,260), 40)


    pygame.display.flip()

pygame.quit()