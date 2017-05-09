import pygame
import time
from Funções import *
from Classes import *


pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Tower Defense")
clock = pygame.time.Clock()

fechar = False

mouse = pygame.mouse.get_pos()
click = pygame.mouse.get_pressed()

while not fechar:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			fechar = True

	game_intro(gameDisplay)

	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()