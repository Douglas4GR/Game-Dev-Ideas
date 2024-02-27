import pygame
from pygame.locals import *
from sys import exit
pygame.init()

#TELA DO JOGO
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Sapo")