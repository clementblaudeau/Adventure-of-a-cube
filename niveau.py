
#------------------------------#
#			Niveau.py		   #
#		Clement Blaudeau	   #
#			******			   #
#------------------------------#

# -*- coding: utf-8 -*-


import pygame
from pygame.locals import *
from obstacles import * 


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
		
		self.nombre_obstacles = self.contenu[3]
		self.obstacles = Obstacles()
		
		i = 4
		j = 1
		while j <= int(self.nombre_obstacles):
			print self.nombre_obstacles
			print j
			print self.contenu[i]
			print self.contenu[i+1]
			print self.contenu[i+2]
			self.obstacles.NouvelObjet(int(self.contenu[i]),int(self.contenu[i+1]), int(self.contenu[i+2]))
			i += 3
			j += 1
		


