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
		try:
			self.fichier = open('sauvegardes/campagne.sa', "r")
			self.persos = int(self.fichier.read())
			if self.persos >= 2:
				general.caracters.append("Perl")
			if self.persos >= 3:
				general.caracters.append("Sneeze")
		except:
			self.fichier = open('sauvegardes/campagnes.sa', 'w')
			self.fichier.write("1")
		finally:
			self.fichier.close()
	
	def Difficulte(self, caracter):
		try:
			self.fichier = open('sauvegardes/'+str(general.caracters[caracter])+'/campagne.sa', 'r')
			self.contenu = self.fichier.read()
			self.fichier.close()
			return int(self.contenu)
		except:
			self.fichier = open('sauvegardes/'+str(general.caracters[caracter])+'/campagne.sa', 'w')
			self.fichier.write("1")
			self.fichier.close()
			return 1
	
	def NiveauActuel(self, pers):
		self.fichier = open('sauvegardes/'+pers+'/('+str(general.diff_level)+')/campagne.sa', "r")
		self.niveau = self.fichier.read()
		return self.niveau
	
	def MeilleurScore(self, numero, score,pers):
		try :
			self.fichier2 = open('sauvegardes/'+pers+'/('+str(general.diff_level)+')/'+str(numero)+'.sa', 'r')
		except:
			try:
				self.fichier2 = open('sauvegardes/'+pers+'/('+str(general.diff_level)+')/'+str(numero)+'.sa', 'w')
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
			self.fichier2 = open('sauvegardes/'+pers+'/('+str(general.diff_level)+')/'+str(numero)+'.sa','w')
			self.fichier2.write(str(score))
			self.fichier2.close()
			return "Nouveau record !"
		
	def NouveauNiveau(self):
		self.fichier = open('sauvegardes/'+pers+'/('+str(general.diff_level)+')/campagne.sa', "w")
		self.fichier.write(str(int(self.niveau) + 1))
		self.niveau = str(int(self.niveau) + 1)
		self.fichier.close()


