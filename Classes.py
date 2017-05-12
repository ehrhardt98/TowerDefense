import pygame
import time
import os, sys
import Funções
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


	def posicionar(self, displaySurf):
		time.sleep(1)
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			
			if pygame.mouse.get_pressed()[0] == 1:
				self.posiçãoy = pygame.mouse.get_pos()[1]
				self.posiçãox = pygame.mouse.get_pos()[0]
				displaySurf.blit(self.imagem, (self.posiçãox, self.posiçãoy))
				pygame.display.update()			
				return [self.posiçãox, self.posiçãoy]



	def distancia(self, inimigo):
		distancia = ((self.posição[0] - inimigo.posiçãox)**2 + (self.posição[1] - inimigo.posiçãoy)**2)**0.5
		return distancia

	def atacar(self, inimigo):
		while distancia(inimigo) <= self.raio:
			inimigo.vida = inimigo.vida - self.ataque
			time.sleep(self.dps)



class Castelo:
	def __init__(self, vida, posição_x, posição_y, imagem):
		self.vida = vida
		self.posiçãox = posição_x
		self.posiçãoy =posição_y
		self.imagem = pygame.image.load(imagem)



class Invasores:
	def __init__(self, vida, posição_x, posição_y, velocidade_x, velocidade_y, sprite1, sprite2, sprite3):
		self.vida = vida
		self.posiçãox = posição_x
		self.posiçãoy = posição_y
		self.vx = velocidade_x
		self.vy = velocidade_y
		self.sprite1 = pygame.image.load(sprite1)
		self.sprite2 = pygame.image.load(sprite2)
		self.sprite3 = pygame.image.load(sprite3)


