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
#	onde.py
#	Clement Blaudeau       
#	******	       
#------------------------------
#	Fichier qui prend en charge
#	les attaques d'ondes.
#------------------------------

import pygame
from pygame.locals import *
import general

class Onde:
	
	def __init__(self):
		self.onde01 = pygame.image.load("../images/onde01.png").convert_alpha()
		self.onde02 = pygame.image.load("../images/onde02.png").convert_alpha()
		self.onde03 = pygame.image.load("../images/onde03.png").convert_alpha()
		self.onde04 = pygame.image.load("../images/onde04.png").convert_alpha()
		self.onde05 = pygame.image.load("../images/onde05.png").convert_alpha()
		self.onde06 = pygame.image.load("../images/onde06.png").convert_alpha()
		self.onde07 = pygame.image.load("../images/onde07.png").convert_alpha()
		self.onde08 = pygame.image.load("../images/onde08.png").convert_alpha()
		self.onde09 = pygame.image.load("../images/onde09.png").convert_alpha()
		self.onde10 = pygame.image.load("../images/onde10.png").convert_alpha()
		self.onde11 = pygame.image.load("../images/onde11.png").convert_alpha()
		self.onde12 = pygame.image.load("../images/onde12.png").convert_alpha()
		self.onde13 = pygame.image.load("../images/onde13.png").convert_alpha()
		self.onde14 = pygame.image.load("../images/onde14.png").convert_alpha()
		self.onde15 = pygame.image.load("../images/onde15.png").convert_alpha()
		self.onde16 = pygame.image.load("../images/onde16.png").convert_alpha()
		self.onde17 = pygame.image.load("../images/onde17.png").convert_alpha()
		self.onde18 = pygame.image.load("../images/onde18.png").convert_alpha()
		self.onde19 = pygame.image.load("../images/onde19.png").convert_alpha()
		self.onde20 = pygame.image.load("../images/onde20.png").convert_alpha()
		self.positions = []
		self.progressions = []
		self.protect = True
		self.temps = 0
		
	def NouvelleOnde(self, position):
		if (pygame.time.get_ticks() - self.temps) > 1500:
			self.temps = pygame.time.get_ticks()
			temp = self.onde01.get_rect()
			position = temp.move(position.x, position.y)
			self.positions.append(position)
			self.progressions.append(0)
		
	def Progression(self):
		i = 0
		for element in self.positions:
			general.tirs += 2
			self.progressions[i] += 0.05
			if self.progressions[i] > 5:
				self.progressions.remove(self.progressions[i])
				self.positions.remove(self.positions[i])
			i +=1
	
	def Protege(self, cub):
		i = 0
		general.c_protect = False
		for element in self.positions:
			if self.progressions[i] > 1:
				if element.colliderect(cub) == True:
					general.c_protect = True
					
				
			i+=1
	
	def Niveau(self, a):
		if a <= 0.25:
			return self.onde01
		elif a <= 0.5:
			return self.onde02
		elif a <= 0.75:
			return self.onde03
		elif a <= 1:
			return self.onde04
		elif a <= 1.25:
			return self.onde05
		elif a <= 1.5:
			return self.onde06
		elif a <= 1.75:
			return self.onde07
		elif a <= 2:
			return self.onde08
		elif a <= 2.25:
			return self.onde09
		elif a <= 2.5:
			return self.onde10
		elif a <= 2.75:
			return self.onde11
		elif a <= 3:
			return self.onde12
		elif a <= 3.25:
			return self.onde13
		elif a <= 3.5:
			return self.onde14
		elif a <= 3.75:
			return self.onde15
		elif a <= 4:
			return self.onde16
		elif a <= 4.25:
			return self.onde17
		elif a <= 4.5:
			return self.onde18
		elif a <= 4.75:
			return self.onde19
		elif a <= 5:
			return self.onde20
		else:
			return self.onde20

	def Affichage(self, fenetre):
		self.Progression()
		i = 0
		for element in self.positions:
			fenetre.blit(self.Niveau(self.progressions[i]), element)
			fenetre.blit(self.Niveau(self.progressions[i]-0.25), element)
			i +=1




