#------------------------------#
#	Tir.py                 #
#	Clement Blaudeau       #
#            ******	       #
#------------------------------#


import pygame
from pygame.locals import *

import general




class tir1:
	
	def __init__(self):
		self.image = [pygame.image.load("images/tir.png").convert_alpha(),pygame.image.load("images/tir2.png").convert_alpha(),pygame.image.load("images/tir3.png").convert_alpha()]
		self.son = pygame.mixer.Sound("son/tir.ogg")
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
			fenetre.blit(self.image[general.niv], element)
			
	def Tir(self,position):
		if ((pygame.time.get_ticks() - self.k) > 100-(5*general.niv)):
		    self.k = pygame.time.get_ticks()
		    general.tirs += 1
		    self.son.play()
		    self.positions.append(Rect(0,0,20,30).move(position.left + 20, position.top - 10))
		
	
class tir2:
	
	def __init__(self):
		self.image = [pygame.image.load("images/attaque.png").convert_alpha(),pygame.image.load("images/attaque2.png").convert_alpha(),pygame.image.load("images/attaque3.png").convert_alpha()]
		self.positions = []
		self.son = pygame.mixer.Sound("son/tir2.ogg")
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
			fenetre.blit(self.image[general.niv], element)
			
			
	def Tir(self,position):
		if ((pygame.time.get_ticks() - self.k) > 350-(5*general.niv)):
		    self.k = pygame.time.get_ticks()
		    self.positions.append(Rect(0,0,20,30).move(position.left + 20, position.top - 20))
		    self.son.play()
		    general.tirs += 3
		
	
	

















