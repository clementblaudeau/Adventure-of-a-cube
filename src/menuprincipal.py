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
# 	menuprincipal.py
#	Clement Blaudeau       
#	******	       
#------------------------------
#	Fichier des menus à texte
#	(mode de jeu, difficulte, 
#	personnage, etc...)
#------------------------------


import pygame
from pygame.locals import *
import general
from cub import *
from boutons import *


class MenuPrincipal:
	
	def __init__(self):
		self.fond = pygame.image.load("../images/menu.png").convert_alpha()
		self.gagne = pygame.image.load("../images/fin_niveau.png").convert()
		self.boutons = Bouton_Text()
		self.lastclic = 0
		self.lastevent = 0
		self.ok = 0
		self.lastpos = (0,0)
		self.cube = Cub()
		self.cube.position = self.cube.position.move(100,100)
		self.boutons.NewBouton((general.w/2 - 100,170), "Histoire")
		self.boutons.NewBouton((general.w/2 - 100,220), "Fast Play")
		self.boutons.NewBouton((general.w/2 - 100,270), "Boss Rush",20,False)
		self.boutons.NewBouton((general.w/2 - 100,320), "Credits")
		
	def Menu_Display(self,window,boss):
		window.blit(pygame.image.load("../images/lv1.jpg").convert(), (general.w,0))
		window.blit(self.fond,(0,0))
		_continue = 1
		self.boutons = Bouton_Text()
		self.boutons.NewBouton((general.w/2 - 100,170), "Histoire")
		self.boutons.NewBouton((general.w/2 - 100,220), "Fast Play")
		self.boutons.NewBouton((general.w/2 - 100,270), "Boss Rush",20,boss)
		self.boutons.NewBouton((general.w/2 - 100,320), "Credits")
		self.boutons.NewBouton((general.w/2 - 100,370), "Quitter")
		
		self.boutons.Display(window, (0,0), 0)
		self.ok = 0
		self.ok2 = 0
		while _continue:
			tps_debut_boucle = pygame.time.get_ticks()
			window.blit(self.fond,(0,0))
			self.cube.Rotation()
			self.cube.Display2(window)
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					return 0
				if event.type == MOUSEMOTION:
					self.lastevent = event.dict["buttons"][0]
					self.lastpos = event.dict["pos"]
				if event.type == MOUSEBUTTONDOWN:
					self.lastevent = 1
				if event.type == MOUSEBUTTONUP:
					self.lastevent = 0
					if self.ok >= 1:
						if self.ok == 5:
							pygame.quit()
						return self.ok				
			if self.lastevent == 1:
				self.ok = self.boutons.Display(window, self.lastpos, 1)
			else:
				self.boutons.Display(window, self.lastpos, 0)
			
			pygame.display.flip()
			tps_fin_boucle = pygame.time.get_ticks()
			if tps_fin_boucle - tps_debut_boucle < 9:
				pygame.time.delay(9 -(tps_fin_boucle - tps_debut_boucle))
				
				
	def Choixpersonnage(self,window,pers=[True,True,True], ajout=""):
		self.boutons = Bouton_Text()
		self.boutons2 = Bouton_Text()
		self.font = pygame.font.Font("../polices/Coalition.ttf", 35)
		self.boutons.NewBouton((general.w/2 - 100,170), "Cub",20,pers[0])
		try:
			self.boutons.NewBouton((general.w/2 - 100,220), str(general.caracters[1]),20,pers[1])
			self.boutons.NewBouton((general.w/2 - 100,270), str(general.caracters[2]),20,pers[2])
		except:
			pass
		self.boutons2.NewBouton((general.w/2 + 100,370), "< Retour")
		window.blit(self.fond,(0,0))
		_continue = 1
		self.titre = (self.font.render(str(ajout), 1, (0, 0, 0)))
		self.pos_titre = self.titre.get_rect().move(100,100)
		self.boutons.Display(window, (0,0), 0)
		self.ok = 0
		while _continue:
			tps_debut_boucle = pygame.time.get_ticks()
			window.blit(self.fond,(0,0))
			self.cube.Rotation()
			window.blit(self.titre,(general.w / 2 - 150,130))
			self.cube.Display2(window)
			for event in pygame.event.get():
				if event.type == QUIT:
					return 0
				if event.type == MOUSEMOTION:
					self.lastevent = event.dict["buttons"][0]
					self.lastpos = event.dict["pos"]
				if event.type == MOUSEBUTTONDOWN:
					self.lastevent = 1
				if event.type == MOUSEBUTTONUP:
					self.lastevent = 0
					if self.ok >= 1:
						return self.ok		
					if self.ok2 >=1:
						general.back = True
						return 0
			if self.lastevent == 1:
				self.ok = self.boutons.Display(window, self.lastpos, 1)
				self.ok2 = self.boutons2.Display(window, self.lastpos, 1)
			else:
				self.boutons.Display(window, self.lastpos, 0)
				self.boutons2.Display(window, self.lastpos, 0)
			
			pygame.display.flip()
			tps_fin_boucle = pygame.time.get_ticks()
			if tps_fin_boucle - tps_debut_boucle < 9:
				pygame.time.delay(9 -(tps_fin_boucle - tps_debut_boucle))
				
	def ChoixLevel(self,window, niv,lock):
		self.boutons = Bouton_Text()
		self.boutons2 = Bouton_Text()
		self.font = pygame.font.Font("../polices/Coalition.ttf", 35)
		
		self.boutons.NewBouton((general.w/2 - 100,170), "Facile",20,lock[0])
		self.boutons.NewBouton((general.w/2 - 100,220), "Moyen",20,lock[1])
		self.boutons.NewBouton((general.w/2 - 100,270), "Difficile",20,lock[2])
		
		self.boutons2.NewBouton((general.w/2 + 100,370), "< Retour")
		window.blit(self.fond,(0,0))
		_continue = 1
		
		self.titre = (self.font.render(str("Level"), 1, (0, 0, 0)))
		self.boutons.Display(window, (0,0), 0)
		self.boutons2.Display(window, (0,0), 0)
		self.ok = 0
		while _continue:
			tps_debut_boucle = pygame.time.get_ticks()
			window.blit(self.fond,(0,0))
			self.cube.Rotation()
			window.blit(self.titre,(general.w / 2 - 150,130))
			self.cube.Display2(window)
			for event in pygame.event.get():
				if event.type == QUIT:
					return 0
				if event.type == MOUSEMOTION:
					self.lastevent = event.dict["buttons"][0]
					self.lastpos = event.dict["pos"]
				if event.type == MOUSEBUTTONDOWN:
					self.lastevent = 1
				if event.type == MOUSEBUTTONUP:
					self.lastevent = 0
					if self.ok >= 1:
						return self.ok		
					if self.ok2 >=1:
						general.back = True
						return 0
			if self.lastevent == 1:
				self.ok = self.boutons.Display(window, self.lastpos, 1)
				self.ok2 = self.boutons2.Display(window, self.lastpos, 1)
			else:
				self.boutons.Display(window, self.lastpos, 0)
				self.boutons2.Display(window, self.lastpos, 0)
			
			pygame.display.flip()
			tps_fin_boucle = pygame.time.get_ticks()
			if tps_fin_boucle - tps_debut_boucle < 9:
				pygame.time.delay(9 -(tps_fin_boucle - tps_debut_boucle))
	


