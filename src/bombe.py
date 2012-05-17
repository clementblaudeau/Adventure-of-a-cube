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
#	bombe.py		   
#	Clement Blaudeau       
#	******	       
#------------------------------
#	Fichier qui gère l'utilisation
#	de la bombe
#------------------------------

import pygame
from pygame.locals import *	
import general


class Bomb:
	
	def __init__(self):
		self.k = 0
		self.images = [
		pygame.image.load("../images/Bomb/bomb01.png"),
		pygame.image.load("../images/Bomb/bomb02.png"),
		pygame.image.load("../images/Bomb/bomb03.png"),
		pygame.image.load("../images/Bomb/bomb04.png"),
		pygame.image.load("../images/Bomb/bomb05.png"),
		pygame.image.load("../images/Bomb/bomb06.png"),
		pygame.image.load("../images/Bomb/bomb07.png"),
		pygame.image.load("../images/Bomb/bomb08.png"),
		pygame.image.load("../images/Bomb/bomb09.png"),
		pygame.image.load("../images/Bomb/bomb10.png"),
		pygame.image.load("../images/Bomb/bomb11.png"),
		pygame.image.load("../images/Bomb/bomb12.png"),
		pygame.image.load("../images/Bomb/bomb13.png"),
		pygame.image.load("../images/Bomb/bomb14.png"),
		pygame.image.load("../images/Bomb/bomb15.png"),
		pygame.image.load("../images/Bomb/bomb16.png"),
		pygame.image.load("../images/Bomb/bomb17.png"),
		pygame.image.load("../images/Bomb/bomb18.png"),
		pygame.image.load("../images/Bomb/bomb19.png"),
		pygame.image.load("../images/Bomb/bomb20.png"),
		pygame.image.load("../images/Bomb/bomb21.png"),
		pygame.image.load("../images/Bomb/bomb22.png"),
		pygame.image.load("../images/Bomb/bomb23.png"),
		pygame.image.load("../images/Bomb/bomb24.png"),
		pygame.image.load("../images/Bomb/bomb25.png"),
		pygame.image.load("../images/Bomb/bomb26.png"),
		pygame.image.load("../images/Bomb/bomb27.png"),
		pygame.image.load("../images/Bomb/bomb28.png"),
		pygame.image.load("../images/Bomb/bomb29.png"),
		pygame.image.load("../images/Bomb/bomb30.png"),
		pygame.image.load("../images/Bomb/bomb31.png"),
		pygame.image.load("../images/Bomb/bomb32.png"),
		pygame.image.load("../images/Bomb/bomb33.png"),
		pygame.image.load("../images/Bomb/bomb34.png"),
		pygame.image.load("../images/Bomb/bomb35.png"),
		pygame.image.load("../images/Bomb/bomb36.png"),
		pygame.image.load("../images/Bomb/bomb37.png"),
		pygame.image.load("../images/Bomb/bomb38.png"),
		pygame.image.load("../images/Bomb/bomb39.png"),
		pygame.image.load("../images/Bomb/bomb40.png")]
		
	def Tir(self, ennemis,window):
		if ((pygame.time.get_ticks() - self.k) > 5000):
			if general.n_bomb >= 0:
				general.n_bomb -= 1
				pygame.time.delay(300)
				for element in self.images:
					pygame.time.delay(20)
					window.blit(element, (0,0))
					pygame.display.flip()
				ennemis.Nettoyage()
			self.k = pygame.time.get_ticks()


