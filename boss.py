# -*- coding: utf-8 -*-
#------------------------------#
#           Boss.py            #
#		Clement Blaudeau	   #
#			******			   #
#------------------------------#



import pygame
from pygame.locals import *
from obstacles import * 
from animations import *
from ennemis import *
import general
import pickle


class Boss:
	
	def __init__(self, niv, pers):
		try:
			self.image = pygame.image.load("images/boss"+str(niv)+".png")
		except:
			self.image = pygame.image.load("images/boss1.png")
		try:
			self.fichier = open("niveaux/"+str(pers)+"/("+str(general.diff_level)+")/boss"+str(niv)+".bs", "r")
			boss = pickle.load(self.fichier)
			self.hitboxs = boss[0]
			self.timer = boss[1]
			self.tirs = boss[2]
			self.fichier.close()
		except:
			self.fichier = open("niveaux/Cub/(1)/boss1.bs", "r")
			boss = pickle.load(self.fichier)
			self.hitboxs = boss[0]
			self.timer = boss[1]
			self.tirs = boss[2]
			self.fichier.close()
			for i in range(len(self.hitboxs)):
				self.hitboxs[i][1].top = general.scrool
		self.position = self.image.get_rect().move(0,general.scrool)
		self.time = 0
		self.son = pygame.mixer.Sound("son/mort.ogg")
		self.img_hitbox = pygame.image.load("images/hitbox.png").convert_alpha()
		self.eclats = Eclat()
		
		
	def CollisionCube(self, hitbox):
		if self.Fini() == False:
			if hitbox.y <= (100 + self.position.y):
				return True
			else :
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
		
		
		
		
		
	def Tir(self,ennemis,obstacles):
		if (pygame.time.get_ticks() - self.time) >= self.timer:
			ennemis.Cleaner()
			self.time = pygame.time.get_ticks()
			for hitbox in self.hitboxs:
				if hitbox[0] >= 0:
					hitbox = hitbox[1]
					if (hitbox.top >= 0) and (hitbox.left >= 0) and (hitbox.left <= general.w):
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
					if self.hitboxs[i][0] >= 0:
						if element.colliderect(self.hitboxs[i][1]) == True:
							self.hitboxs[i][0] -= 1
							self.eclats.Explosion(self.hitboxs[i][1],9)
							try:
								self.son.play()
								tirs.remove(element)
							except:
								pass

				
	def Affichage(self, fenetre):
		fenetre.blit(self.image, self.position)
		for element in self.hitboxs:
			fenetre.blit(self.img_hitbox,element[1].move(-5,-5))
		self.eclats.Affichage(fenetre)
	
