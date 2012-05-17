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
# 	boutons.py	       
#	Clement Blaudeau       
#	******	       
#------------------------------
#	Fichier chargé des boutons
#	ou interupteurs des menus
#------------------------------

import pygame
from pygame.locals import *


class Bouton_Text:
	
	def __init__(self):
		self.off = pygame.image.load("../images/bouton_l.png").convert_alpha()
		self.hover = pygame.image.load("../images/bouton-hover_l.png").convert_alpha()
		self.on = pygame.image.load("../images/bouton-on_l.png").convert_alpha()
		self.lock = pygame.image.load("../images/bouton_lock.png").convert_alpha()
		self.boutons = []
		self.font = pygame.font.Font("../polices/Coalition.ttf", 20)
		
	
	def NouveauBouton(self, position, nom, taille=20, unlock=True):
		self.font = pygame.font.Font("../polices/Coalition.ttf", taille)
		temp = self.off.get_rect()
		self.boutons.append([temp.move(position),self.font.render(str(nom), 1, (0, 0, 0)),unlock])

	
	def Affichage(self,window, souris, clic):
		i = 0
		for element in self.boutons:
			window.blit(self.off,element[0])
			if element[2] == False:
				window.blit(self.lock,element[0])
				window.blit(element[1], (element[0].centerx - 85, element[0].centery-10))
			else:
				window.blit(element[1], (element[0].centerx - 85, element[0].centery-10))
		for element in self.boutons:
			window.blit(self.off,element[0])
			if element[2] == False:
				window.blit(self.lock,element[0])
				window.blit(element[1], (element[0].centerx - 85, element[0].centery-10))
			else:
				window.blit(element[1], (element[0].centerx - 85, element[0].centery-10))
				if souris[0] > element[0].left and souris[0] < element[0].right:
					if souris[1] > element[0].top and souris[1] < element[0].bottom:
						if clic == 1:
							window.blit(self.on, element[0])
							window.blit(element[1], (element[0].centerx - 85, element[0].centery-10))
							
							return i+1
						else:
							window.blit(self.hover, element[0])
							window.blit(element[1], (element[0].centerx - 85, element[0].centery-10))
				
			i +=1
			
			
	def Netoyage(self):
		self.positions = []
		self.numeros = []
		self.num = []
		self.boutons = []
		
		
		
class Bouton_Nb:
	
	def __init__(self):
		self.off = pygame.image.load("../images/bouton.png").convert_alpha()
		self.hover = pygame.image.load("../images/bouton-hover.png").convert_alpha()
		self.on = pygame.image.load("../images/bouton-on.png").convert_alpha()
		self.positions = []
		self.numeros = []
		self.num = []
		self.font = pygame.font.Font("../polices/Coalition.ttf", 32)
		
	
	def NouveauBouton(self, position, numero):
		temp = self.off.get_rect()
		self.positions.append(temp.move(position))
		self.numeros.append(self.font.render(str(numero), 1, (0, 0, 0)))
		self.num.append(numero)
	
	def Affichage(self,window, souris, clic):
		i = 0
		for element in self.positions:
			window.blit(self.off,element)
		for element in self.positions:
			window.blit(self.numeros[i], (element.centerx - 15, element.centery-10))
			if souris[0] > element.left and souris[0] < element.right:
				if souris[1] > element.top and souris[1] < element.bottom:
					if clic == 1:
						window.blit(self.on, element)
						j = 0
						for element in self.positions:
							window.blit(self.numeros[j], (element.centerx - 15, element.centery-10))
							j += 1
						return int(self.num[i])
					else:
						window.blit(self.hover, element)
						window.blit(self.numeros[i], (element.centerx - 15, element.centery-10))
			i +=1
	def Netoyage(self):
		self.positions = []
		self.numeros = []
		self.num = []
