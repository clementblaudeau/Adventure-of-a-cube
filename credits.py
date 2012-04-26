
# -*- coding: utf-8 -*-

#------------------------------#
# 		Menu Principal.py	   #
#		Clement Blaudeau	   #
#			******			   #
#------------------------------#


import pygame
from pygame.locals import *
import general

class Credits:
	def __init__(self):
		self.e = 2
		
	def Affichage(self, fenetre):
		image = pygame.image.load("images/"+general.screen+"/credits.png").convert_alpha()
		continuer = 1
		while continuer:
			pygame.display.flip()
			fenetre.blit(image, (0,0))
			for event in pygame.event.get():
				if event.type == QUIT:
					continuer = 0
				if event.type == KEYDOWN:
					continuer = 0
