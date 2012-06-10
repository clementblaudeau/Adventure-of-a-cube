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
#   boss.py
#	Clement Blaudeau       
#	******	       
#------------------------------
#	Fichier qui gère le système 
#	du boss.
#------------------------------

import pygame
from pygame.locals import *
from obstacles import * 
from animations import *
from ennemis import *
import general
import pickle
import random


class Boss:
	
	def __init__(self, niv, pers):
		try:
			self.image = pygame.image.load("../images/boss"+str(niv)+".png")
		except:
			self.image = pygame.image.load("../images/boss1.png")
			print "erreur de Load de l'image"
		try:
			self.fichier = open("../niveaux/"+str(pers)+"/("+str(general.diff_level)+")/boss"+str(niv)+".bs", "r")
			print "../niveaux/"+str(pers)+"/("+str(general.diff_level)+")/boss"+str(niv)+".bs"
			boss = pickle.load(self.fichier)
			self.hitboxs = boss[0]
			self.timer = boss[1]
			self.tirs = boss[2]
			self.fichier.close()
		except:
			print "Erreur de Load du boss !"
			self.fichier = open("../niveaux/Cub/(1)/boss2.bs", "r")
			boss = pickle.load(self.fichier)
			self.hitboxs = boss[0]
			self.timer = boss[1]
			self.tirs = boss[2]
			self.fichier.close()
			for i in range(len(self.hitboxs)):
				self.hitboxs[i][1].top = general.scrool
		self.position = self.image.get_rect().move(0,general.scrool)
		self.time = 0
		self.sound = pygame.mixer.Sound("../son/mort.ogg")
		self.img_hitbox = pygame.image.load("../images/hitbox.png").convert_alpha()
		self.eclats = Eclat()
		self._done = False
		
		
	def CollisionCube(self, hitbox):
		if self.Fini() == False:
			for element in self.hitboxs:
				if hitbox.colliderect(element) == True:
					return True
		return False
			
	def Scrool(self):
		self.position = self.position.move(0,1)
		for i in range(len(self.hitboxs)):
			if int(str(self.hitboxs[i][2])) == 1:
				self.hitboxs[i][1] = self.hitboxs[i][1].move(0,1)
			elif int(str(self.hitboxs[i][2])) == 2:
				self.hitboxs[i][1] = self.hitboxs[i][1].move(1,0)
			elif int(str(self.hitboxs[i][2])) == 3:
				self.hitboxs[i][1] = self.hitboxs[i][1].move(-1,0)
			else:
				pass
				
	def Scrool_BossRush(self,scrool):
		if self._done == False:
			for i in range(len(self.hitboxs)):
				if int(str(self.hitboxs[i][2])) == 1:
					self.hitboxs[i][1] = self.hitboxs[i][1].move(0,444)
				elif int(str(self.hitboxs[i][2])) == 2:
					self.hitboxs[i][1] = self.hitboxs[i][1].move(444,0)
				elif int(str(self.hitboxs[i][2])) == 3:
					self.hitboxs[i][1] = self.hitboxs[i][1].move(-444,0)
				else:
					pass
			self._done = True
		else:
			pass
			
		self.position = self.position.move(0,1)
		
		for i in range(len(self.hitboxs)):
			if int(str(self.hitboxs[i][2])) == 1:
				self.hitboxs[i][1] = self.hitboxs[i][1].move(0,1)
			elif int(str(self.hitboxs[i][2])) == 2:
				self.hitboxs[i][1] = self.hitboxs[i][1].move(1,0)
			elif int(str(self.hitboxs[i][2])) == 3:
				self.hitboxs[i][1] = self.hitboxs[i][1].move(-1,0)
			else:
				pass
		
		
	def Move(self):
		for i in range(len(self.hitboxs)):
			if self.hitboxs[i][3][0] == 1:
				continue
			elif self.hitboxs[i][3][0] == 2:
				if self.hitboxs[i][1].left <= 5:
					self.hitboxs[i][3][1][0] = 1
				elif self.hitboxs[i][1].right >= general.w - 5:
					self.hitboxs[i][3][1][0] = -1
				self.hitboxs[i][1].left += self.hitboxs[i][3][1][0]
				continue
			elif self.hitboxs[i][3][0] == 3:
				if self.hitboxs[i][1].left <= 5:
					self.hitboxs[i][3][1][0] = 1
				elif self.hitboxs[i][1].right >= general.w - 5:
					self.hitboxs[i][3][1][0] = -1
				self.hitboxs[i][1].left += self.hitboxs[i][3][1][0]
				if self.hitboxs[i][1].top <= 5:
					self.hitboxs[i][3][1][1] = 1
				elif self.hitboxs[i][1].bottom >= general.h - 5:
					self.hitboxs[i][3][1][1] = -1
				self.hitboxs[i][1].top += self.hitboxs[i][3][1][1]
				continue
			elif self.hitboxs[i][3][0] == 4:
				r = random.randint(0,100)
				if r < 50:
					if self.hitboxs[i][1].left >= 5:
						self.hitboxs[i][1].left -= 2
					else:
						self.hitboxs[i][1].left += 2
				else:
					if self.hitboxs[i][1].right <= general.w - 5:
						self.hitboxs[i][1].right += 2
					else:
						self.hitboxs[i][1].right -= 2
				r = random.randint(0,100)
				if r < 50:
					if self.hitboxs[i][1].top >= 5:
						self.hitboxs[i][1].top -= 2
					else:
						self.hitboxs[i][1].top += 2
				else:
					if self.hitboxs[i][1].bottom <= general.h - 5:
						self.hitboxs[i][1].bottom += 2
					else:
						self.hitboxs[i][1].bottom -= 2
						
				
			
		
		
	def Tir(self,ennemis,obstacles):
		if (pygame.time.get_ticks() - self.time) >= self.timer:
			ennemis.Cleaner()
			self.time = pygame.time.get_ticks()
			for hitbox in self.hitboxs:
				if hitbox[0] >= 0:
					hitbox = hitbox[1]
					if (hitbox.bottom >= 0) and (hitbox.left >= 0) and (hitbox.left <= general.w):
						for element in self.tirs:
							if element == 1:
								ennemis.tirs1.append(pygame.Rect(hitbox.centerx,hitbox.centery,10,10))
							elif element == 2:
								ennemis.tirs2.append(pygame.Rect(hitbox.centerx,hitbox.centery,10,10))
							elif element == 3:
								ennemis.tirs3.append(pygame.Rect(hitbox.centerx,hitbox.centery,10,10))
							elif element == 4:
								ennemis.tirs4.append(pygame.Rect(hitbox.centerx,hitbox.centery,10,10))
							elif element == 5:
								ennemis.tirs5.append(pygame.Rect(hitbox.centerx,hitbox.centery,10,10))
							elif element == 6:
								ennemis.tirs6.append(pygame.Rect(hitbox.centerx,hitbox.centery,10,10))
							elif element == 7:
								ennemis.tirs7.append(pygame.Rect(hitbox.centerx,hitbox.centery,10,10))
							elif element == 8:
								ennemis.tirs8.append(pygame.Rect(hitbox.centerx,hitbox.centery,10,10))
							else:
								pass
							
							
							
	def Fini(self):
		for element in self.hitboxs:
			if element[0] >= 0:
				return False
		if self.eclats.positions != []:
			return False
		
		
		
		return True
			
	def CollisionTirs(self, tirs):
		for i in range(len(self.hitboxs)):
			for element in tirs:
				if self.hitboxs[i][1].top >= -10:
						if self.hitboxs[i][0] >= 0:
							if element.colliderect(self.hitboxs[i][1]) == True:
								self.hitboxs[i][0] -= 1
								self.eclats.Explosion(self.hitboxs[i][1],9)
								try:
									self.sound.set_volume(0.2)
									self.sound.play()
									tirs.remove(element)
								except:
									pass

				
	def Display(self, window):
		if self.position.bottom >= -5:
			self.Move()
		window.blit(self.image, self.position)
		for element in self.hitboxs:
			if element[0] >= 0:
				window.blit(self.img_hitbox,element[1].move(-5,-5))
		self.eclats.Display(window)
	
