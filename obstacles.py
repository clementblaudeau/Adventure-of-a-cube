#------------------------------#
#		  Obstacles.py		   #
#		Clement Blaudeau	   #
#			******			   #
#------------------------------#
  
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *	
from animations import *



class Obstacles:
	
	def __init__(self):
		self.positions = []
		self.style1 = pygame.image.load("images/debris1.png").convert_alpha()
		self.style2 = pygame.image.load("images/mur.png").convert_alpha()
		self.style3 = pygame.image.load("images/mur.png").convert_alpha()
		self.style4 = pygame.image.load("images/mur.png").convert_alpha()
		self.style5 = pygame.image.load("images/mur.png").convert_alpha()
		self.style6 = pygame.image.load("images/mur.png").convert_alpha()
		self.style7 = pygame.image.load("images/mur.png").convert_alpha()
		self.vies = []
		self.sortes = []
		self.j = 0
		self.eclat = Eclat()
		
	def NouvelObjet(self, sorte, largeur, hauteur):
		self.temp = self.style1.get_rect()
		self.temp = self.temp.move(largeur, hauteur)
		self.positions.append(self.temp)
		self.vies.append(sorte * 3)
		self.sortes.append(sorte)
		
	def Affichage(self, fenetre):
		i = 0
		self.eclat.Affichage(fenetre)
		for element in self.positions:
			if self.sortes[i] == 1:
				fenetre.blit(self.style1, element)
			elif self.sortes[i] == 2:
				fenetre.blit(self.style2, element)
			elif self.sortes[i] == 3:
				fenetre.blit(self.style3, element)
			elif self.sortes[i] == 4:
				fenetre.blit(self.style4, element)
			elif self.sortes[i] == 5:
				fenetre.blit(self.style5, element)
			elif self.sortes[i] == 6:
				fenetre.blit(self.style6, element)
			elif self.sortes[i] == 7:
				fenetre.blit(self.style7, element)
			else:
				fenetre.blit(self.style1, element)
			i+=1
	
	def ColisionsCube(self, cub):
		for element in self.positions:
			if element.colliderect(cub) == True:
				return True
				
		return False
	
	def ColisionsTir(self, attaques, degats):
		i = 0
		for element in self.positions:
			for element2 in attaques:
					if element.left < element2.right and element.right > element2.left and element.bottom >= (element2.top - 8) and element.top <= element2.bottom:
						attaques.remove(element2)
						self.vies[i] = self.vies[i] - degats
						if self.vies[i] <= 0:
							self.eclat.Explosion(element,self.sortes[i])
							self.positions.remove(element)
							self.vies.remove(self.vies[i])
							self.sortes.remove(self.sortes[i])
							
			i += 1
		return attaques
	
	
	
	def Scrool(self, cub):
		self.j += 1
		i = 0
		if self.j > 10:
			for element in self.positions:
				self.positions[i] = self.positions[i].move(0,2)
				i += 1
			self.j = 0
			
			for element in self.positions:
				if element.top > 500:
					self.positions.remove(element)
					i -= 1
				i += 1
			




