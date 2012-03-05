# -*- coding: utf-8 -*-

#------------------------------#
# 	    	Boutons.py	       #
#		Clement Blaudeau	   #
#			******			   #
#------------------------------#


import pygame
from pygame.locals import *


class Bouton_Text:
	
	def __init__(self):
		self.off = pygame.image.load("images/bouton_l.png").convert_alpha()
		self.hover = pygame.image.load("images/bouton-hover_l.png").convert_alpha()
		self.on = pygame.image.load("images/bouton-on_l.png").convert_alpha()
		self.positions = []
		self.numeros = []
		self.noms = []
		self.num = []
		self.font = pygame.font.Font("polices/Coalition.ttf", 20)
		
	
	def NouveauBouton(self, position, nom, taille=20):
		self.font = pygame.font.Font("polices/Coalition.ttf", taille)
		temp = self.off.get_rect()
		self.positions.append(temp.move(position))
		self.noms.append(self.font.render(str(nom), 1, (0, 0, 0)))
	
	def Affichage(self,fenetre, souris, clic):
		i = 0
		for element in self.positions:
			fenetre.blit(self.off,element)
		for element in self.positions:
			fenetre.blit(self.noms[i], (element.centerx - 85, element.centery-10))
			if souris[0] > element.left and souris[0] < element.right:
				if souris[1] > element.top and souris[1] < element.bottom:
					if clic == 1:
						fenetre.blit(self.on, element)
						j = 0
						for element in self.positions:
							fenetre.blit(self.noms[j], (element.centerx - 85, element.centery-10))
							j += 1
						return i+1
					else:
						fenetre.blit(self.hover, element)
						fenetre.blit(self.noms[i], (element.centerx - 85, element.centery-10))
			i +=1
			
			
	def Netoyage(self):
		self.positions = []
		self.numeros = []
		self.num = []
		
		
		
class Bouton_Nb:
	
	def __init__(self):
		self.off = pygame.image.load("images/bouton.png").convert_alpha()
		self.hover = pygame.image.load("images/bouton-hover.png").convert_alpha()
		self.on = pygame.image.load("images/bouton-on.png").convert_alpha()
		self.positions = []
		self.numeros = []
		self.num = []
		self.font = pygame.font.Font("polices/Coalition.ttf", 32)
		
	
	def NouveauBouton(self, position, numero):
		temp = self.off.get_rect()
		self.positions.append(temp.move(position))
		self.numeros.append(self.font.render(str(numero), 1, (0, 0, 0)))
		self.num.append(numero)
	
	def Affichage(self,fenetre, souris, clic):
		i = 0
		for element in self.positions:
			fenetre.blit(self.off,element)
		for element in self.positions:
			fenetre.blit(self.numeros[i], (element.centerx - 15, element.centery-10))
			if souris[0] > element.left and souris[0] < element.right:
				if souris[1] > element.top and souris[1] < element.bottom:
					if clic == 1:
						fenetre.blit(self.on, element)
						j = 0
						for element in self.positions:
							fenetre.blit(self.numeros[j], (element.centerx - 15, element.centery-10))
							j += 1
						return int(self.num[i])
					else:
						fenetre.blit(self.hover, element)
						fenetre.blit(self.numeros[i], (element.centerx - 15, element.centery-10))
			i +=1
	def Netoyage(self):
		self.positions = []
		self.numeros = []
		self.num = []
