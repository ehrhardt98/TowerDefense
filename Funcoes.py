import pygame
import time
from Mapa import *
from Classes import *

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
yellow = (255,255,100)
bright_yellow = (255,255,0)
logo0 = "logo0.png"
logo1 = "logo1.png"


zumbi1 = Invasores(10, 1200, 160, -10, 10, "zombie04.png", "zombie05.png", "zombie06.png", 2)
zumbi2 = Invasores(10, 1220, 160, -10, 10, "zombie04.png", "zombie05.png", "zombie06.png", 2)
zumbi3 = Invasores(10, 1240, 160, -10, 10, "zombie04.png", "zombie05.png", "zombie06.png", 2)
zumbi4 = Invasores(10, 1260, 160, -10, 10, "zombie04.png", "zombie05.png", "zombie06.png", 2)
invasoress = [zumbi1, zumbi2, zumbi3, zumbi4]

castelo = Castelo(10, 80,1)
torre1 = Torres(10, 100, 1, 10, "torrechoque_4.png", "agua")
torre2 = Torres(10, 100, 1, 10, "torrefogo_0.png", "agua")
torre3 = Torres(10, 100, 1, 5, "torredegelo0.png", "agua")
torre4 = Torres(10, 100, 1, 5, "TORREE.png", "agua")
jogador = Jogador(10, 25)
lista_torres = []


def pixel_matriz(pixelx, pixely):
	x = pixelx//40 + 1
	y = pixely//40 + 1
	posicaox = 40 * (x)
	posicaoy = 40 * (y)
	return [posicaox, posicaoy]




def movimentar(invasores, displaySurface):
	mapa()
	jogador.mostradinheiro(displaySurface, lista_torres)
	for i in lista_torres:
		displaySurface.blit(i.imagem, (i.posicaox, i.posicaoy))
	displaySurface.blit(invasores[0].sprite1,(invasores[0].posicaox, invasores[0].posicaoy))
	displaySurface.blit(invasores[1].sprite1, (invasores[1].posicaox, invasores[1].posicaoy))
	displaySurface.blit(invasores[2].sprite1, (invasores[2].posicaox, invasores[2].posicaoy))
	displaySurface.blit(invasores[3].sprite1, (invasores[3].posicaox, invasores[3].posicaoy))
	invasores[0].posicaox = invasores[0].posicaox + invasores[0].vx
	invasores[1].posicaox = invasores[1].posicaox + invasores[1].vx
	invasores[2].posicaox = invasores[2].posicaox + invasores[2].vx
	invasores[3].posicaox = invasores[3].posicaox + invasores[3].vx
	time.sleep(0.1)
	pygame.display.update()

	mapa()
	jogador.mostradinheiro(displaySurface, lista_torres)
	for i in lista_torres:
		displaySurface.blit(i.imagem, (i.posicaox, i.posicaoy))
	displaySurface.blit(invasores[0].sprite2,(invasores[0].posicaox, invasores[0].posicaoy))
	displaySurface.blit(invasores[1].sprite2, (invasores[1].posicaox, invasores[1].posicaoy))
	displaySurface.blit(invasores[2].sprite2, (invasores[2].posicaox, invasores[2].posicaoy))
	displaySurface.blit(invasores[3].sprite2, (invasores[3].posicaox, invasores[3].posicaoy))
	invasores[0].posicaox = invasores[0].posicaox + invasores[0].vx
	invasores[1].posicaox = invasores[1].posicaox + invasores[1].vx
	invasores[2].posicaox = invasores[2].posicaox + invasores[2].vx
	invasores[3].posicaox = invasores[3].posicaox + invasores[3].vx
	time.sleep(0.1)
	pygame.display.update()

	mapa()
	jogador.mostradinheiro(displaySurface, lista_torres)
	for i in lista_torres:
		displaySurface.blit(i.imagem, (i.posicaox, i.posicaoy))
	displaySurface.blit(invasores[0].sprite3,(invasores[0].posicaox, invasores[0].posicaoy))
	displaySurface.blit(invasores[1].sprite3, (invasores[1].posicaox, invasores[1].posicaoy))
	displaySurface.blit(invasores[2].sprite3, (invasores[2].posicaox, invasores[2].posicaoy))
	displaySurface.blit(invasores[3].sprite3, (invasores[3].posicaox, invasores[3].posicaoy))
	invasores[0].posicaox = invasores[0].posicaox + invasores[0].vx
	invasores[1].posicaox = invasores[1].posicaox + invasores[1].vx
	invasores[2].posicaox = invasores[2].posicaox + invasores[2].vx
	invasores[3].posicaox = invasores[3].posicaox + invasores[3].vx
	time.sleep(0.1)
	pygame.display.update()

	for x in invasores:
		if pixel_matriz(x.posicaox, x.posicaoy)[0] == pixel_matriz(castelo.posicaox, castelo.posicaoy)[0]:
			jogador.mostradinheiro(displaySurface, lista_torres)
			for i in lista_torres:
				displaySurface.blit(i.imagem, (i.posicaox, i.posicaoy))
			x.posicaox = -1000
			
			pygame.display.update()
			castelo.perdevida(invasores)


def button(gameDisplay, msg, x, y, w, h, ic, ac, action, tamanho_letra, imagem, imagem2):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	if msg == "none":
		image = pygame.image.load(imagem)
		
		gameDisplay.blit(image, (x, y))
		if x + w > mouse[0] > x and y + h > mouse[1] > y and action == "position":
			image2 = pygame.image.load(imagem2)
			gameDisplay.blit(image2, (x, y))
			if click[0] == 1:
				return 1
		if x + w > mouse[0] > x and y + h > mouse[1] > y and action == "start":
			image2 = pygame.image.load(imagem2)
			gameDisplay.blit(image2, (x, y))
			if click[0] == 1:
				return 1

	
	else:
		if x + w > mouse[0] > x and y + h > mouse[1] > y and msg != "none":
			pygame.draw.rect(gameDisplay, ac, (x, y, w, h))

			if click[0] == 1 and action == "start":			
				return 1
			if click[0] == 1 and action == "wave":
				return 2

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

		x = button(gameDisplay, "none", 200, 200, 400, 400, yellow, bright_yellow, "start", 40, "logo0.png", "logo1.png")

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
			jogador.mostradinheiro(surface, lista_torres)
			t = 1
		elif t == 1:

			while t == 1:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						quit()
				variavel_aux = 0
				if  variavel_aux == 0:
					y = button(surface, "none", 0, 60, 30, 30, green, bright_green, "position", 10, "torrechoque_0.png", "torrechoque_4.png")
					x = button(surface, "none", 0, 105, 30, 30, green, bright_green, "position", 10, "torrefogo_7.png", "torrefogo_0.png")
					z = button(surface, "none", 0, 150, 30, 30, green, bright_green, "position", 10, "torredegelo0.png", "torredegelo2.png")
					w = button(surface, "none", 0, 195, 30, 30, green, bright_green, "position", 10, "TORREE.png", "TORREE.png")
					
					pygame.display.update()
					
					if y == 1:
						
						torre1.posicionar(surface, lista_torres, jogador)
						jogador.mostradinheiro(surface, lista_torres)
					if x == 1:
						torre2.posicionar(surface, lista_torres, jogador)
						jogador.mostradinheiro(surface, lista_torres)	
					if z == 1:
						torre3.posicionar(surface, lista_torres, jogador)
						jogador.mostradinheiro(surface, lista_torres)	
					if w == 1:
						torre4.posicionar(surface, lista_torres, jogador)
						jogador.mostradinheiro(surface, lista_torres)	
						
					y = button(surface, "Wave1", 1150, 200, 50, 20, green, bright_green, "wave", 10, 0, 0)
					if y == 2:
						t = 2
		elif t == 2:

			zumatacado = invasoress[3]
			for x in range(0, len(invasoress)):
				
				if invasoress[x].posicaox > zumatacado.posicaox:
					zumatacado = invasoress[x]
				else:
					zumatacado = invasoress[x]
			
			
			movimentar(invasoress, surface)
			Torres.distancia(torre1, zumatacado)
			Torres.atacar(torre1, zumatacado)
			zumatacado.morte(jogador, surface, lista_torres)

			for x in range(0, len(invasoress)):
				if invasoress[x].posicaox > zumatacado.posicaox:
					zumatacado = invasoress[x]
			
			movimentar(invasoress, surface)
			Torres.distancia(torre2, zumatacado)
			Torres.atacar(torre2, zumatacado)
			zumatacado.morte(jogador, surface, lista_torres)
			for x in range(0, len(invasoress)):
				if invasoress[x].posicaox > zumatacado.posicaox:
					zumatacado = invasoress[x]
			
			movimentar(invasoress, surface)
			Torres.distancia(torre3, zumatacado)
			Torres.atacar(torre3,zumatacado)
			zumatacado.morte(jogador, surface, lista_torres)

			for x in range(0, len(invasoress)):
				if invasoress[x].posicaox > zumatacado.posicaox:
					zumatacado = invasoress[x]
			
			movimentar(invasoress, surface)
			Torres.distancia(torre4, zumatacado)
			Torres.atacar(torre4, zumatacado)
			zumatacado.morte(jogador, surface, lista_torres)



		pygame.display.update()
		clock.tick(60)