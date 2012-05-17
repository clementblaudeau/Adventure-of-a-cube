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
#	BossRush.py	       
#	Clement Blaudeau       
#	******	       
#------------------------------
#	Fichier qui gère les niveaux
#	en mode BossRush
#------------------------------


import pygame
from pygame.locals import *
from obstacles import * 
from ennemis import *
from boss import *
from text import *
import general

class BossRush:
	
	def __init__(self, pers):
		
		self.nom = "Boss Rush !"
		self.fond = pygame.image.load("../images/lv1.jpg").convert()
		try:
		    self.son = pygame.mixer.Sound("../son/bossrush.wav")
		except:
		    self.son = pygame.mixer.Sound("../son/Cub/1.wav")
		self.obstacles = Obstacles()
		self.ennemis = Ennemis(1)
		self.boss = Boss(2, pers)
		self.niv = 1
		self.transition = False
		self.clear = False
		self.imgtransition = pygame.image.load("../images/transition.png").convert()
		self.chrono = Chrono()
		self.pers = pers
		
		
	def Cleaner(self,cub):
		self.ennemis = Ennemis(1)
		#self.ennemis = Ennemis(self.niv)  <== Vrai version de la ligne
		self.obstacles = Obstacles()
		cub.Nettoyage2()		
		
	def Display(self, window, scrool):
		if self.transition == False:
			window.blit(self.fond, scrool)
			self.ennemis.Tir()
			self.boss.Tir(self.ennemis, self.obstacles)
			self.ennemis.Deplacements()
			self.boss.Display(window)
			self.obstacles.Display(window)
			self.ennemis.Display(window)
			self.chrono.Display(pygame.time.get_ticks(), window, "")
		else:
			self.Transition(window)
			self.chrono.Display(pygame.time.get_ticks(), window, "")
			
	def Collisions(self,cub):
	    cub.tir1.positions = self.obstacles.ColisionsTir(cub.tir1.positions, 1+general.niv)
	    cub.tir2.positions = self.obstacles.ColisionsTir(cub.tir2.positions, 6+general.niv)
	    cub.tir1.positions = self.ennemis.CollisionsTirs(cub.tir1.positions, 1+general.niv)
	    cub.tir2.positions = self.ennemis.CollisionsTirs(cub.tir2.positions, 6+general.niv)
	    self.boss.CollisionTirs(cub.tir1.positions)
	    self.boss.CollisionTirs(cub.tir2.positions)
	    cub.score.score += self.obstacles.eclat.Absorption(cub)
	    cub.score.score += self.ennemis.eclats.Absorption(cub)
	    cub.score.score += self.boss.eclats.Absorption(cub)
	    if (self.ennemis.CollisionCube(cub.hitbox) == True):
			if cub.degats == 0:
				cub.vie.vie += -1
				cub.degats +=200
				cub.Reboot()
	    try:
		if (self.boss.CollisionCube(cub.hitbox) == True):
			if cub.degats == 0:
				cub.vie.vie += -1
				cub.degats +=200
				cub.Reboot()
	    except:
		pass
		
		
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
									self.boss = Boss(self.niv*2,self.pers)
									self.transition = True
									self.clear = True
									self.compteur = 100
									general.scrool = -100
		return False
		
	def Transition(self,window):
		if self.clear == True:
			self.clear = False
		window.blit(self.imgtransition, (0,0))
		self.compteur -= 1
		if self.compteur == 0:
			self.compteur = 300
			self.transition = False
		

