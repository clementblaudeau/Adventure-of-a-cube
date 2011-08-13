import pygame
from pygame.locals import *





class tir1:
	
	def __init__(self):
		self.image = pygame.image.load("images/tir.png").convert_alpha()
		self.positions = []
	
	
	def Progression(self):
		i = 0
		for element in self.positions:
			self.positions[i] = self.positions[i].move(0,-3)
			if self.positions[i].top < - 50:
				self.positions.remove(self.positions[i])
			i +=1
			
			
	def Affichage(self, fenetre):
		for element in self.positions:
			fenetre.blit(self.image, element)
		
	
class tir2:
	
	def __init__(self):
		self.image = pygame.image.load("images/attaque.png").convert_alpha()
		self.positions = []
		
		
	def Progression(self):
		i = 0
		for element in self.positions:
			self.positions[i] = self.positions[i].move(0,-3)
			if self.positions[i].top < - 50:
				self.positions.remove(self.positions[i])
			i +=1
		
	def Affichage(self, fenetre):
		for element in self.positions:
			fenetre.blit(self.image, element)
		
	
	

















