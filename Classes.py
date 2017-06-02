import pygame
import time
import os, sys
import Funcoes
from Mapa import *

clock = pygame.time.Clock()

def pixel_matriz(pixelx, pixely):
	x = pixelx//40
	y = pixely//40
	posicaox = 40 * (x)
	posicaoy = 40 * (y)
	return [posicaox, posicaoy]



class Torres:
	def __init__(self, ataque, raio, dps, custo, imagem, propriedade):
		self.posicaox = 0
		self.posicaoy = 0
		self.ataque = ataque
		self.imagem = pygame.image.load(imagem)
		self.raio = raio
		self.custo = custo
		self.dps = dps
		self.propriedade = propriedade

	def comprar(self, jogador):
		if jogador.dinheiro >= self.custo:
			return True
		else:
			return False


	def posicionar(self, displaySurf, lista_torres, jogador):
		time.sleep(0.5)
		dinheiro_disponivel = self.comprar(jogador)
		while dinheiro_disponivel:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()

			if dinheiro_disponivel == True:
				if pygame.mouse.get_pressed()[0] == 1:
					self.posicaoy = pixel_matriz(pygame.mouse.get_pos()[1], pygame.mouse.get_pos()[0])[0]
					self.posicaox = pixel_matriz(pygame.mouse.get_pos()[1], pygame.mouse.get_pos()[0])[1]
					jogador.dinheiro = jogador.dinheiro - self.custo
					displaySurf.blit(self.imagem, (self.posicaox, self.posicaoy))
					pygame.display.update()
					lista_torres.append(self)
					return [self.posicaox, self.posicaoy]
			else:
				return [1800, 1800]



	def distancia(self, inimigo):
		self.distancia = ((self.posicaox - inimigo.posicaox)**2 + (self.posicaoy - inimigo.posicaoy)**2)**0.5
		

	def atacar(self, inimigo):
		if self.distancia <= self.raio:
			print( "atacando")
			inimigo.vida = inimigo.vida - self.ataque
			print(inimigo.vida)


class Castelo:
	def __init__(self, vida, posicao_x, posicao_y):
		self.vida = vida
		self.posicaox = posicao_x
		self.posicaoy = posicao_y
	
		
	def perdevida(self, invasores):
		print("1")
		if invasores.posicaox <= self.posicaox:
			print("2")
			print (self.vida)
			self.vida = self.vida - 10
			invasores.posicaox = 10000
			invasores.posicaoy = 5000


	def endgame(self):
		if self.vida <= 0:
			x = 3
			return x
		else:
			return 2




class Invasores:
	def __init__(self, vida, posicao_x, posicao_y, velocidade_x, velocidade_y, sprite1, sprite2, sprite3, dinheiro):
		self.vida = vida
		self.posicaox = posicao_x
		self.posicaoy = posicao_y
		self.posicao = [self.posicaox, self.posicaoy]
		self.vx = velocidade_x
		self.vy = velocidade_y
		self.sprite1 = pygame.image.load(sprite1)
		self.sprite2 = pygame.image.load(sprite2)
		self.sprite3 = pygame.image.load(sprite3)
		self.dinheiro = dinheiro

	def morte(self, jogador, gameDisplay, lista_torres):
		if self.vida <= 0:	
			self.posicaox = 10000
			jogador.ganhadinheiro(self)
			jogador.mostradinheiro(gameDisplay, lista_torres)


class Jogador:
	def __init__(self, vida, dinheiro):
		self.vida = vida
		self.dinheiro = dinheiro

	def ganhadinheiro(self, invasores):
		if invasores.vida <= 0:
			self.dinheiro = self.dinheiro + invasores.dinheiro
	
	def mostradinheiro(self, gameDisplay, lista_torres):
		mapa()
		for i in lista_torres:
			gameDisplay.blit(i.imagem, (i.posicaox, i.posicaoy))
		text = pygame.font.Font("freesansbold.ttf", 10)
		TextSurf, TextRect = text_objects("Dinheiro: {0}".format(self.dinheiro), text)
		TextRect.center = ((20 + 20/2)), ((30 + 30/2))
		gameDisplay.blit(TextSurf, TextRect)