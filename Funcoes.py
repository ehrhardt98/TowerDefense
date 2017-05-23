import pygame
import time
from Mapa import *
from Classes import *

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 200, 0)
bright_green = (0, 250, 0)

chaves = Invasores(10, 1600, 245, -20, 10, "sprite_1.png", "sprite_2.png", "sprite_3.png", 2)
castelo = Castelo(10, 210, 10, "TORREE.png")
torre = Torres(1, 10, 1, 5, "TORREE.png", "agua")
jogador = Jogador(10, 25)
lista_torres = []

clock = pygame.time.Clock()

def pixel_matriz(pixelx, pixely):
	poisçãox = pixelx//40 + 1
	posiçãoy = pixely//40 + 1
	return [posiçãox, posiçãoy]


def movimentar(invasores, displaySurface):
	mapa()
	jogador.mostradinheiro(displaySurface)
	for i in lista_torres:
		displaySurface.blit(i.imagem, (i.posicaox, i.posicaoy))
	displaySurface.blit(invasores.sprite1,(invasores.posicaox, invasores.posicaoy))
	invasores.posicaox = invasores.posicaox + invasores.vx
	time.sleep(0.1)
	pygame.display.update()

	mapa()
	jogador.mostradinheiro(displaySurface)
	for i in lista_torres:
		displaySurface.blit(i.imagem, (i.posicaox, i.posicaoy))
	displaySurface.blit(invasores.sprite2,(invasores.posicaox, invasores.posicaoy))
	invasores.posicaox = invasores.posicaox + invasores.vx
	time.sleep(0.1)
	pygame.display.update()

	mapa()
	jogador.mostradinheiro(displaySurface)
	for i in lista_torres:
		displaySurface.blit(i.imagem, (i.posicaox, i.posicaoy))
	displaySurface.blit(invasores.sprite3,(invasores.posicaox, invasores.posicaoy))
	invasores.posicaox = invasores.posicaox + invasores.vx
	time.sleep(0.1)
	pygame.display.update()


def button(gameDisplay, msg, x, y, w, h, ic, ac, action, tamanho_letra, imagem):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	if msg == "none":
		image = pygame.image.load(imagem)
		gameDisplay.blit(image, (x, y))
		if x + w > mouse[0] > x and y + h > mouse[1] > y and action == "position":
			if click[0] == 1:
				return 1

	
	else:
		if x + w > mouse[0] > x and y + h > mouse[1] > y and msg != "none":
			pygame.draw.rect(gameDisplay, ac, (x, y, w, h))

			if click[0] == 1 and action == "start":			
				return 1
			if click[0] == 1 and action == "wave":
				return 1

			button_text = pygame.font.Font("freesansbold.ttf", tamanho_letra)
			TextSurf, TextRect = text_objects(msg, button_text)
			TextRect.center = ((x + w/2)), ((y + h/2))
			gameDisplay.blit(TextSurf, TextRect)

		elif msg != "none":
			pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
			button_text = pygame.font.Font("freesansbold.ttf", tamanho_letra)
			TextSurf, TextRect = text_objects(msg, button_text)
			TextRect.center = ((x + w/2)), ((y + h/2))
			gameDisplay.blit(TextSurf, TextRect)

	return 0



def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()



def game_intro(gameDisplay):
	file = ("musica1.mp3")
	pygame.mixer.music.load(file)
	pygame.mixer.music.play(-1)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		gameDisplay.fill(white)

		x = button(gameDisplay, "Defend your Castle!", 200, 270, 400, 50, green, bright_green, "start", 40, 0)

		if x == 1:
			break

		pygame.display.update()
		clock.tick(60)
	
	return 1

def game_loop(invasores):
	t = 0
	x = 0
	file = ("musica1.mp3")
	pygame.mixer.music.load(file)
	pygame.mixer.music.play(-1)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		if t == 0:
			surface = mapa()
			jogador.mostradinheiro(surface)
			t = 1
		elif t == 1:
			y = button(surface, "none", 150, 30, 30, 30, green, bright_green, "position", 10, "TORREE.png")
			if y == 1:
				torre.posicionar(surface, lista_torres, jogador)
				jogador.mostradinheiro(surface)
				t = 2			
		elif t == 2:
			x = button(surface, "Comeca", 1500, 310, 50, 20, green, bright_green, "wave", 10, 0)
			if x == 1:
				t = 3
		elif t == 3:
			movimentar(invasores, surface)
			Torres.distancia(torre,invasores)
			Torres.atacar(torre,invasores)
			if invasores.vida < 0:
				jogador.ganhadinheiro(invasores)
				jogador.mostradinheiro(surface)
				invasores = Invasores(10, 0, 0, 0, 10, "sprite_1.png", "sprite_2.png", "sprite_3.png", 2)
			

		pygame.display.update()
		clock.tick(60)


	
