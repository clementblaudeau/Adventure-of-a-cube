import pygame
from pygame.locals import *	
import general


class Explosions:
	
	
	def __init__(self):
		self.positions = []
		self.images = [
		pygame.image.load("images/explosion1.png").convert_alpha(),
		pygame.image.load("images/explosion1a.png").convert_alpha(),
		pygame.image.load("images/explosion1a.png").convert_alpha(),
		pygame.image.load("images/explosion1b.png").convert_alpha(),
		pygame.image.load("images/explosion1b.png").convert_alpha(),
		pygame.image.load("images/explosion2.png").convert_alpha(),
		pygame.image.load("images/explosion2a.png").convert_alpha(),
		pygame.image.load("images/explosion2a.png").convert_alpha(),
		pygame.image.load("images/explosion2b.png").convert_alpha(),
		pygame.image.load("images/explosion2b.png").convert_alpha(),
		pygame.image.load("images/explosion3.png").convert_alpha(),
		pygame.image.load("images/explosion3a.png").convert_alpha(),
		pygame.image.load("images/explosion3a.png").convert_alpha(),
		pygame.image.load("images/explosion3b.png").convert_alpha(),
		pygame.image.load("images/explosion3b.png").convert_alpha(),
		pygame.image.load("images/explosion4.png").convert_alpha(),
		pygame.image.load("images/explosion4a.png").convert_alpha(),
		pygame.image.load("images/explosion4a.png").convert_alpha(),
		pygame.image.load("images/explosion4b.png").convert_alpha(),
		pygame.image.load("images/explosion4b.png").convert_alpha()]
						

	def NouvelleExplosion(self, x, y):
		self.positions.append([(x,y),0])
		
		
	def Affichage(self, fenetre):
		if self.positions != []:
			supp = []
			for i in range(len(self.positions)):
				fenetre.blit(self.images[self.positions[i][1]],self.positions[i][0])
				self.positions[i][1]+= 1
			for i in range(len(self.positions)):
				if self.positions[i][1] > 11:
					supp.append(i)
			for element in supp:
				try:
					self.positions.pop(element)
				except:
					pass
			
		
			

class Eclat:
	
	def __init__(self):
		self.eclat = pygame.image.load("images/eclat.png").convert_alpha()
		self.positions = []
		self.explosions = Explosions()
		self.j = 0

	def Explosion(self, position, sorte):
		self.explosions.NouvelleExplosion(position.left-50,position.top-50)
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
		self.explosions.Affichage(fenetre)
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







