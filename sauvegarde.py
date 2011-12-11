#!/usr/bin/env python
#------------------------------#
#		Sauvegardes.py		   #
#		Clement Blaudeau	   #
#			******			   #
#------------------------------#

# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *	

import general

class Sauvegarde:
	
	def __init__(self):
		self.fichier = open('sauvegardes/1.sa', "r")
		self.niveau = self.fichier.read()
		
	def NiveauActuel(self):
		return self.niveau
		
	def NouveauNiveau(self):
		self.fichier = open('sauvegardes/1.sa', "w")
		self.fichier.write(str(int(self.niveau) + 1))
		self.niveau = str(int(self.niveau) + 1)
		self.fichier.close()


