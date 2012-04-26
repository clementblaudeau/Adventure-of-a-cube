
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
from boss2 import *
from boss import *
from text import *
import general

class Niveau:
	
	def __init__(self, numero, pers):
		self.nom_fichier = "niveaux/"+pers+"/("+str(general.diff_level)+")/" + numero + ".lvl"
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
		#self.fond = pygame.image.load(self.nom_background).convert()
		self.nom_background = self.nom_background.split("/")
		self.fond = pygame.image.load(self.nom_background[0] + "/" + str(general.screen) + "/" + self.nom_background[1]).convert()
		self.nom_son = self.contenu[2]
		self.son = pygame.mixer.Sound(self.nom_son)
		self.nombre_obstacles = self.contenu[4]
		self.obstacles = Obstacles()
		if int(numero)%2 == 0:
		    self.boss = Boss(numero,pers)
		self.clear = False
		self.chrono = Chrono()
		
		
		
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
		try:
		    self.boss.Tir(self.ennemis, self.obstacles)
		except:
		    pass
		self.ennemis.Deplacements()
		try:
		    self.boss.Affichage(fenetre)
		except:
		    pass
		self.obstacles.Affichage(fenetre)
		self.ennemis.Affichage(fenetre)
		self.chrono.Affichage(pygame.time.get_ticks(), fenetre, "")
		
	def Collisions(self,cub):
	    if general.c_protect == False:
		cub.tir1.positions = self.obstacles.ColisionsTir(cub.tir1.positions, 1+general.niv)
		cub.tir2.positions = self.obstacles.ColisionsTir(cub.tir2.positions, 6+general.niv)
		cub.tir1.positions = self.ennemis.CollisionsTirs(cub.tir1.positions, 1+general.niv)
		cub.tir2.positions = self.ennemis.CollisionsTirs(cub.tir2.positions, 6+general.niv)
		try:
		    self.boss.CollisionTirs(cub.tir1.positions)
		    self.boss.CollisionTirs(cub.tir2.positions)
		    cub.score.score += self.boss.eclats.Absorption(cub)
		except:
		    pass
		cub.score.score += self.obstacles.eclat.Absorption(cub)
		cub.score.score += self.ennemis.eclats.Absorption(cub)
		if (self.ennemis.CollisionCube(cub.hitbox) == True):
		    if cub.degats == 0:
			cub.vie.vie += -1
			cub.degats +=200
			cub.Reboot()
		try:
		    if (self.boss.CollisionCube(cub.hitbox) == True):
			if cub.degats == 0:
			    cub.vie.vie += -1
			    cub.degats +=200
			    cub.Reboot()
		except:
		    pass
		
	def Fini(self):
	    self.ennemis.Cleaner()
	    if (self.ennemis.positions == []) and (self.ennemis.Fini() == True) and (self.ennemis.positionsf == []):
		if self.obstacles.positions == []:
		    if self.obstacles.eclat.positions == [] and self.ennemis.eclats.positions == []:
			try:
			    if self.boss.Fini() == True:
				return True
			except:
			    return True
	    return False
		


