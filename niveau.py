
#------------------------------#
#	Niveau.py	       #
#	Clement Blaudeau       #
#	******		       #
#------------------------------#

# -*- coding: utf-8 -*-


import pygame
from pygame.locals import *
from obstacles import * 
from ennemis import *
from boss import *
import general

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
		self.nombre_obstacles = self.contenu[4]
		self.obstacles = Obstacles()
		self.boss = Boss(numero)
		self.clear = False
		
		
		
		i = 5
		j = 1
		while j <= int(self.nombre_obstacles):
		    try:
			self.obstacles.NouvelObjet(int(self.contenu[i]),int(self.contenu[i+1]), int(self.contenu[i+2]))
		    except:
			pass
		    finally:
			i += 3
			j += 1
		
		j = 1
		i += 1
		self.style = self.contenu[i]
		i += 1
		self.ennemis = Ennemis(self.style)
		self.nombre_ennemis = self.contenu[i]
		i += 1
		while j <= int(self.nombre_ennemis):
			self.ennemis.NouvelEnnemi(int(self.contenu[int(i)]),int(self.contenu[int(i)+1]), int(self.contenu[int(i)+2]))
			i += 3
			j += 1
		i += 2
		j=1
		try :	    
		    self.nombre_ennemisf = self.contenu[i]
		    while j <= int(self.nombre_ennemisf):
			    self.ennemis.NouvelEnnemiFixe(int(self.contenu[int(i)]),int(self.contenu[int(i)+1]), int(self.contenu[int(i)+2]))
			    i += 3
			    j += 1
		except:
		    pass
			
		
	def Affichage(self, fenetre, scrool):
		fenetre.blit(self.fond, scrool)
		self.ennemis.Tir()
		self.boss.Tir(self.ennemis, self.obstacles)
		self.ennemis.Deplacements()
		self.boss.Affichage(fenetre)
		self.obstacles.Affichage(fenetre)
		self.ennemis.Affichage(fenetre)
		
		
	def Fini(self):
		if self.ennemis.positions == []:
			if self.obstacles.positions == []:
				if self.obstacles.eclat.positions == []:
					if self.ennemis.eclats.positions == []:
						if self.ennemis.positionsf == []:
						    if self.boss.Fini() == True:
								return True
		return False
		


