#------------------------------#
#			Menu.py			   #
#		Clement Blaudeau	   #
#			******			   #
#------------------------------#

# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

class Menu:
	
	def __init__(self):
		self.fond = pygame.image.load("images/menu.png").convert_alpha()
		self.gagne = pygame.image.load("images/fin_niveau.png").convert()
		
	def MenuAffichage(self,fenetre):
		fenetre.blit(self.fond,(0,0))
		print "bon"
		continuer = 1
		while continuer:
			fenetre.blit(self.fond,(0,0))
			pygame.display.flip()
			for event in pygame.event.get():
				print event.dict
				if event.type == QUIT:
					continuer = 0
					return 0
				if event.type == MOUSEBUTTONDOWN:
					print event.dict['pos']
					if (event.dict["pos"][1] > 147) and (event.dict["pos"][1] < 207):
						if event.dict["pos"][0] > 50 and event.dict["pos"][0] < 180:
							continuer = 0
							return 1

	def FinNiveau(self, score, vies, fenetre):
		if vies > 0:
			image = self.gagne
		else:
			image = pygame.image.load("images/game_over.png").convert()
		fenetre.blit(image,(0,0))
		
		continuer = 1
		while continuer:
			fenetre.blit(image,(0,0))
			pygame.display.flip()
			for event in pygame.event.get():
				print event.dict
				if event.type == QUIT:
					continuer = 0
				if event.type == MOUSEBUTTONDOWN:
							continuer = 0

