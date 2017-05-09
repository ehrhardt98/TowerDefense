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

	terrenos = [DIRT, GRASS, WATER, COAL, ROCK, LAVA]

	textures = {
		DIRT: pygame.image.load('DIRT.png'),
		GRASS: pygame.image.load('GRASS.png'),
		WATER: pygame.image.load('WATER.png'),
		COAL: pygame.image.load('COAL.png'),
		ROCK: pygame.image.load('ROCK.png'),
		LAVA: pygame.image.load('LAVA.png'),
		TOWER: pygame.image.load('TOWER.png')

	}

	TILESIZE = 40
	MAPWIDTH = 10
	MAPHEIGHT = 10

	tilemap = [
	[LAVA, LAVA, GRASS, LAVA, GRASS, GRASS, LAVA, GRASS, GRASS, GRASS],
	[GRASS, LAVA, GRASS, LAVA, GRASS, GRASS, LAVA, GRASS, GRASS, GRASS],
	[GRASS, LAVA, GRASS, LAVA, GRASS, LAVA, LAVA, GRASS, GRASS, GRASS],
	[GRASS, LAVA, LAVA, LAVA, GRASS, LAVA, GRASS, GRASS, GRASS, GRASS],
	[GRASS, GRASS, GRASS, GRASS, GRASS, LAVA, GRASS, GRASS, GRASS, GRASS],
	[ TOWER , DIRT , DIRT , DIRT , DIRT , ROCK , DIRT , DIRT , DIRT , TOWER],
	[GRASS, GRASS, GRASS, GRASS, GRASS, LAVA, GRASS, GRASS, GRASS, GRASS],
	[GRASS, GRASS, GRASS, GRASS, GRASS, LAVA, LAVA, LAVA, GRASS, GRASS],
	[GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, LAVA, LAVA, GRASS],
	[GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, LAVA, GRASS],
	[GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, LAVA, GRASS]
	]

	DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))
	pygame.display.set_caption('Tower Defense')

	while True:

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

		for row in range(MAPHEIGHT):

			for column in range(MAPWIDTH):
				DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE,row*TILESIZE))

		pygame.display.update()
mapa()
#DISPLAYSURF.blit(self.textures[tilemap[row][column]], (column*TILESIZE,row*TILESIZE))
#pygame.display.set_caption('Tower Defense')