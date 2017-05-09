import pygame
import time

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 200, 0)
bright_green = (0, 250, 0)


clock = pygame.time.Clock()

def button(gameDisplay, msg, x, y, w, h, ic, ac, action=None):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	
	if x + w > mouse[0] > x and y + h > mouse[1] > y:
		pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
		if click[0] == 1 and action != None:
			if action == "Defend your Castle!":
				game_loop()
	else:
		pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

	button_text = pygame.font.Font("freesansbold.ttf", 40)
	TextSurf, TextRect = text_objects(msg, button_text)
	TextRect.center = ((x + w/2)), ((y + h/2))
	gameDisplay.blit(TextSurf, TextRect)



def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()



def game_intro(gameDisplay):

	intro = True

	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		gameDisplay.fill(white)

		button(gameDisplay, "Defend your Castle!", 200, 270, 400, 50, green, bright_green, "Defend your Castle!")

		pygame.display.update()
		clock.tick(60)

