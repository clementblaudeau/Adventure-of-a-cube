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


class Boss:
	
	def __init__(self, niv):
		#variables en tous genres
		self.position = 0
		self.vie = 0
		try:
			self.image = pygame.image.load("images/boss"+str(niv)+".png").convert_alpha()
		except:
			self.image = pygame.image.load("images/boss1.png").convert_alpha()
		self.imghitbox = pygame.image.load("images/hitbox_boss.png").convert_alpha()
		self.j = 0
		self.temps = 0
		self.eclats = Eclat()
		self.fini = 0
		self.temps = 0
		self.niv = niv
		self.vagues = 0
		self.detruit = False
		self.position = (self.image.get_rect()).move(0,general.scrool)
		self.ennemisTues = 0
		self.hitbox = (self.imghitbox.get_rect()).move(general.w/2,50)
		try:
			self.fichier = open("niveaux/("+str(general.diff_level)+")/boss"+str(niv)+".bs", "r")
		except:
			self.fichier = open("niveaux/("+str(general.diff_level)+")/boss.bs", "r")
		self.contenu = self.fichier.readlines()
		b = 0
		c = 0
		for element in self.contenu:
			for lettres in element:
				c += 1
			self.contenu[b]= element[0:c-1]
			c = 0
			b += 1
		self.nbEnnemis = int(self.contenu[0])
		self.nbEnnemisf = int(self.contenu[1])
		self.sorteEnnemis = int(self.contenu[2])
		self.sorteEnnemisf = int(self.contenu[3])
		self.nbVagues = int(self.contenu[4])
		self.y1 = general.w/self.nbEnnemis
		self.y2 = general.w/self.nbEnnemisf
		try:
			self.nbObstacles = int(self.contenu[5])
			self.sorteObstacles = int(self.contenu[6])
		except:
			self.nbObstacles = 0
			self.sorteObstacles = 0
		self.fichier.close()
		
		
	def CollisionCube(self, hitbox):
		if self.Vivant() == True:
			if self.detruit == False:
				if hitbox.y <= (100 + self.position.y):
					return True
				else :
					return False

	def Scrool(self):
		self.position = self.position.move(0,1)
	
	def Tir(self,ennemis,obstacles):
		if self.position.y >= -50:
			if self.Vivant() == True:
				if (pygame.time.get_ticks() - self.temps) > 15000:
					if self.vagues < self.nbVagues:
						self.temps = pygame.time.get_ticks()
						self.vagues += 1
						i = 0
						while i < self.nbEnnemis:
							ennemis.NouvelEnnemi(self.sorteEnnemis, (((self.y1/2)-15)+(self.y1*i)), 30)
							i+=1
						i = 0
						while i < self.nbEnnemisf:
							ennemis.NouvelEnnemiFixe(self.sorteEnnemisf, (((self.y2/2)-15)+(self.y2*i)), 30)
							i+=1
						i = 0
						while i < self.nbObstacles:
							obstacles.NouvelObjet(self.sorteObstacles, (((self.y2/2)-15)+(self.y2*i)), 50)
							i+=1
			
	def Fini(self):
		if (self.detruit == True) and (self.eclats.positions == []):
			return True
		else:
			return False
			
	def CollisionTirs(self, tirs):
		if self.vagues >= self.nbVagues:
			for element in tirs:
				if element.colliderect(self.hitbox):
					if self.detruit == False:
						self.detruit = True
						self.eclats.Explosion(self.hitbox,40)
						return True
		return False
			
	def Vivant(self):
		if self.vagues <= self.nbVagues:
			return True
		else:
			if self.detruit == True:
				return False
			else:
				return True
				
	def Affichage(self, fenetre):
		if self.position.y >= -100:
			if self.detruit == False:
				fenetre.blit(self.image, self.position)
				if self.vagues >= self.nbVagues:
					fenetre.blit(self.imghitbox, self.hitbox)
		
		self.eclats.Affichage(fenetre)
	
