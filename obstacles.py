import pygame
from pygame.locals import *	


class Obstacles:
	
	def __init__(self):
		self.positions = []
		self.mur = pygame.image.load("images/mur.png").convert_alpha()
		self.vies = []
		self.sortes = []
		self.j = 0
		
		
	def NouvelObjet(self, sorte, hauteur, largeur, vie):
		self.temp = self.mur.get_rect()
		self.temp = self.temp.move(largeur, hauteur)
		self.positions.append(self.temp)
		self.vies.append(vie)
		self.sortes.append(sorte)
		
	def Affichage(self, fenetre):
		for element in self.positions:
			fenetre.blit(self.mur, element)
	
	def ColisionsCube(self, cub):
		for element in self.positions:
			if element.colliderect(cub) == True:
				return True
				
		return False
	
	def ColisionsTir(self, attaques):
		for element in self.positions:
			for element2 in attaques:
					if element.left < element2.right and element.right > element2.left and element.bottom >= element2.top:
						attaques.remove(element2)
		return attaques
	
	
	
	def Scrool(self, cub):
		self.j += 1
		i = 0
		if self.j > 15:
			for element in self.positions:
				self.positions[i] = self.positions[i].move(0,2)
				i += 1
			self.j = 0




