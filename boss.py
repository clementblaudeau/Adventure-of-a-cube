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
		self.sorte = 0
		self.vie = 0 
		self.image = pygame.image.load("images/boss"+str(niv)+".png").convert_alpha()
		self.j = 0
		self.temps = 0
		self.eclats = Eclat()
		self.fini = 0
		self.temps = 0
		self.niv = niv
		self.detruit = False
		self.position = (self.image.get_rect()).move(0,-544)
		self.ennemisTues = 0
		self.hitbox = pygame.Rect(30,30,general.w/2,50)
		
		
	def CollisionCube(self, hitbox):
		if self.Vivant() == True:
			if hitbox.y <= (100 + self.position.y):
				return True
			else :
				return False

	def Scrool(self):
		self.position = self.position.move(0,1)
	
	def Tir(self,ennemis):
		if self.position.y >= -50:
			if self.Vivant() == True:
				if (pygame.time.get_ticks() - self.temps) > 15000:
					self.temps = pygame.time.get_ticks()
					i = 0
					self.ennemisTues += 5
					ennemis.NouvelEnnemiFixe(6, 30, 30)
					ennemis.NouvelEnnemi(5, 80, 30)
					ennemis.NouvelEnnemiFixe(4, 130, 30)
					ennemis.NouvelEnnemi(5, 180, 30)
					ennemis.NouvelEnnemiFixe(6, 230, 30)
					ennemis.NouvelEnnemi(6, 280, 30)
					ennemis.NouvelEnnemiFixe(4, 330, 30)
					ennemis.NouvelEnnemi(6, 380, 30)
					ennemis.NouvelEnnemiFixe(6, 430, 30)
					ennemis.NouvelEnnemi(4, 480, 30)
					ennemis.NouvelEnnemiFixe(4, 530, 30)
					ennemis.NouvelEnnemi(4, 580, 30)
					ennemis.NouvelEnnemiFixe(6, 630, 30)
			
	def Fini(self):
		if (self.ennemisTues > 30) and (self.eclats.positions == []):
			return True
		else:
			return False
			
	def CollisionTirs(self, tirs):
		if self.ennemisTues >= 30:
			for element in tirs:
				if element.colliderect(self.hitbox):
					self.detruit = True
					return True
		return False
			
	def Vivant(self):
		if self.ennemisTues <= 30:
			return True
		else:
			if self.detruit == True:
				return False
			else:
				return True
				
	def Affichage(self, fenetre):
		if self.position.y >= -100:
			if self.Vivant() == True:
				fenetre.blit(self.image, self.position)
		
		self.eclats.Affichage(fenetre)
	
