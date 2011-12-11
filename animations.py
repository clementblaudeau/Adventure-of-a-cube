import pygame
from pygame.locals import *	
import general


class Explosions:
	
	
	def __init__(self):
		self.positions = []
		self.niveau = []
		self.etapes = [
						pygame.image.load("images/explosion1.png").convert_alpha(),
						pygame.image.load("images/explosion2.png").convert_alpha(),
						pygame.image.load("images/explosion3.png").convert_alpha(),
						pygame.image.load("images/explosion4.png").convert_alpha()
						]
						

	def NouvelleExplosion(self, y, x):
		ttemp = self.etapes[1].get_rect()
		self.positions.append(ttemp.move(y,x))
		self.niveau.append(0)
		
	def Affichage(self, fenetre):
		i = 0
		for element in self.positions:
			self.niveau[i] += 1
			if self.niveau == 1:
				fenetre.blit(self.etapes[1], element)
			if self.niveau == 2:
				fenetre.blit(self.etapes[2], element)
			if self.niveau == 3:
				fenetre.blit(self.etapes[3], element)
			if self.niveau == 4:
				fenetre.blit(self.etapes[4], element)
			if self.niveau == 5:
				self.niveau.remove(5)
				self.positions.remove(element)
			i+=1
			

class Eclat:
	
	def __init__(self):
		self.eclat = pygame.image.load("images/eclat.png").convert_alpha()
		self.positions = []
		self.j = 0

	def Explosion(self, position, sorte):
		if sorte > 0:
			self.positions.append(position.move(12,12))
			self.positions.append(position.move(-12,-12))
		if sorte > 2:
			self.positions.append(position.move(-12,12))
			self.positions.append(position.move(12,-12))
		if sorte > 5:
			self.positions.append(position.move(0,15))
			self.positions.append(position.move(0,-15))
			self.positions.append(position.move(-15,0))
			self.positions.append(position.move(15,0))
	
	
	def Absorption(self, cub):
		retour = 0
		for element in self.positions:
			if cub.position.colliderect(element):
				self.positions.remove(element)
				retour += 10
		return retour

	def Affichage(self, fenetre):
		self.j += 1
		i = 0
		if self.j > 10:
			for element in self.positions:
				if (element.top > 660):
					self.positions.remove(element)
				else:
					self.positions[i] = self.positions[i].move(0,2)
				i += 1
			self.j = 0

		for element in self.positions:
			fenetre.blit(self.eclat, element)







