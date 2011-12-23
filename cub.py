#------------------------------#
#			Cub.py			   #
#		Clement Blaudeau	   #
#			******			   #
#------------------------------#

# -*- coding: utf-8 -*-


import pygame
from pygame.locals import *
from obstacles import * 
from text import *
from onde import *
from tir import *
import general

class Cub:
	
	
	def __init__(self):
		self.image = pygame.image.load("images/cub001.png").convert_alpha()
		self.position = self.image.get_rect()
		self.i = 1
		self.k = 0
		self.cube_actuel = "images/cub002.png"
		self.hitbox = Rect(0,0,5,5)
		self.glissement_vertical = 0
		self.glissement_horizontal = 0
		self.degats = 0
		self.img_degat = pygame.image.load("images/degats.png").convert_alpha()
		self.score = Score()
		self.vie = Vie()
		self.nivtirs = NivTirs()
		self.onde = Onde()
		self.tir1 = tir1()
		self.tir2 = tir2()
		self.modelent = ModeLent()
		self.images = []
		self.ve = 0
		self.ho = 0
		while self.i <= 200:
			if self.i < 10:
				self.cube_actuel = "images/cub00"+ str(self.i) +".png"
			elif self.i < 100:
				self.cube_actuel = "images/cub0"+ str(self.i) +".png"
			elif self.i < 200:
				self.cube_actuel = "images/cub"+ str(self.i) +".png"
			elif self.i == 200:
				self.cube_actuel = "images/cub"+ str(self.i) +".png"
			self.images.append(pygame.image.load(self.cube_actuel).convert_alpha())
			self.i += 1
		self.i = 0
		
	def Rotation(self):
		if self.i > 199:
			self.i = 0
		self.image = self.images[self.i]
		self.i += 1
		
		
	def Deplace(self, direction, obstacles):
		if direction == 'bas':
			if self.position.bottom <= general.h+10 and not obstacles.ColisionsCube(self.hitbox.move(0,3)):
				self.position = self.position.move(0,3)
				self.hitbox = self.hitbox.move(0,3)
				if self.glissement_vertical < 40:
					self.glissement_vertical += 3

		elif direction == 'haut':
			if self.position.top >= 0 and not obstacles.ColisionsCube(self.hitbox.move(0,-3)):
				self.position = self.position.move(0,-3)
				self.hitbox = self.hitbox.move(0,-3)
				if self.glissement_vertical > -40:
					self.glissement_vertical += -3

		elif direction == 'gauche':
			if self.position.left >= -10 and not obstacles.ColisionsCube(self.hitbox.move(-3,0)):
				self.position = self.position.move(-3,0)
				self.hitbox = self.hitbox.move(-3,0)
				if self.glissement_horizontal > -40:
					self.glissement_horizontal += -3

		elif direction == 'droite':
			if self.position.right <= general.w+10 and not obstacles.ColisionsCube(self.hitbox.move(3,0)):
				self.position = self.position.move(3,0)
				self.hitbox = self.hitbox.move(3,0)
				if self.glissement_horizontal < 40:
					self.glissement_horizontal += 3
				
				
	
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
				


	def Affichage(self, fenetre):
		fenetre.blit(self.image, self.position)	
		if self.degats > 0:
			self.degats -= 1
			if self.degats % 10:
				fenetre.blit(self.img_degat, self.position.move(7,7))
		self.vie.Affichage(fenetre)
		self.tir1.Affichage(fenetre)
		self.tir2.Affichage(fenetre)
		self.onde.Affichage(fenetre)
		self.score.Affichage(fenetre)
		self.nivtirs.Affichage(fenetre)
		
	def Affichage2(self, fenetre):
		fenetre.blit(self.image, self.position)	

	def AvanceTirs(self):
	    self.tir1.Progression()
	    self.tir2.Progression()

	def Nettoyage(self):
		self.position.x = 0
		self.position.y = 0
		self.hitbox.x = 0
		self.hitbox.y = 0
		self.position = self.position.move(275,350)
		self.hitbox = self.hitbox.move(303,373)
		self.vie.vie = 5
		self.score.score = 0
		self.glissement_vertical = 0
		self.glissement_horizontal = 0
		self.k = 0
		self.tir1 = tir1()
		self.tir2 = tir2()
		general.tirs = 0
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

