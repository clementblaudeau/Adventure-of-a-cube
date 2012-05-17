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
#	cub.py
#	Clement Blaudeau       
#	******	       
#------------------------------
#	Fichier qui gère le personnage
#	de Cube
#------------------------------


import pygame
from pygame.locals import *
from obstacles import * 
from text import *
from onde import *
from bombe import *
from tir import *
import general

class Cub:
	
	
	def __init__(self):
		self.image = pygame.image.load("../images/Cub/cub001.png").convert_alpha()
		self.position = self.image.get_rect()
		self.i = 1
		self.k = 0
		self.cube_actuel = "../images/Cub/cub002.png"
		self.hitbox = Rect(0,0,5,5)
		self.glissement_vertical = 0
		self.glissement_horizontal = 0
		self.degats = 0
		self.img_degat = pygame.image.load("../images/degats.png").convert_alpha()
		self.score = Score()
		self.vie = Vie()
		self.nivtirs = NivTirs()
		self.onde = Onde()
		self.tir1 = tir1()
		self.tir2 = tir2()
		self.bomb = Bomb()
		self.modelent = ModeLent()
		self.images = []
		self.ve = 0
		self.ho = 0
		while self.i <= 200:
			if self.i < 10:
				self.cube_actuel = "../images/Cub/cub00"+ str(self.i) +".png"
			elif self.i < 100:
				self.cube_actuel = "../images/Cub/cub0"+ str(self.i) +".png"
			elif self.i < 200:
				self.cube_actuel = "../images/Cub/cub"+ str(self.i) +".png"
			elif self.i == 200:
				self.cube_actuel = "../images/Cub/cub"+ str(self.i) +".png"
			self.images.append(pygame.image.load(self.cube_actuel).convert_alpha())
			self.i += 1
		self.i = 0
		
	def Rotation(self):
		if self.i > 199:
			self.i = 0
		self.image = self.images[self.i]
		self.i += 1
	
	def Action(self,key,mode,obstacles):
		
		if mode == "lent":
				if key[general.k_up] == True:
					self.DeplaceLent('haut', obstacles)
				if key[general.k_down] == True:
					self.DeplaceLent('bas', obstacles)
				if key[general.k_left] == True:
					self.DeplaceLent('gauche', obstacles)
				if key[general.k_right] == True:
					self.DeplaceLent('droite', obstacles)
				if (key[general.k_shot] == True) or (key[97] == True):
					self.tir2.Tir(self.position)
				if (key[general.k_shot2] == True) or (key[101] == True):
					self.onde.NewOnde(self.position.move(-70,-50))
		else:
				if key[general.k_up] == True:
					self.Deplace('haut',obstacles)
				if key[general.k_down] == True:
					self.Deplace('bas', obstacles)
				if key[general.k_left] == True:
					self.Deplace('gauche', obstacles)
				if key[general.k_right] == True:
					self.Deplace('droite', obstacles)
				if (key[general.k_shot] == True) or (key[97] == True):
					self.tir1.Tir(self.position)
				if (key[general.k_shot2] == True) or (key[101] == True):
					self.onde.NewOnde(self.position.move(-70,-50))
		
	def Deplace(self, direction, obstacles):
		if direction == 'bas':
			if self.position.bottom <= general.h+10 and not obstacles.ColisionsCube(self.hitbox.move(0,4)):
				self.position = self.position.move(0,4)
				self.hitbox = self.hitbox.move(0,4)
				if self.glissement_vertical < 40:
					self.glissement_vertical += 2

		elif direction == 'haut':
			if self.position.top >= 0 and not obstacles.ColisionsCube(self.hitbox.move(0,4)):
				self.position = self.position.move(0,-4)
				self.hitbox = self.hitbox.move(0,-4)
				if self.glissement_vertical > -40:
					self.glissement_vertical += -2

		elif direction == 'gauche':
			if self.position.left >= -10 and not obstacles.ColisionsCube(self.hitbox.move(-4,0)):
				self.position = self.position.move(-4,0)
				self.hitbox = self.hitbox.move(-4,0)
				if self.glissement_horizontal > -40:
					self.glissement_horizontal += -2

		elif direction == 'droite':
			if self.position.right <= general.w+10 and not obstacles.ColisionsCube(self.hitbox.move(4,0)):
				self.position = self.position.move(4,0)
				self.hitbox = self.hitbox.move(4,0)
				if self.glissement_horizontal < 40:
					self.glissement_horizontal += 2
				
				
	
	def Reboot(self):
		self.glissement_vertical = 0
		self.glissement_horizontal = 0
	
			
	def DeplaceLent(self, direction, obstacles):
		if direction == 'bas':
			if self.position.bottom <= general.h+10 and not obstacles.ColisionsCube(self.hitbox.move(0,2)):
				self.position = self.position.move(0,2)
				self.hitbox = self.hitbox.move(0,2)

		elif direction == 'haut':
			if self.position.top >= 0 and not obstacles.ColisionsCube(self.hitbox.move(0,-2)):
				self.position = self.position.move(0,-2)
				self.hitbox = self.hitbox.move(0,-2)

		elif direction == 'gauche':
			if self.position.left >= -10 and not obstacles.ColisionsCube(self.hitbox.move(-2,0)):
				self.position = self.position.move(-2,0)
				self.hitbox = self.hitbox.move(-2,0)

		elif direction == 'droite':
			if self.position.right <= general.w+10 and not obstacles.ColisionsCube(self.hitbox.move(2,0)):
				self.position = self.position.move(2,0)
				self.hitbox = self.hitbox.move(2,0)
				


	def Affichage(self, window):
		self.onde.Protect(self.hitbox)
		window.blit(self.image, self.position)	
		if self.degats > 0:
			self.degats -= 1
			if self.degats % 10:
				window.blit(self.img_degat, self.position.move(7,7))
		self.vie.Affichage(window)
		self.tir1.Affichage(window)
		self.tir2.Affichage(window)
		self.onde.Affichage(window)
		self.score.Affichage(window)
		self.nivtirs.Affichage(window)
		
	def Affichage2(self, window):
		window.blit(self.image, self.position)	

	def AvanceTirs(self):
	    self.tir1.Progress()
	    self.tir2.Progress()

	def Nettoyage(self):
		self.position.x = 0
		self.position.y = 0
		self.hitbox.x = 0
		self.hitbox.y = 0
		self.position = self.position.move(275,350)
		self.hitbox = self.hitbox.move(303,373)
		self.vie.vie = 5
		self.vie.vies_utilisees = 5
		self.score.score = 0
		self.glissement_vertical = 0
		self.glissement_horizontal = 0
		self.k = 0
		self.tir1 = tir1()
		self.tir2 = tir2()
		general.tirs = 0
		self.degats = 0
		general.n_bomb = 2
		
	def Nettoyage2(self):
		self.position.x = 0
		self.position.y = 0
		self.hitbox.x = 0
		self.hitbox.y = 0
		self.position = self.position.move(275,350)
		self.hitbox = self.hitbox.move(303,373)
		self.vie.vies_utilisees += 5-self.vie.vie
		self.vie.vie = 5
		self.glissement_vertical = 0
		self.glissement_horizontal = 0
		self.k = 0
		self.tir1 = tir1()
		self.tir2 = tir2()
		self.degats = 0
	
	def Glissement(self, obstacles):
		self.k +=1
		if self.k > 1:
			self.k = 0
			if (self.position.bottom <= general.h+10 and self.position.top >= 3) and not (obstacles.ColisionsCube(self.hitbox.move(0,-1)) or obstacles.ColisionsCube(self.hitbox.move(0,1))):
				if (self.glissement_vertical > 0):
					self.position = self.position.move(0,1)
					self.hitbox = self.hitbox.move(0,1)
					self.glissement_vertical = self.glissement_vertical - 1
				elif (self.glissement_vertical < 0):
					self.position = self.position.move(0,-1)
					self.hitbox = self.hitbox.move(0,-1)
					self.glissement_vertical = self.glissement_vertical + 1
				else:
					self.glissement_vertical = 0
		
			if (self.position.left >= -10 and self.position.right <= general.w+10) and not (obstacles.ColisionsCube(self.hitbox.move(10,0)) or obstacles.ColisionsCube(self.hitbox.move(-10,0))):
				if (self.glissement_horizontal > 0):
					self.position = self.position.move(1,0)
					self.hitbox = self.hitbox.move(1,0)
					self.glissement_horizontal = self.glissement_horizontal - 1
				elif (self.glissement_horizontal < 0):
					self.position = self.position.move(-1,0)
					self.hitbox = self.hitbox.move(-1,0)
					self.glissement_horizontal = self.glissement_horizontal + 1
				else:
					self.glissement_horizontal = 0

