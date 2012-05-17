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
		self.images = [pygame.image.load("../images/Wave/onde01.png").convert_alpha(),
		pygame.image.load("../images/Wave/onde02.png").convert_alpha(),
		pygame.image.load("../images/Wave/onde03.png").convert_alpha(),
		pygame.image.load("../images/Wave/onde04.png").convert_alpha(),
		pygame.image.load("../images/Wave/onde05.png").convert_alpha(),
		pygame.image.load("../images/Wave/onde06.png").convert_alpha(),
		pygame.image.load("../images/Wave/onde07.png").convert_alpha(),
		pygame.image.load("../images/Wave/onde08.png").convert_alpha(),
		pygame.image.load("../images/Wave/onde09.png").convert_alpha(),
		pygame.image.load("../images/Wave/onde10.png").convert_alpha(),
		pygame.image.load("../images/Wave/onde11.png").convert_alpha(),
		pygame.image.load("../images/Wave/onde12.png").convert_alpha(),
		pygame.image.load("../images/Wave/onde13.png").convert_alpha(),
		pygame.image.load("../images/Wave/onde14.png").convert_alpha(),
		pygame.image.load("../images/Wave/onde15.png").convert_alpha(),
		pygame.image.load("../images/Wave/onde16.png").convert_alpha(),
		pygame.image.load("../images/Wave/onde17.png").convert_alpha(),
		pygame.image.load("../images/Wave/onde18.png").convert_alpha(),
		pygame.image.load("../images/Wave/onde19.png").convert_alpha(),
		pygame.image.load("../images/Wave/onde20.png").convert_alpha()]
		self.position = False
		self.progress = 0
		self.temps = 0
		self.time_progress = 0
		general.c_protect = False
		
	def NewOnde(self, position):
		if (pygame.time.get_ticks() - self.temps) > 1500:
			self.temps = pygame.time.get_ticks()
			temp = self.images[0].get_rect()
			self.position = temp.move(position.x, position.y)
			self.progress = 0
		
	def Progress(self):
		if self.position != False:
			if pygame.time.get_ticks() - self.time_progress > 50:
				self.time_progress = pygame.time.get_ticks()
				self.progress += 1
				if self.progress >= 20:
					self.progress = 0
					self.position = False
					general.c_protect = False
			
	def Protect(self, cub):
		if self.position != False:
			general.c_protect = False
			if self.progress >= 1:
				if self.position.colliderect(cub) == True:
					general.c_protect = True
				
	def Level(self, a=0):
		return self.images[self.progress + a]

	def Affichage(self, window):
		self.Progress()
		if self.position != False:
			window.blit(self.Level(),self.position)
			window.blit(self.Level(-1),self.position)




