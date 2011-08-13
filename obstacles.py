import pygame
from pygame.locals import *	


class Obstacles:
	
	def __init__(self):
		self.positions = []
		self.mur = pygame.image.load("images/mur.png").convert_alpha()
		self.vies = []
		self.sortes = []
		
		
	def NouvelObjet(self, sorte, hauteur, largeur, vie):
		self.temp = self.mur.get_rect()
		self.temp = self.temp.move(300, 300)
		self.positions.append(self.temp)
		self.vies.append(vie)
		self.sortes.append(sorte)
		
	def Affichage(self, fenetre):
		for element in self.positions:
			fenetre.blit(self.mur, element)
	
	def Colisions(self, positions_attaques):
		i = 0






