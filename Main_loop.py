import pygame
import time
from Funcoes import *
from Classes import *
from Mapa import *


pygame.init()

display_width = 800
display_height = 600



gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Tower Defense")
clock = pygame.time.Clock()

fechar = False
state = 0

mouse = pygame.mouse.get_pos()
click = pygame.mouse.get_pressed()



while not fechar:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			fechar = True

	if state == 0:
		state = game_intro(gameDisplay)

	if state == 1:
		state = game_loop(invasoress)


	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()