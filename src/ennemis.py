# -*- coding: utf-8 -*-
'''
Copyright (c) 2012 Clément Blaudeau
This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
'''
#------------------------------
#   ennemis.py
#	Clement Blaudeau       
#	******	       
#------------------------------
#	Fichier qui gère les ennemis,
#	leurs tirs, leur affichage,etc..
#------------------------------

import pygame
from pygame.locals import *
from obstacles import * 
from animations import *
import general


class Ennemis:
	
	def __init__(self, style):
		#variables en tous genres
		self.positions = []
		self.sortes = []
		self.vies = []
		self.positionsf = []
		self.sortesf = []
		self.viesf = []
		self.tirs1 = []
		self.tirs2 = []
		self.tirs3 = []
		self.tirs4 = []
		self.tirs5 = []
		self.tirs6 = []
		self.tirs7 = []
		self.tirs8 = []
		self.positions_tirs = []
		self.bille1 = pygame.image.load("../images/bille("+str(style)+").png").convert_alpha()
		self.bille2 = pygame.image.load("../images/bille("+str(style)+")(2).png").convert_alpha()
		self.bille3 = pygame.image.load("../images/bille("+str(style)+")(3).png").convert_alpha()
		self.bille = self.bille1
		self.ennemis1 = pygame.image.load("../images/("+str(style)+")/ennemis1.png").convert_alpha()
		self.ennemis2 = pygame.image.load("../images/("+str(style)+")/ennemis2.png").convert_alpha()
		self.ennemis3 = pygame.image.load("../images/("+str(style)+")/ennemis3.png").convert_alpha()
		self.ennemis4 = pygame.image.load("../images/("+str(style)+")/ennemis4.png").convert_alpha()
		self.ennemis5 = pygame.image.load("../images/("+str(style)+")/ennemis5.png").convert_alpha()
		self.ennemis6 = pygame.image.load("../images/("+str(style)+")/ennemis6.png").convert_alpha()
		self.ennemis_f1 = pygame.image.load("../images/("+str(style)+")/ennemis_f1.png").convert_alpha()
		self.ennemis_f2 = pygame.image.load("../images/("+str(style)+")/ennemis_f2.png").convert_alpha()
		self.ennemis_f3 = pygame.image.load("../images/("+str(style)+")/ennemis_f3.png").convert_alpha()
		self.ennemis_f4 = pygame.image.load("../images/("+str(style)+")/ennemis_f4.png").convert_alpha()
		self.ennemis_f5 = pygame.image.load("../images/("+str(style)+")/ennemis_f5.png").convert_alpha()
		self.ennemis_f6 = pygame.image.load("../images/("+str(style)+")/ennemis_f6.png").convert_alpha()
		self.j = 0
		self.son = pygame.mixer.Sound("../son/mort.ogg")
		self.temps = pygame.time.get_ticks()
		self.eclats = Eclat()
		self.fini = 0
		self.comp = False
		self.t_bille = 0
		self.t_bille2 = 0
		
	def NouvelEnnemi(self, sorte, x, y):
		#Ajout d'un ennemi. A faire avec les niveaux
		self.positions.append(pygame.Rect(x,y,30,30))
		self.sortes.append(sorte)
		if sorte == 6:
			self.comp == True
		self.vies.append(sorte * 3)
		
	def NouvelEnnemiFixe(self, sorte, x, y):
		#Ajout d'un ennemi. A faire avec les niveaux
		self.positionsf.append(pygame.Rect(x,y,30,30))
		self.sortesf.append(sorte)
		if sorte == 6:
			self.comp == True
		self.viesf.append(sorte * 3)
		
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
				general.niv = 0
				general.ennemis = 0
				return True
			i+=1
		i = 0
		for element in self.positionsf:
			if element.colliderect(hitbox):
				self.eclats.Explosion(self.positionsf[i],self.sortesf[i] * 3)
				self.viesf.remove(self.viesf[i])
				self.sortesf.remove(self.sortesf[i])
				self.positionsf.remove(self.positionsf[i])
				general.niv = 0
				general.ennemis = 0
				return True
			i+=1
		i = 0
		for element in self.tirs1:
			if element.colliderect(hitbox):
				self.tirs1.remove(element)
				general.niv = 0
				general.ennemis = 0
				return True
			i+=1
		for element in self.tirs2:
			if element.colliderect(hitbox):
				self.tirs2.remove(element)
				general.niv = 0
				general.ennemis = 0
				return True
			i+=1
		for element in self.tirs3:
			if element.colliderect(hitbox):
				self.tirs3.remove(element)
				general.niv = 0
				general.ennemis = 0
				return True
			i+=1
		for element in self.tirs4:
			if element.colliderect(hitbox):
				self.tirs4.remove(element)
				general.niv = 0
				general.ennemis = 0
				return True
			i+=1
		for element in self.tirs5:
			if element.colliderect(hitbox):
				self.tirs5.remove(element)
				general.niv = 0
				general.ennemis = 0
				return True
			i+=1
		for element in self.tirs6:
			if element.colliderect(hitbox):
				self.tirs6.remove(element)
				general.niv = 0
				general.ennemis = 0
				return True
			i+=1
		for element in self.tirs7:
			if element.colliderect(hitbox):
				self.tirs7.remove(element)
				general.niv = 0
				general.ennemis = 0
				return True
			i+=1
		for element in self.tirs8:
			if element.colliderect(hitbox):
				self.tirs8.remove(element)
				general.niv = 0
				general.ennemis = 0
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
							general.ennemis += 1
							self.eclats.Explosion(self.positions[i],self.sortes[i] * 3)
							self.vies.remove(self.vies[i])
							self.sortes.pop(i)
							self.positions.remove(element2)
							self.son.set_volume(0.2)
							self.son.play()
					i +=1
				i = 0
				for element2 in self.positionsf:
					if element2.colliderect(element) == True:
						try :
							tirs.remove(element)
						except:
							pass
						self.viesf[i] =- degats
						if self.viesf[i] <= 0:
							general.ennemis += 1
							self.eclats.Explosion(self.positionsf[i],self.sortesf[i] * 3)
							self.viesf.remove(self.viesf[i])
							self.sortesf.pop(i)
							self.positionsf.remove(element2)
							self.son.play()
					i +=1
			i = 0
		
		return tirs
		
	def Deplacements(self):
		#depaclement des ennemis en fonction de leurs paterns.
		i = 0
		for element in self.sortes:
			if element == 1 or element == 6:
				self.positions[i] = self.positions[i].move(0,1)
				if self.positions[i].top > general.h+10:
					self.vies.remove(self.vies[i])
					self.sortes.remove(self.sortes[i])
					self.positions.remove(self.positions[i])
			elif element == 2:
				self.positions[i] = self.positions[i].move(1,0)
				if self.positions[i].left > general.w:
					self.vies.remove(self.vies[i])
					self.sortes.remove(self.sortes[i])
					self.positions.remove(self.positions[i])
			elif element == 3:
				self.positions[i] = self.positions[i].move(-1,0)
				if self.positions[i].right < 0:
					self.vies.remove(self.vies[i])
					self.sortes.remove(self.sortes[i])
					self.positions.remove(self.positions[i])
			elif element == 4:
				self.positions[i] = self.positions[i].move(-1,1)
				if self.positions[i].right < 0 or self.positions[i].top > int(general.h) + 10:
					self.vies.remove(self.vies[i])
					self.sortes.remove(self.sortes[i])
					self.positions.remove(self.positions[i])
			elif element == 5:
				self.positions[i] = self.positions[i].move(1,1)
				if self.positions[i].left > 680 or self.positions[i].top > int(general.h) + 10:
					self.vies.remove(self.vies[i])
					self.sortes.remove(self.sortes[i])
					self.positions.remove(self.positions[i])
			#elif element == 6:
			#elif element == 7:
			i+=1
		    		
	def ScroolEnnemisFixes(self):
	    i = 0
	    for element in self.positionsf:
		self.positionsf[i] = element.move(0,1)
		i += 1
	    
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
					if element == 4 or element == 5:
						self.tirs4.append(pygame.Rect(self.positions[i].centerx,self.positions[i].top - 5,10,10))
						self.tirs3.append(pygame.Rect(self.positions[i].centerx + 5,self.positions[i].bottom + 5,10,10))
						self.tirs1.append(pygame.Rect(self.positions[i].left - 5,self.positions[i].top,10,10))
						self.tirs2.append(pygame.Rect(self.positions[i].right + 5,self.positions[i].top,10,10))
					if element == 6:
						self.tirs4.append(pygame.Rect(self.positions[i].centerx,self.positions[i].top - 5,10,10))
						self.tirs1.append(pygame.Rect(self.positions[i].left - 5,self.positions[i].top,10,10))
						self.tirs2.append(pygame.Rect(self.positions[i].right + 5,self.positions[i].top,10,10))
						self.tirs5.append(pygame.Rect(self.positions[i].right + 5,self.positions[i].top,10,10))
						self.tirs6.append(pygame.Rect(self.positions[i].right + 5,self.positions[i].top,10,10))
						self.tirs7.append(pygame.Rect(self.positions[i].right - 5,self.positions[i].bottom + 5,10,10))
						self.tirs8.append(pygame.Rect(self.positions[i].left + 5,self.positions[i].bottom + 5,10,10))
						self.tirs3.append(pygame.Rect(self.positions[i].centerx + 5,self.positions[i].bottom + 5,10,10))
					
				i += 1
			i = 0
			for element in self.sortesf:
				if self.positionsf[i].bottom >= 0:
					try:
						if element == 1:
							self.tirs1.append(pygame.Rect(self.positionsf[i].left - 5,self.positionsf[i].top+5,10,10))
						if element == 2 :
							self.tirs2.append(pygame.Rect(self.positionsf[i].right + 5,self.positionsf[i].top,10,10))
						if element == 3:
							self.tirs2.append(pygame.Rect(self.positionsf[i].right + 5,self.positionsf[i].top,10,10))
							self.tirs1.append(pygame.Rect(self.positionsf[i].left - 5,self.positionsf[i].top+5,10,10))
						if element == 4:
							self.tirs3.append(pygame.Rect(self.positionsf[i].centerx + 5,self.positionsf[i].bottom + 5,10,10))
						if element == 5:
							self.tirs3.append(pygame.Rect(self.positionsf[i].centerx + 5,self.positionsf[i].bottom + 5,10,10))
							self.tirs2.append(pygame.Rect(self.positionsf[i].right + 5,self.positionsf[i].top,10,10))
							self.tirs1.append(pygame.Rect(self.positionsf[i].left - 5,self.positionsf[i].top+5,10,10))
						if element == 6:
							self.tirs5.append(pygame.Rect(self.positionsf[i].right + 5,self.positionsf[i].top,10,10))
							self.tirs6.append(pygame.Rect(self.positionsf[i].right + 5,self.positionsf[i].top,10,10))
							self.tirs7.append(pygame.Rect(self.positionsf[i].right - 5,self.positionsf[i].bottom + 5,10,10))
							self.tirs8.append(pygame.Rect(self.positionsf[i].left + 5,self.positionsf[i].bottom + 5,10,10))
					except:
						pass
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
			if self.tirs2[i].left > general.w:
				self.tirs2.remove(element)
				return 0
			i+=1
		i = 0
		for element in self.tirs3:
			if self.tirs3[i].top > int(general.h) + 10:
				self.tirs3.remove(element)
				return 0
			i+=1
		i = 0
		for element in self.tirs4:
			if self.tirs4[i].bottom < 0:
				self.tirs4.remove(element)
				return 0
			i+=1
		i = 0
		for element in self.tirs5:
			if self.tirs5[i].bottom < 0:
				self.tirs5.remove(element)
				return 0
			i+=1
		i = 0
		for element in self.tirs6:
			if self.tirs6[i].bottom < 0:
				self.tirs6.remove(element)
				return 0
			i+=1
		i = 0
		for element in self.tirs7:
			if self.tirs7[i].top > int(general.h) + 10:
				self.tirs7.remove(element)
				return 0
			i+=1
		i = 0
		for element in self.tirs8:
			if self.tirs8[i].top > int(general.h) + 10:
				self.tirs8.remove(element)
				return 0
			i+=1			
				
	def Affichage(self, fenetre):
		#Scrool, 
		#Affichage
		self.Cleaner()
		
		if (pygame.time.get_ticks() - self.t_bille) >= 150:
			self.t_bille = pygame.time.get_ticks()
			if self.bille == self.bille1:
				self.bille = self.bille2
			elif self.bille == self.bille2:
				self.bille = self.bille3
			else:
				self.bille = self.bille1
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
		for element in self.tirs5:
			self.tirs5[i].bottom -= 1
			self.tirs5[i].right -= 1
			i+=1
		i = 0
		for element in self.tirs6:
			self.tirs6[i].bottom -= 1
			self.tirs6[i].right += 1
			i+=1
		i = 0
		for element in self.tirs7:
			self.tirs7[i].bottom += 1
			self.tirs7[i].right -= 1
			i+=1
		i = 0
		for element in self.tirs8:
			self.tirs8[i].bottom += 1
			self.tirs8[i].right += 1
			i+=1
		i = 0
		for element in self.positions:
			if self.sortes[i] == 1:
				fenetre.blit(self.ennemis1, element)
			if self.sortes[i] == 2:
				fenetre.blit(self.ennemis2, element)
			if self.sortes[i] == 3:
				fenetre.blit(self.ennemis3, element)
			if self.sortes[i] == 4:
				fenetre.blit(self.ennemis4, element)
			if self.sortes[i] == 5:
				fenetre.blit(self.ennemis5, element)
			if self.sortes[i] == 6:
				fenetre.blit(self.ennemis6, element)
			i+=1
		i = 0
		for element in self.positionsf:
			if self.sortesf[i] == 1:
				fenetre.blit(self.ennemis_f1, element)
			if self.sortesf[i] == 2:
				fenetre.blit(self.ennemis_f2, element)
			if self.sortesf[i] == 3:
				fenetre.blit(self.ennemis_f3, element)
			if self.sortesf[i] == 4:
				fenetre.blit(self.ennemis_f4, element)
			if self.sortesf[i] == 5:
				fenetre.blit(self.ennemis_f5, element)
			if self.sortesf[i] == 6:
				fenetre.blit(self.ennemis_f6, element)
			i+=1
		
		
		
		for element in self.tirs1:
			if not (element.right > int(general.w) + 10) and not (element.left < -10) and not (element.top < -5) and not (element.bottom > int(general.h) + 10):
				fenetre.blit(self.bille, element)
				
		for element in self.tirs2:
			if not (element.right > int(general.w) + 10) and not (element.left < -10) and not (element.top < -5) and not (element.bottom > int(general.h) + 10):
				fenetre.blit(self.bille, element)
				
		for element in self.tirs3:
			if not (element.right > int(general.w) + 10) and not (element.left < -10) and not (element.top < -5) and not (element.bottom > int(general.h) + 10):
				fenetre.blit(self.bille, element)
				
		for element in self.tirs4:
			if not (element.right > int(general.w) + 10) and not (element.left < -10) and not (element.top < -5) and not (element.bottom > int(general.h) + 10):
				fenetre.blit(self.bille, element)
				
		for element in self.tirs5:
			if not (element.right > int(general.w) + 10) and not (element.left < -10) and not (element.top < -5) and not (element.bottom > int(general.h) + 10):
				fenetre.blit(self.bille, element)
				
		for element in self.tirs6:
			if not (element.right > int(general.w) + 10) and not (element.left < -10) and not (element.top < -5) and not (element.bottom > int(general.h) + 10):
				fenetre.blit(self.bille, element)
				
		for element in self.tirs7:
			if not (element.right > int(general.w) + 10) and not (element.left < -10) and not (element.top < -5) and not (element.bottom > int(general.h) + 10):
				fenetre.blit(self.bille, element)
				
		for element in self.tirs8:
			if not (element.right > int(general.w) + 10) and not (element.left < -10) and not (element.top < -5) and not (element.bottom > int(general.h) + 10):
				fenetre.blit(self.bille, element)
		
		self.eclats.Affichage(fenetre)
	
	def Fini(self):
		self.Cleaner()
		if self.tirs1 == [] and self.tirs2 == [] and self.tirs3 == [] and self.tirs4 == [] and self.tirs5 == [] and self.tirs6 == [] and self.tirs7 == [] and self.tirs8 == []:
			return True
		else:
			return False
	
	
	def Nettoyage(self):
		self.tirs1 = []
		self.tirs2 = []
		self.tirs3 = []
		self.tirs4 = []
		self.tirs5 = []
		self.tirs6 = []
		self.tirs7 = []
		self.tirs8 = []
		self.CollisionsTirs([pygame.Rect(0,0,1000,1000),pygame.Rect(0,0,1000,1000),pygame.Rect(0,0,1000,1000),pygame.Rect(0,0,1000,1000),pygame.Rect(0,0,1000,1000)], 1000)
		self.CollisionsTirs([pygame.Rect(0,0,1000,1000),pygame.Rect(0,0,1000,1000),pygame.Rect(0,0,1000,1000),pygame.Rect(0,0,1000,1000),pygame.Rect(0,0,1000,1000)], 1000)
		self.CollisionsTirs([pygame.Rect(0,0,1000,1000),pygame.Rect(0,0,1000,1000),pygame.Rect(0,0,1000,1000),pygame.Rect(0,0,1000,1000),pygame.Rect(0,0,1000,1000)], 1000)
		self.CollisionsTirs([pygame.Rect(0,0,1000,1000),pygame.Rect(0,0,1000,1000),pygame.Rect(0,0,1000,1000),pygame.Rect(0,0,1000,1000),pygame.Rect(0,0,1000,1000)], 1000)
		
