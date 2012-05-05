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
#	animations.py
#	Clement Blaudeau       
#	******	       
#------------------------------
#	Fichier qui gère les animations
#	des explosions et les points de
#	score lachés par les ennemis
#------------------------------


import pygame
from pygame.locals import *	
import general


class Explosions:
	
	
	def __init__(self):
		self.positions = []
		self.images = [
		pygame.image.load("images/explosion1.png").convert_alpha(),
		pygame.image.load("images/explosion1a.png").convert_alpha(),
		pygame.image.load("images/explosion1a.png").convert_alpha(),
		pygame.image.load("images/explosion1b.png").convert_alpha(),
		pygame.image.load("images/explosion1b.png").convert_alpha(),
		pygame.image.load("images/explosion2.png").convert_alpha(),
		pygame.image.load("images/explosion2a.png").convert_alpha(),
		pygame.image.load("images/explosion2a.png").convert_alpha(),
		pygame.image.load("images/explosion2b.png").convert_alpha(),
		pygame.image.load("images/explosion2b.png").convert_alpha(),
		pygame.image.load("images/explosion3.png").convert_alpha(),
		pygame.image.load("images/explosion3a.png").convert_alpha(),
		pygame.image.load("images/explosion3a.png").convert_alpha(),
		pygame.image.load("images/explosion3b.png").convert_alpha(),
		pygame.image.load("images/explosion3b.png").convert_alpha(),
		pygame.image.load("images/explosion4.png").convert_alpha(),
		pygame.image.load("images/explosion4a.png").convert_alpha(),
		pygame.image.load("images/explosion4a.png").convert_alpha(),
		pygame.image.load("images/explosion4b.png").convert_alpha(),
		pygame.image.load("images/explosion4b.png").convert_alpha()]
						

	def NouvelleExplosion(self, x, y):
		self.positions.append([(x,y),0])
		
		
	def Affichage(self, fenetre):
		if self.positions != []:
			supp = []
			for i in range(len(self.positions)):
				fenetre.blit(self.images[self.positions[i][1]],self.positions[i][0])
				self.positions[i][1]+= 1
			for i in range(len(self.positions)):
				if self.positions[i][1] > 11:
					supp.append(i)
			for element in supp:
				try:
					self.positions.pop(element)
				except:
					pass
			
		
			

class Eclat:
	
	def __init__(self):
		self.eclat = pygame.image.load("images/eclat.png").convert_alpha()
		self.positions = []
		self.explosions = Explosions()
		self.j = 0

	def Explosion(self, position, sorte):
		self.explosions.NouvelleExplosion(position.left-50,position.top-50)
		if sorte > 0:
			self.positions.append(position.move(12,12))
			self.positions.append(position.move(-12,-12))
		if sorte > 2:
			self.positions.append(position.move(-12,12))
			self.positions.append(position.move(12,-12))
		if sorte > 5:
			self.positions.append(position.move(0,15))
			self.positions.append(position.move(0,-15))
			self.positions.append(position.move(-15,0))
			self.positions.append(position.move(15,0))
	
	
	def Absorption(self, cub):
		retour = 0
		for element in self.positions:
			if cub.position.colliderect(element):
				self.positions.remove(element)
				retour += 10
		return retour

	def Affichage(self, fenetre):
		self.explosions.Affichage(fenetre)
		self.j += 1
		i = 0
		if self.j > 10:
			for element in self.positions:
				if (element.top > 660):
					self.positions.remove(element)
				else:
					self.positions[i] = self.positions[i].move(0,2)
				i += 1
			self.j = 0

		for element in self.positions:
			fenetre.blit(self.eclat, element)







