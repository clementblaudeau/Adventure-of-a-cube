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
#	tir.py
#	Clement Blaudeau       
#	******	       
#------------------------------
#	Fichier qui gère les tirs
#	des personnages
#------------------------------


import pygame
from pygame.locals import *

import general




class tir1:
	
	def __init__(self):
		self.image = [pygame.image.load("../images/tir.png").convert_alpha(),pygame.image.load("../images/tir2.png").convert_alpha(),pygame.image.load("../images/tir3.png").convert_alpha()]
		self.son = pygame.mixer.Sound("../son/tir.ogg")
		self.positions = []
		self.k = 0
	
	def Progress(self):
		i = 0
		for element in self.positions:
			self.positions[i] = self.positions[i].move(0,-3)
			if self.positions[i].bottom < 0:
				self.positions.remove(self.positions[i])
			i +=1
			
			
	def Affichage(self, window):
		for element in self.positions:
			window.blit(self.image[general.niv], element)
			
	def Tir(self,position):
		if ((pygame.time.get_ticks() - self.k) > 100-(5*general.niv)):
		    self.k = pygame.time.get_ticks()
		    general.tirs += 1
		    self.son.set_volume(0.2)
		    self.son.play()
		    self.positions.append(Rect(0,0,20,30).move(position.left + 20, position.top - 10))
		
	
class tir2:
	
	def __init__(self):
		self.image = [pygame.image.load("../images/attaque.png").convert_alpha(),pygame.image.load("../images/attaque2.png").convert_alpha(),pygame.image.load("../images/attaque3.png").convert_alpha()]
		self.positions = []
		self.son = pygame.mixer.Sound("../son/tir2.ogg")
		self.k = 0
		
		
	def Progress(self):
		i = 0
		for element in self.positions:
			self.positions[i] = self.positions[i].move(0,-3)
			if self.positions[i].top < - 50:
				self.positions.remove(self.positions[i])
			i +=1
		
	def Affichage(self, window):
		for element in self.positions:
			window.blit(self.image[general.niv], element)
			
			
	def Tir(self,position):
		if ((pygame.time.get_ticks() - self.k) > 350-(5*general.niv)):
		    self.k = pygame.time.get_ticks()
		    self.positions.append(Rect(0,0,20,30).move(position.left + 20, position.top - 20))
		    self.son.play()
		    self.son.set_volume(0.2)
		    general.tirs += 3
		
	
	

















