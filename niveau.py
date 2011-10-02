
#------------------------------#
#			Niveau.py		   #
#		Clement Blaudeau	   #
#			******			   #
#------------------------------#

# -*- coding: utf-8 -*-


import pygame
from pygame.locals import *
from obstacles import * 
from ennemis import *

class Niveau:
	
	def __init__(self, numero):
		self.nom_fichier = "niveaux/" + numero + ".lvl"
		self.fichier = open(self.nom_fichier, "r")
		self.contenu = self.fichier.readlines()
		b = 0
		c = 0
		for element in self.contenu:
			for lettres in element:
				c += 1
			self.contenu[b]= element[0:c-1]
			c = 0
			b += 1
		
		self.nom = self.contenu[0]
		self.nom_background = self.contenu[1]
		self.fond = pygame.image.load(self.nom_background).convert()
		self.nom_son = self.contenu[2]
		self.son = pygame.mixer.Sound(self.nom_son)
		self.nombre_obstacles = self.contenu[3]
		self.obstacles = Obstacles()
		self.ennemis = Ennemis()
		
		
		i = 4
		j = 1
		while j <= int(self.nombre_obstacles):
			self.obstacles.NouvelObjet(int(self.contenu[i]),int(self.contenu[i+1]), int(self.contenu[i+2]))
			i += 3
			j += 1
		
		j = 1
		self.nombre_ennemis = self.contenu[i]
		i += 1
		while j <= int(self.nombre_ennemis):
			self.ennemis.NouvelEnnemi(int(self.contenu[i]),int(self.contenu[i+1]), int(self.contenu[i+2]))
			print self.contenu[i]
			print self.contenu[i+1]
			print self.contenu[i+2]
			i += 3
			j += 1
			
		
	def Affichage(self, fenetre):
		self.ennemis.Tir()
		self.ennemis.Deplacements()
		self.obstacles.Affichage(fenetre)
		self.ennemis.Affichage(fenetre)
		
		


