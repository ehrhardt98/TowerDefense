import pygame,sys
from pygame.locals import *

def mapa():

	DIRT = 0
	GRASS = 1
	WATER = 2
	COAL = 3
	ROCK = 4
	LAVA = 5
	TOWER = 6

	terrenos = [DIRT, GRASS, WATER, COAL, ROCK, LAVA, TOWER]

	textures ={
		DIRT: pygame.image.load('DIRT.png'),
		GRASS: pygame.image.load('GRASS.png'),
		WATER: pygame.image.load('WATER.png'),
		COAL: pygame.image.load('COAL.png'),
		ROCK: pygame.image.load('ROCK.png'),
		LAVA: pygame.image.load('LAVA.png'),
		TOWER: pygame.image.load('TOWER.png')

	}

	TILESIZE = 41
	MAPWIDTH = 10
	MAPHEIGHT = 10

	tilemap = [
	[WATER, WATER, GRASS, WATER, GRASS, GRASS, WATER, GRASS, GRASS, GRASS],
	[GRASS, WATER, GRASS, WATER, GRASS, GRASS, WATER, GRASS, GRASS, GRASS],
	[GRASS, WATER, GRASS, WATER, GRASS, WATER, WATER, GRASS, GRASS, GRASS],
	[GRASS, WATER, WATER, WATER, GRASS, WATER, GRASS, GRASS, GRASS, GRASS],
	[GRASS, GRASS, GRASS, GRASS, GRASS, WATER, GRASS, GRASS, GRASS, GRASS],
	[ TOWER , DIRT , DIRT , DIRT , DIRT , ROCK , DIRT , DIRT , DIRT , TOWER],
	[GRASS, GRASS, GRASS, GRASS, GRASS, WATER, GRASS, GRASS, GRASS, GRASS],
	[GRASS, GRASS, GRASS, GRASS, GRASS, WATER, WATER, WATER, GRASS, GRASS],
	[GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, WATER, WATER, GRASS],
	[GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, WATER, GRASS],
	[GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, WATER, GRASS]
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

 