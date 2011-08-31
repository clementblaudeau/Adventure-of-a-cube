
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
		self.ennemis = Ennemis()
		
		self.ennemis.NouvelEnnemi(1,200,-150)
		self.ennemis.NouvelEnnemi(1,400,-150)
		self.ennemis.NouvelEnnemi(1,600,-150)
		self.ennemis.NouvelEnnemi(1,30,-150)
		
		self.ennemis.NouvelEnnemi(1,100,-250)
		self.ennemis.NouvelEnnemi(1,300,-250)
		self.ennemis.NouvelEnnemi(1,500,-250)
		
		self.ennemis.NouvelEnnemi(1,100,-350)
		self.ennemis.NouvelEnnemi(1,300,-350)
		self.ennemis.NouvelEnnemi(1,500,-350)
		self.ennemis.NouvelEnnemi(1,30,-350)
		
		self.ennemis.NouvelEnnemi(1,200,-450)
		self.ennemis.NouvelEnnemi(1,400,-450)
		self.ennemis.NouvelEnnemi(1,600,-450)
		self.ennemis.NouvelEnnemi(1,30,-450)
		
		self.ennemis.NouvelEnnemi(1,100,-750)
		self.ennemis.NouvelEnnemi(1,300,-750)
		self.ennemis.NouvelEnnemi(1,500,-750)
		
		self.ennemis.NouvelEnnemi(1,200,-850)
		self.ennemis.NouvelEnnemi(1,400,-850)
		self.ennemis.NouvelEnnemi(1,600,-850)
		self.ennemis.NouvelEnnemi(1,30,-850)
		
		self.ennemis.NouvelEnnemi(1,100,-950)
		self.ennemis.NouvelEnnemi(1,300,-950)
		self.ennemis.NouvelEnnemi(1,500,-950)
		
		self.ennemis.NouvelEnnemi(1,30,-1150)
		self.ennemis.NouvelEnnemi(1,200,-1150)
		self.ennemis.NouvelEnnemi(1,400,-1150)
		self.ennemis.NouvelEnnemi(1,600,-1150)
		
		
		
		
		


