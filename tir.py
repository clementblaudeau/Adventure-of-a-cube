#------------------------------#
#	Tir.py                 #
#	Clement Blaudeau       #
#            ******	       #
#------------------------------#


import pygame
from pygame.locals import *





class tir1:
	
	def __init__(self):
		self.image = pygame.image.load("images/tir.png").convert_alpha()
		self.positions = []
		self.k = 0
	
	def Progression(self):
		i = 0
		for element in self.positions:
			self.positions[i] = self.positions[i].move(0,-3)
			if self.positions[i].bottom < 0:
				self.positions.remove(self.positions[i])
			i +=1
			
			
	def Affichage(self, fenetre):
		for element in self.positions:
			fenetre.blit(self.image, element)
			
	def Tir(self,position):
		if self.k >= 15:
		    self.positions.append(Rect(0,0,20,30).move(position.left + 20, position.top - 10))
		    self.k = 0
		self.k += 1
		
	
class tir2:
	
	def __init__(self):
		self.image = pygame.image.load("images/attaque.png").convert_alpha()
		self.positions = []
		self.k = 0
		
		
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
			
			
	def Tir(self,position):
		if ((pygame.time.get_ticks() - self.k) > 350):
		    self.k = pygame.time.get_ticks()
		    self.positions.append(Rect(0,0,20,30).move(position.left + 20, position.top - 20))
		
		
	
	

















