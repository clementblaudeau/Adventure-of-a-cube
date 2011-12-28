
#------------------------------#
#	Niveau.py	       #
#	Clement Blaudeau       #
#	******		       #
#------------------------------#

# -*- coding: utf-8 -*-


import pygame
from pygame.locals import *
from obstacles import * 
from ennemis import *
from boss import *
import general

class BossRush:
	
	def __init__(self):
		
		self.nom = "Boss Rush !"
		self.fond = pygame.image.load("images/lv1.jpg").convert()
	#	self.son = pygame.mixer.Sound("son/bossrush.wav")
		self.obstacles = Obstacles()
		self.ennemis = Ennemis(1)
		self.boss = Boss(1)
		self.niv = 1
		self.transition = False
		self.clear = False
		self.imgtransition = pygame.image.load("images/transition.png").convert()
		
		
	def Cleaner(self,cub):
		self.ennemis = Ennemis(1)
		#self.ennemis = Ennemis(self.niv)  <== Vrai version de la ligne
		self.obstacles = Obstacles()
		cub.Nettoyage2()		
		
	def Affichage(self, fenetre, scrool):
		if self.transition == False:
			fenetre.blit(self.fond, scrool)
			self.ennemis.Tir()
			self.boss.Tir(self.ennemis, self.obstacles)
			self.ennemis.Deplacements()
			self.boss.Affichage(fenetre)
			self.obstacles.Affichage(fenetre)
			self.ennemis.Affichage(fenetre)
		else:
			self.Transition(fenetre)
			
		
	def Fini(self):
		if self.ennemis.positions == []:
			if self.obstacles.positions == []:
				if self.obstacles.eclat.positions == []:
					if self.ennemis.eclats.positions == []:
						if self.ennemis.positionsf == []:
						    if self.boss.Fini() == True:
								if self.niv == 8:
									return True
								else:
									self.niv += 1
									self.boss = Boss(self.niv)
									self.transition = True
									self.clear = True
									self.compteur = 100
									general.scrool = -100
		return False
		
	def Transition(self,fenetre):
		if self.clear == True:
			self.clear = False
		fenetre.blit(self.imgtransition, (0,0))
		self.compteur -= 1
		if self.compteur == 0:
			self.compteur = 300
			self.transition = False
		

