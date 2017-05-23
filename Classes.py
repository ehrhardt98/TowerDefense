import pygame
import time
import os, sys
import Funcoes
from Mapa import *

clock = pygame.time.Clock()



class Torres:
	def __init__(self, ataque, raio, dps, custo, imagem, propriedade):
		self.ataque = ataque
		self.imagem = pygame.image.load(imagem)
		self.raio = raio
		self.custo = custo
		self.dps = dps
		self.propriedade = propriedade
		self.posicao = [0,0]
		self.distancia = 0

	def comprar(self, jogador):
		if jogador.dinheiro >= self.custo:
			jogador.dinheiro = jogador.dinheiro - self.custo
			return True
		else:
			return False


	def posicionar(self, displaySurf, lista_torres, jogador):
		time.sleep(0.5)
		dinheiro_disponivel = self.comprar(jogador)
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()

			if dinheiro_disponivel == True:
				if pygame.mouse.get_pressed()[0] == 1:
					self.posicaoy = pygame.mouse.get_pos()[1]
					self.posicaox = pygame.mouse.get_pos()[0]
					displaySurf.blit(self.imagem, (self.posicaox, self.posicaoy))
					pygame.display.update()	
					lista_torres.append(self)
					return pixel_matriz(self.posicaox, self.posicaoy)
			else:
				return [1800, 1800]



	def distancia(self, inimigo):
		self.distancia = ((self.posicao[0] - inimigo.posicaox)**2 + (self.posicao[1] - inimigo.posicaoy)**2)**0.5
		return self.distancia

	def atacar(self, inimigo):
		if self.distancia >= self.raio:
			inimigo.vida = inimigo.vida - self.ataque
			print(inimigo.vida)
			print(self.ataque)
			time.sleep(self.dps)



class Castelo:
	def __init__(self, vida, posicao_x, posicao_y, imagem):
		self.vida = vida
		self.posicaox = posicao_x
		self.posicaoy = posicao_y
		self.imagem = pygame.image.load(imagem)



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
	def morte(self):
		if self.vida <= 0:			
			chaves = Invasores(10, 0, 0, 0, 10, "sprite_1.png", "sprite_2.png", "sprite_3.png")

class Jogador:
	def __init__(self, vida, dinheiro):
		self.vida = vida
		self.dinheiro = dinheiro

	def ganhadinheiro(self, invasores):
		if invasores.vida < 0:
			self.dinheiro = self.dinheiro + invasores.dinheiro
	
	def mostradinheiro(self, gameDisplay):
		text = pygame.font.Font("freesansbold.ttf", 10)
		TextSurf, TextRect = text_objects("Dinheiro: {0}".format(self.dinheiro), text)
		TextRect.center = ((20 + 20/2)), ((30 + 30/2))
		gameDisplay.blit(TextSurf, TextRect)