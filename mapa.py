import pygame,sys
from pygame.locals import *

BLACK = (0, 0, 0)
BROWN = (153, 76, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (100, 100, 100)
RED = (255, 0, 0)

DIRT = 0
GRASS = 1
WATER = 2
COAL = 3
ROCK = 4
LAVA = 5

colours = {
	DIRT:BROWN,
	GRASS:GREEN,
	WATER:BLUE,
	COAL:BLACK,
	ROCK:GREY,
	LAVA:RED
}

tilemap = [
[GRASS, ROCK, DIRT, LAVA, GRASS],
[WATER, WATER, GRASS, LAVA, DIRT],
[ROCK, GRASS, WATER, COAL, WATER],
[DIRT, LAVA, COAL, DIRT, GRASS],
[GRASS, WATER, LAVA, ROCK, ROCK]
]

TILESIZE = 50
MAPWIDTH = 5
MAPHEIGHT = 5

pygame.init()
DISPLYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))

while True:

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	for row in range(MAPHEIGHT):

		for column in range(MAPWIDTH):
			pygame.draw.rect(DISPLYSURF, colours[tilemap[row][column]], (column*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))

	pygame.display.update()