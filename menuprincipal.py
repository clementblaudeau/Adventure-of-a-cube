
# -*- coding: utf-8 -*-

#------------------------------#
# 		Menu Principal.py	   #
#		Clement Blaudeau	   #
#			******			   #
#------------------------------#


import pygame
from pygame.locals import *
import general
from cub import *
from boutons import *


class MenuPrincipal:
	
	def __init__(self):
		self.fond = pygame.image.load("images/"+general.screen+"/menu.png").convert_alpha()
		self.gagne = pygame.image.load("images/"+general.screen+"/fin_niveau.png").convert()
		self.boutons = Bouton_Text()
		self.lastclic = 0
		self.lastevent = 0
		self.ok = 0
		self.lastpos = (0,0)
		self.cube = Cub()
		self.cube.position = self.cube.position.move(100,100)
		self.boutons.NouveauBouton((general.w/2 - 100,170), "Histoire")
		self.boutons.NouveauBouton((general.w/2 - 100,220), "Fast Play")
		self.boutons.NouveauBouton((general.w/2 - 100,270), "Boss Rush",20,False)
		self.boutons.NouveauBouton((general.w/2 - 100,320), "Credits")
		
	def MenuAffichage(self,fenetre,boss):
		fenetre.blit(pygame.image.load("images/"+general.screen+"/lv1.jpg").convert(), (general.w,0))
		fenetre.blit(self.fond,(0,0))
		continuer = 1
		self.boutons = Bouton_Text()
		self.boutons.NouveauBouton((general.w/2 - 100,170), "Histoire")
		self.boutons.NouveauBouton((general.w/2 - 100,220), "Fast Play")
		self.boutons.NouveauBouton((general.w/2 - 100,270), "Boss Rush",20,boss)
		self.boutons.NouveauBouton((general.w/2 - 100,320), "Credits")
		self.boutons.NouveauBouton((general.w/2 - 100,370), "Quitter")
		
		self.boutons.Affichage(fenetre, (0,0), 0)
		self.ok = 0
		self.ok2 = 0
		while continuer:
			tps_debut_boucle = pygame.time.get_ticks()
			fenetre.blit(self.fond,(0,0))
			self.cube.Rotation()
			self.cube.Affichage2(fenetre)
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
				self.ok = self.boutons.Affichage(fenetre, self.lastpos, 1)
			else:
				self.boutons.Affichage(fenetre, self.lastpos, 0)
			
			pygame.display.flip()
			tps_fin_boucle = pygame.time.get_ticks()
			if tps_fin_boucle - tps_debut_boucle < 9:
				pygame.time.delay(9 -(tps_fin_boucle - tps_debut_boucle))
				
				
	def ChoixPersonnage(self,fenetre, ajout=""):
		self.boutons = Bouton_Text()
		self.boutons2 = Bouton_Text()
		self.font = pygame.font.Font("polices/Coalition.ttf", 35)
		self.boutons.NouveauBouton((general.w/2 - 100,170), "Cub")
		try:
			self.boutons.NouveauBouton((general.w/2 - 100,220), str(general.caracters[1]))
			self.boutons.NouveauBouton((general.w/2 - 100,270), str(general.caracters[2]))
		except:
			pass
		self.boutons2.NouveauBouton((general.w/2 + 100,370), "< Retour")
		fenetre.blit(self.fond,(0,0))
		continuer = 1
		self.titre = (self.font.render(str(ajout), 1, (0, 0, 0)))
		self.pos_titre = self.titre.get_rect().move(100,100)
		self.boutons.Affichage(fenetre, (0,0), 0)
		self.ok = 0
		while continuer:
			tps_debut_boucle = pygame.time.get_ticks()
			fenetre.blit(self.fond,(0,0))
			self.cube.Rotation()
			fenetre.blit(self.titre,(general.w / 2 - 150,130))
			self.cube.Affichage2(fenetre)
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
				self.ok = self.boutons.Affichage(fenetre, self.lastpos, 1)
				self.ok2 = self.boutons2.Affichage(fenetre, self.lastpos, 1)
			else:
				self.boutons.Affichage(fenetre, self.lastpos, 0)
				self.boutons2.Affichage(fenetre, self.lastpos, 0)
			
			pygame.display.flip()
			tps_fin_boucle = pygame.time.get_ticks()
			if tps_fin_boucle - tps_debut_boucle < 9:
				pygame.time.delay(9 -(tps_fin_boucle - tps_debut_boucle))
				
	def ChoixNiveau(self,fenetre, niv,lock):
		self.boutons = Bouton_Text()
		self.boutons2 = Bouton_Text()
		self.font = pygame.font.Font("polices/Coalition.ttf", 35)
		
		self.boutons.NouveauBouton((general.w/2 - 100,170), "Facile",20,lock[0])
		self.boutons.NouveauBouton((general.w/2 - 100,220), "Moyen",20,lock[1])
		self.boutons.NouveauBouton((general.w/2 - 100,270), "Difficile",20,lock[2])
		
		self.boutons2.NouveauBouton((general.w/2 + 100,370), "< Retour")
		fenetre.blit(self.fond,(0,0))
		continuer = 1
		
		self.titre = (self.font.render(str("Niveau"), 1, (0, 0, 0)))
		self.boutons.Affichage(fenetre, (0,0), 0)
		self.boutons2.Affichage(fenetre, (0,0), 0)
		self.ok = 0
		while continuer:
			tps_debut_boucle = pygame.time.get_ticks()
			fenetre.blit(self.fond,(0,0))
			self.cube.Rotation()
			fenetre.blit(self.titre,(general.w / 2 - 150,130))
			self.cube.Affichage2(fenetre)
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
				self.ok = self.boutons.Affichage(fenetre, self.lastpos, 1)
				self.ok2 = self.boutons2.Affichage(fenetre, self.lastpos, 1)
			else:
				self.boutons.Affichage(fenetre, self.lastpos, 0)
				self.boutons2.Affichage(fenetre, self.lastpos, 0)
			
			pygame.display.flip()
			tps_fin_boucle = pygame.time.get_ticks()
			if tps_fin_boucle - tps_debut_boucle < 9:
				pygame.time.delay(9 -(tps_fin_boucle - tps_debut_boucle))
	


