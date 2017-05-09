import pygame,sys
from pygame.locals import *

def Mapa():

	DIRT = 0
	GRASS = 1
	WATER = 2
	COAL = 3
	ROCK = 4
	LAVA = 5

	self.terrenos = [DIRT, GRASS, WATER, COAL, ROCK, LAVA]

	self.textures = {
		DIRT: pygame.image.load('DIRT.png'),
		GRASS: pygame.image.load('GRASS.png'),
		WATER: pygame.image.load('WATER.png'),
		COAL: pygame.image.load('COAL.png'),
		ROCK: pygame.image.load('ROCK.png'),
		LAVA: pygame.image.load('LAVA.png')
	}


	TILESIZE = 32
	MAPWIDTH = 20
	MAPHEIGHT = 13

	tilemap = [
	[WATER, WATER, GRASS, WATER, GRASS, GRASS, WATER, GRASS, GRASS, GRASS],
	[GRASS, WATER, GRASS, WATER, GRASS, GRASS, WATER, GRASS, GRASS, GRASS],
	[GRASS, WATER, GRASS, WATER, GRASS, WATER, WATER, GRASS, GRASS, GRASS],
	[GRASS, WATER, WATER, WATER, GRASS, WATER, GRASS, GRASS, GRASS, GRASS],
	[GRASS, GRASS, GRASS, GRASS, GRASS, WATER, GRASS, GRASS, GRASS, GRASS],
	[ COAL , DIRT , DIRT , DIRT , DIRT , ROCK , DIRT , DIRT , DIRT , COAL],
	[GRASS, GRASS, GRASS, GRASS, GRASS, WATER, GRASS, GRASS, GRASS, GRASS],
	[GRASS, GRASS, GRASS, GRASS, GRASS, WATER, WATER, WATER, GRASS, GRASS],
	[GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, WATER, WATER, GRASS],
	[GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, WATER, GRASS],
	[GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, WATER, GRASS]
	]

	#DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))
	#DISPLAYSURF.blit(self.textures[tilemap[row][column]], (column*TILESIZE,row*TILESIZE))
	#pygame.display.set_caption('Tower Defense')