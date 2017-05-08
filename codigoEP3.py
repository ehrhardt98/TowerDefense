import pygame
from pygame.locals import *
from sys import exit



preto = (0, 0, 0)
marrom = (153, 76, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)



grama = 0
caminho = 1
agua = 2
castelo = 3


cores = {
grama : verde,
caminho : marrom,
agua : azul,
castelo : preto
}


tilemap = [
[3, 0, 0, 2, 0, 0],
[3, 0, 0, 2, 0, 0],
[3, 1, 0, 2, 0, 0],
[3, 0, 1, 2, 0, 0],
[3, 0, 0, 1, 0, 0],
[3, 0, 0, 2, 1, 0],
[3, 0, 0, 2, 0, 1],
[3, 0, 0, 2, 0, 0]
]

altura = 8
largura = 6
TILESIZE = 40

pygame.init()

DISPLAYSURF = pygame.display.set_mode((largura*TILESIZE, altura*TILESIZE))

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()

	for fileira in range(altura):
		for coluna in range(largura):
			pygame.draw.rect(DISPLAYSURF, cores[tilemap[fileira][coluna]], (coluna*TILESIZE, fileira*TILESIZE, TILESIZE, TILESIZE))

	pygame.display.update()


 