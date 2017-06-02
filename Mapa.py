import pygame,sys
from pygame.locals import *
import sys, os

pygame.init()


black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 200, 0)
bright_green = (0, 250, 0)



def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()

def mapa():

	CANTOESQUERDO = 0
	LADOESQ = 1
	GRASS = 2
	AGUA = 3
	LADODIR = 4
	CIMAGRAMA = 5
	BAIXOGRAMA = 6
	CANTODIREITO = 7
	CAMINHO = 8
	tilecastelo = 9
	bordatorre = 10
	cantotorre = 11
	bordabaixo = 12
	pedra = 13
	arvore = 14
	casa = 16
	sangue = 17
	carro = 18


	terrenos = [CANTOESQUERDO, LADOESQ, GRASS,AGUA, LADODIR, CIMAGRAMA, BAIXOGRAMA,CANTODIREITO, CAMINHO, tilecastelo, bordatorre, cantotorre, bordabaixo, pedra, arvore, casa, sangue, carro]
 
	textures = {
		CANTOESQUERDO: pygame.image.load('CANTOESQUERDO.png'),
		LADOESQ: pygame.image.load('LADOESQ.png'),
		GRASS: pygame.image.load('GRASS.png'),
		AGUA: pygame.image.load('AGUA.png'),
		LADODIR: pygame.image.load('LADODIR.png'),
		CIMAGRAMA: pygame.image.load('CIMAGRAMA.png'),
		BAIXOGRAMA: pygame.image.load('BAIXOGRAMA.png'),
		CANTODIREITO: pygame.image.load('CANTODIREITO.png'),
		CAMINHO: pygame.image.load('CAMINHO.png'),
		tilecastelo: pygame.image.load('tilecastelo.png'),
		bordatorre: pygame.image.load('bordatorre.png'),
		cantotorre: pygame.image.load('cantotorre.png'),
		bordabaixo: pygame.image.load('bordabaixo.png'),
		pedra: pygame.image.load('pedra.png'),
		arvore: pygame.image.load('arvore.png'),
		casa: pygame.image.load('casa.png'),
		sangue: pygame.image.load('sangue.png'),
		carro: pygame.image.load('carro.png'),
	}

	TILESIZE = 40
	MAPWIDTH = 30
	MAPHEIGHT = 15

	tilemap = [
	[tilecastelo, tilecastelo, tilecastelo, bordatorre, GRASS,pedra, pedra, pedra, arvore, arvore, arvore,arvore, sangue,GRASS,arvore, arvore, arvore, GRASS, GRASS, GRASS,GRASS, GRASS, GRASS, GRASS, GRASS,GRASS, GRASS, GRASS, GRASS, GRASS],
	[tilecastelo, tilecastelo, tilecastelo, bordatorre, GRASS,GRASS, pedra, pedra,arvore, sangue,GRASS,GRASS, GRASS, pedra,GRASS, arvore, arvore, arvore, pedra, GRASS,GRASS, carro, GRASS, GRASS, GRASS,GRASS, GRASS, GRASS, GRASS, GRASS],
	[tilecastelo, tilecastelo, tilecastelo, bordatorre, GRASS,pedra, GRASS, GRASS,pedra, pedra,GRASS,GRASS, GRASS, GRASS,GRASS, arvore, arvore, GRASS, GRASS, GRASS,GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, sangue],
	[tilecastelo, tilecastelo, tilecastelo, bordatorre, GRASS,GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS,GRASS, GRASS, GRASS, GRASS, GRASS,GRASS, GRASS, GRASS, GRASS, GRASS],
	[tilecastelo, tilecastelo, tilecastelo,bordatorre, CAMINHO,CAMINHO, CAMINHO, CAMINHO, CAMINHO, CAMINHO, CAMINHO,CAMINHO, CAMINHO, CAMINHO, CAMINHO,CAMINHO, CAMINHO,CAMINHO, CAMINHO, CAMINHO, CAMINHO, CAMINHO, CAMINHO,CAMINHO, CAMINHO, CAMINHO, CAMINHO, CAMINHO, CAMINHO,CAMINHO],
	[tilecastelo, tilecastelo, tilecastelo, bordatorre, GRASS,GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS,GRASS, GRASS, GRASS, GRASS, GRASS,GRASS, GRASS, GRASS, GRASS, GRASS],
	[tilecastelo, tilecastelo, tilecastelo, bordatorre, GRASS,GRASS, GRASS, GRASS, GRASS, GRASS,GRASS, arvore, arvore, GRASS, GRASS, GRASS, arvore, arvore, arvore, GRASS,GRASS, GRASS, GRASS, GRASS, GRASS,GRASS, GRASS, GRASS, sangue, sangue],
	[tilecastelo, tilecastelo, tilecastelo, bordatorre, GRASS,GRASS, GRASS, GRASS, GRASS, GRASS,GRASS, pedra, pedra, arvore, pedra, pedra, arvore, arvore, arvore, GRASS,GRASS, GRASS, GRASS, GRASS, GRASS,GRASS, GRASS, GRASS, GRASS, GRASS],
	[tilecastelo, tilecastelo, tilecastelo, bordatorre, GRASS,GRASS, GRASS, AGUA, AGUA, AGUA, AGUA, AGUA, AGUA, AGUA, arvore, arvore, sangue, pedra, arvore, arvore,GRASS, pedra, pedra, pedra, arvore,arvore, GRASS, GRASS, arvore, arvore],
	[tilecastelo, tilecastelo, tilecastelo, bordatorre, sangue,GRASS, GRASS, AGUA, AGUA, AGUA,AGUA, AGUA, AGUA, AGUA, GRASS, arvore, arvore, arvore, arvore, GRASS,GRASS, pedra, pedra, pedra, arvore,sangue, GRASS, arvore, arvore, arvore],
	[tilecastelo, tilecastelo, tilecastelo, bordatorre, GRASS,GRASS, GRASS,AGUA, AGUA, GRASS,GRASS, GRASS, AGUA, AGUA, GRASS, GRASS, sangue, GRASS, GRASS, GRASS,GRASS, pedra, pedra, pedra, arvore,arvore, GRASS, arvore, arvore, GRASS],
	[tilecastelo, tilecastelo, tilecastelo, bordatorre, GRASS,GRASS, GRASS, AGUA, AGUA, GRASS,GRASS, GRASS,AGUA, AGUA, AGUA, AGUA, GRASS, casa, GRASS, sangue,GRASS, GRASS, GRASS, pedra, pedra, pedra, arvore, arvore, arvore, arvore],
	[tilecastelo, tilecastelo, tilecastelo, bordatorre, GRASS,GRASS, GRASS, AGUA, AGUA, GRASS,GRASS, GRASS, AGUA, AGUA, AGUA, AGUA, GRASS, casa, GRASS, casa,GRASS, GRASS,GRASS,pedra, pedra, pedra, pedra, pedra,  pedra, arvore],
	[bordabaixo, bordabaixo, bordabaixo, cantotorre, GRASS,GRASS, GRASS, AGUA, AGUA, GRASS,GRASS, GRASS, GRASS, GRASS, AGUA, AGUA, GRASS, GRASS, GRASS, casa,GRASS, GRASS,GRASS, pedra, pedra,pedra, pedra, arvore, arvore, arvore],
	[GRASS, GRASS,GRASS, GRASS, GRASS,GRASS, GRASS, AGUA, AGUA,GRASS,GRASS, GRASS, GRASS, GRASS, AGUA, AGUA, GRASS, GRASS, GRASS, GRASS,GRASS, sangue, GRASS, GRASS, GRASS,GRASS, pedra, pedra, arvore, arvore],

	]

	DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))
	pygame.display.set_caption('Tower Defense')


	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	for row in range(MAPHEIGHT):

		for column in range(MAPWIDTH):
			DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE,row*TILESIZE))
	return DISPLAYSURF
mapa()