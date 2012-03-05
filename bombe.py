# -*- coding: utf-8 -*-

#------------------------------#
#			Bombe.py		   #
#		Clement Blaudeau       #
#	    	******	 	       #
#------------------------------#

import pygame
from pygame.locals import *	
import general


class Bomb:
	
	def __init__(self):
		self.k = 0
		self.images = [
		pygame.image.load("images/bomb01.png"),
		pygame.image.load("images/bomb02.png"),
		pygame.image.load("images/bomb03.png"),
		pygame.image.load("images/bomb04.png"),
		pygame.image.load("images/bomb05.png"),
		pygame.image.load("images/bomb06.png"),
		pygame.image.load("images/bomb07.png"),
		pygame.image.load("images/bomb08.png"),
		pygame.image.load("images/bomb09.png"),
		pygame.image.load("images/bomb10.png"),
		pygame.image.load("images/bomb11.png"),
		pygame.image.load("images/bomb12.png"),
		pygame.image.load("images/bomb13.png"),
		pygame.image.load("images/bomb14.png"),
		pygame.image.load("images/bomb15.png"),
		pygame.image.load("images/bomb16.png"),
		pygame.image.load("images/bomb17.png"),
		pygame.image.load("images/bomb18.png"),
		pygame.image.load("images/bomb19.png"),
		pygame.image.load("images/bomb20.png"),
		pygame.image.load("images/bomb21.png"),
		pygame.image.load("images/bomb22.png"),
		pygame.image.load("images/bomb23.png"),
		pygame.image.load("images/bomb24.png"),
		pygame.image.load("images/bomb25.png"),
		pygame.image.load("images/bomb26.png"),
		pygame.image.load("images/bomb27.png"),
		pygame.image.load("images/bomb28.png"),
		pygame.image.load("images/bomb29.png"),
		pygame.image.load("images/bomb30.png"),
		pygame.image.load("images/bomb31.png"),
		pygame.image.load("images/bomb32.png"),
		pygame.image.load("images/bomb33.png"),
		pygame.image.load("images/bomb34.png"),
		pygame.image.load("images/bomb35.png"),
		pygame.image.load("images/bomb36.png"),
		pygame.image.load("images/bomb37.png"),
		pygame.image.load("images/bomb38.png"),
		pygame.image.load("images/bomb39.png"),
		pygame.image.load("images/bomb40.png")]
		
	def Tir(self, ennemis,fenetre):
		if ((pygame.time.get_ticks() - self.k) > 10000):
			if general.n_bomb >= 0:
				general.n_bomb -= 1
				pygame.time.delay(500)
				for element in self.images:
					pygame.time.delay(50)
					fenetre.blit(element, (0,0))
					pygame.display.flip()
				ennemis.Nettoyage()
			self.k = pygame.time.get_ticks()


