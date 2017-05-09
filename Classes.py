import pygame
import time


class Torre:
	def __init__(self, ataque, raio, dps, custo, imagem, propriedade):
		self.ataque = ataque
		self.imagem = imagem
		self.raio = raio
		self.custo = custo
		self.dps = dps
		self.propriedade = propriedade

	def posicionar(self):
		while True:
			for event in pygame.event.get():
				if pygame.mouse.get_pressed()[0] == 1:
					self.posição = pygame.mouse.get_pos()
					game.Display.blit(self.imagem, (self.posição))
					break

	def distancia(self, inimigo):
		distancia = ((self.posição[0] - inimigo.posiçãox)**2 + (self.posição[1] - inimigo.posiçãoy)**2)**0.5
		return distancia

	def atacar(self, inimigo):
		while distancia(inimigo) <= self.raio:
			inimigo.vida = inimigo.vida - self.ataque
			time.sleep(self.dps)



class Castelo:
	def __init__(self, vida, posição_x, imagem):
		self.vida = vida
		self.posiçãox = posição_x
		self.imagem = pygame.image.load(imagem)
		
	def aparece(self):
		game.Display.blit(self.imagem, self.posiçaox)



class Invasores:
	def __init__(self, vida, posição_x, posição_y, velocidade_x, velocidade_y, imagem):
		self.vida = vida
		self.velocidade = velocidade
		self.posiçãox = posição_x
		self.posiçãoy = posição_y
		self.vx = velocidade_x
		self.vy = velocidade_y
		self.imagem = imagem

	def movimentar(self, mapa):
		while True:
			self.posiçãox = self.posiçãox + self.vx
			if self.posiçãox == castelo.posição_x:
				break

	def aparece(self):
			game.Display.blit(self.imagem, (self.posiçãox, self.posiçãoy))

