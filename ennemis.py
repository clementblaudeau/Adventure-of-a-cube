#------------------------------#
#          Ennemis.py          #
#		Clement Blaudeau	   #
#			******			   #
#------------------------------#

# -*- coding: utf-8 -*-


import pygame
from pygame.locals import *
from obstacles import * 
from animations import *


class Ennemis:
	
	def __init__(self):
		#variables en tous genres
		self.positions = []
		self.sortes = []
		self.vies = []
		self.tirs1 = []
		self.tirs2 = []
		self.tirs3 = []
		self.tirs4 = []
		self.positions_tirs = []
		self.bille = pygame.image.load("images/bille.png").convert_alpha()
		self.ennemis1 = pygame.image.load("images/ennemis1.png").convert_alpha()
		self.ennemis2 = pygame.image.load("images/ennemis2.png").convert_alpha()
		self.ennemis3 = pygame.image.load("images/ennemis3.png").convert_alpha()
		self.j = 0
		self.temps = pygame.time.get_ticks()
		self.eclats = Eclat()
		self.fini = 0
		
		
		
	def NouvelEnnemi(self, sorte, x, y):
		#Ajout d'un ennemi. A faire avec les niveaux
		self.positions.append(pygame.Rect(x,y,30,30))
		self.sortes.append(sorte)
		self.vies.append(sorte * 3)
		
	def CollisionCube(self, hitbox):
		#Collision avec le cube.
		#return True or False
		i = 0
		for element in self.positions:
			if element.colliderect(hitbox):
				self.eclats.Explosion(self.positions[i],self.sortes[i] * 3)
				self.vies.remove(self.vies[i])
				self.sortes.remove(self.sortes[i])
				self.positions.remove(self.positions[i])
				return True
			i+=1
		i = 0
		for element in self.tirs1:
			if element.colliderect(hitbox):
				self.tirs1.remove(element)
				return True
			i+=1
		for element in self.tirs2:
			if element.colliderect(hitbox):
				self.tirs2.remove(element)
				return True
			i+=1
		for element in self.tirs3:
			if element.colliderect(hitbox):
				self.tirs3.remove(element)
				return True
			i+=1
		for element in self.tirs4:
			if element.colliderect(hitbox):
				self.tirs4.remove(element)
				return True
			i+=1
		return False
		
	def CollisionsTirs(self, tirs, degats):
		#Test la colision avec les tirs
		i = 0
		for element in tirs:
			if element.top >= 0:
				for element2 in self.positions:
					if element2.colliderect(element) == True:
						try :
							tirs.remove(element)
						except:
							pass
						self.vies[i] =- degats
						if self.vies[i] <= 0:
							self.eclats.Explosion(self.positions[i],self.sortes[i] * 3)
							print self.sortes[i]
							self.vies.remove(self.vies[i])
							self.sortes.remove(self.sortes[i])
							self.positions.remove(element2)
					i +=1
			i = 0
		
		return tirs
		
	def Deplacements(self):
		#depaclement des ennemis en fonction de leurs paterns.
		i = 0
		for element in self.sortes:
			if element == 1:
				self.positions[i] = self.positions[i].move(0,1)
				if self.positions[i].top > 490:
					self.vies.remove(self.vies[i])
					self.sortes.remove(self.sortes[i])
					self.positions.remove(self.positions[i])
					print "mort !"
			elif element == 2:
				self.positions[i] = self.positions[i].move(1,0)
				if self.positions[i].left > 640:
					self.vies.remove(self.vies[i])
					self.sortes.remove(self.sortes[i])
					self.positions.remove(self.positions[i])
					print "mort !"
			elif element == 3:
				self.positions[i] = self.positions[i].move(-1,0)
				if self.positions[i].right < 0:
					self.vies.remove(self.vies[i])
					self.sortes.remove(self.sortes[i])
					self.positions.remove(self.positions[i])
					print "mort !"
			#elif element == 4:
			#elif element == 5:
			#elif element == 6:
			#elif element == 7:
			#elif element == 8:
			#elif element == 9:
			#elif element == 10:
			i+=1
			
			
	def Tir(self):
		#Tirs
		#Patern en fonction du type.
		if (pygame.time.get_ticks() - self.temps) > 500:
			self.temps = pygame.time.get_ticks()
			i = 0
			for element in self.sortes:
				if self.positions[i].bottom >= 0:
					if element == 1:
						self.tirs1.append(pygame.Rect(self.positions[i].left - 5,self.positions[i].top,10,10))
						self.tirs2.append(pygame.Rect(self.positions[i].right + 5,self.positions[i].top,10,10))
					if element == 2 or element == 3:
						self.tirs4.append(pygame.Rect(self.positions[i].centerx,self.positions[i].top - 5,10,10))
						self.tirs3.append(pygame.Rect(self.positions[i].centerx + 5,self.positions[i].bottom + 5,10,10))
					
				i += 1
				
	def Cleaner(self):
		i = 0
		for element in self.tirs1:
			if self.tirs1[i].right < 0:
				self.tirs1.remove(element)
				return 0
			i+=1
		i = 0
		for element in self.tirs2:
			if self.tirs2[i].left > 640:
				self.tirs2.remove(element)
				return 0
			i+=1
		i = 0
		for element in self.tirs3:
			if self.tirs3[i].top > 490:
				self.tirs3.remove(element)
				return 0
			i+=1
		i = 0
		for element in self.tirs4:
			if self.tirs4[i].bottom < 0:
				self.tirs4.remove(element)
				return 0
			i+=1
			
				
	def Affichage(self, fenetre):
		#Scrool, 
		#Affichage
		self.Cleaner()
		

		i = 0
		for element in self.tirs1:
			self.tirs1[i].right -= 1
			i+=1
		i =0
		for element in self.tirs2:
			self.tirs2[i].left += 1
			i+=1
		i = 0
		for element in self.tirs3:
			self.tirs3[i].bottom += 1
			i+=1
		i = 0
		for element in self.tirs4:
			self.tirs4[i].bottom -= 1
			i+=1
		i = 0
		for element in self.positions:
			if self.sortes[i] == 1:
				fenetre.blit(self.ennemis1, element)
			if self.sortes[i] == 2:
				fenetre.blit(self.ennemis2, element)
			if self.sortes[i] == 3:
				fenetre.blit(self.ennemis3, element)
			i+=1
			
		for element in self.tirs1:
			if not (element.right > 690) and not (element.left < -10) and not (element.top < -5) and not (element.bottom > 490):
				fenetre.blit(self.bille, element)
				
		for element in self.tirs2:
			if not (element.right > 690) and not (element.left < -10) and not (element.top < -5) and not (element.bottom > 490):
				fenetre.blit(self.bille, element)
				
		for element in self.tirs3:
			if not (element.right > 690) and not (element.left < -10) and not (element.top < -5) and not (element.bottom > 490):
				fenetre.blit(self.bille, element)
				
		for element in self.tirs4:
			if not (element.right > 690) and not (element.left < -10) and not (element.top < -5) and not (element.bottom > 490):
				fenetre.blit(self.bille, element)
		
		self.eclats.Affichage(fenetre)

