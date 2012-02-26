# -*- coding: utf-8 -*-
#!/usr/bin/env python
#------------------------------#
#		Sauvegardes.py		   #
#		Clement Blaudeau	   #
#			******			   #
#------------------------------#

import pygame
from pygame.locals import *	

import general

class Sauvegarde:
	
	def __init__(self):
		self.fichier = open('sauvegardes/('+str(general.diff_level)+')/campagne.sa', "r")
		self.niveau = self.fichier.read()
		
	def NiveauActuel(self):
		self.fichier = open('sauvegardes/('+str(general.diff_level)+')/campagne.sa', "r")
		self.niveau = self.fichier.read()
		return self.niveau
	
	def MeilleurScore(self, numero, score):
		try :
			self.fichier2 = open('sauvegardes/('+str(general.diff_level)+')/'+str(numero)+'.sa', 'r')
		except:
			try:
				self.fichier2 = open('sauvegardes/('+str(general.diff_level)+')/'+str(numero)+'.sa', 'w')
				self.fichier2.write(str(score))
				self.fichier2.close()	
				return "Nouveau record !"
			except:
				return "Erreur de Sauvegarde !"
		
		self.score = self.fichier2.read()
		if int(self.score) >= int(score):
			return "Meilleur score : "+str(int(self.score))+" ..."
		else:
			self.fichier2.close()
			self.fichier2 = open('sauvegardes/('+str(general.diff_level)+')/'+str(numero)+'.sa','w')
			self.fichier2.write(str(score))
			self.fichier2.close()
			return "Nouveau record !"
		
	def NouveauNiveau(self):
		self.fichier = open('sauvegardes/('+str(general.diff_level)+')/campagne.sa', "w")
		self.fichier.write(str(int(self.niveau) + 1))
		self.niveau = str(int(self.niveau) + 1)
		self.fichier.close()


