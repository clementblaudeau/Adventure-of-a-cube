# -*- coding: utf-8 -*-
#!/usr/bin/env python
#------------------------------#
#		Sauvegardes.py		   #
#		Clement Blaudeau	   #
#			******			   #
#------------------------------#

import pygame
from pygame.locals import *	
import pickle
import general
import os

class Sauvegarde:
	
	def __init__(self, sav=1):
			self.sav = sav
		#try:
			self.saves = open("save/"+str(self.sav)+"/general.sa", "r")
			self.data_saves = pickle.load(self.saves)
			self.scores = open("save/"+str(self.sav)+"/score.sa", "r")
			self.data_scores = pickle.load(self.scores)
			general.caracters = self.data_saves[0]
		#except:
			general.error = "Save Error"
			#self.Reset()
		#finally:
			self.saves.close()
			self.scores.close()
	
	def Difficulte(self, caracter):
			if self.data_saves[1][int(int(caracter)+1)][3][0] == True:
				return 3
			elif self.data_saves[1][int(int(caracter)+1)][2][0] == True:
				return 2
			else:
				return 1
	
	def NiveauActuel(self, pers):
		return self.data_saves[1][int(pers)][general.diff_level][1]
		
	
	def MeilleurScore(self, numero, score,pers):
		print general.diff_level
		print numero
		print score
		print pers
		if pers == "Cub":
			if self.data_scores[0][1][int(general.diff_level - 1)][int(int(numero)-1)] >= score:
				return "Meilleur score : "+str(self.data_scores[0][1][int(general.diff_level - 1)][int(int(numero)-1)])+"..."
			else:
				self.data_scores[0][1][general.diff_level -1][int(numero) - 1] = score
				self.scores = open("save/"+str(self.sav)+"/score.sa", "w")
				pickle.dump(self.data_scores,self.scores)
				self.scores.close()
				return "Nouveau record !"
		elif pers == "Perl":
			if self.data_scores[1][1][general.diff_level -1][int(numero) - 1] >= score:
				return "Meilleur score : "+str(int(self.data_scores[1][general.diff_level -1][int(numero) - 1]))+"..."
			else:
				self.data_scores[1][1][general.diff_level -1][int(numero) - 1] = score
				self.scores = open("save/"+str(self.sav)+"/score.sa", "w")
				pickle.dump(self.data_scores,self.scores)
				self.scores.close()
				return "Nouveau record !"
		elif pers == "Sneeze":
			if self.data_scores[2][1][general.diff_level -1][int(numero) - 1] >= score:
				return "Meilleur score : "+str(int(self.data_scores[2][general.diff_level -1][int(numero) - 1]))+"..."
			else:
				self.data_scores[2][1][general.diff_level -1][int(numero) - 1] = score
				self.scores = open("save/"+str(self.sav)+"/score.sa", "w")
				pickle.dump(self.data_scores,self.scores)
				self.scores.close()
				return "Nouveau record !"
				
				return
		
	def NouveauNiveau(self,pers):
		if pers == "Cub":
			if self.data_saves[1][1][int(general.diff_level)][1] + 1 > 16:
				self.data_saves[1][1][int(general.diff_level)][1] = 16
				self.data_saves[1][1][int(general.diff_level + 1)][0] = True
				self.data_saves[1][2][int(general.diff_level)][0] = True
			else:
				self.data_saves[1][1][int(general.diff_level)][1] += 1
			self.saves = open("save/"+str(self.sav)+"/general.sa", "w")
			pickle.dump(self.data_saves,self.saves)
			self.saves.close()
		elif pers == "Perl":
			if self.data_saves[1][2][int(general.diff_level)][1] + 1 > 16:
				self.data_saves[1][2][int(general.diff_level)][1] = 16
				self.data_saves[1][2][int(general.diff_level + 1)][0] = True
				self.data_saves[1][3][int(general.diff_level)][0] = True
			else:
				self.data_saves[1][2][int(general.diff_level)][1] += 1
			self.saves = open("save/"+str(self.sav)+"/general.sa", "w")
			pickle.dump(self.data_saves,self.saves)
			self.saves.close()
		elif pers == "Sneeze":
			if self.data_saves[1][1][int(general.diff_level)][1] + 1 > 16:
				self.data_saves[1][1][int(general.diff_level)][1] = 16
				self.data_saves[2][1][1][0] = True
				self.data_saves[2][1][2][0] = True
				self.data_saves[2][1][3][0] = True
				self.data_saves[2][2][1][0] = True
				self.data_saves[2][2][2][0] = True
				self.data_saves[2][2][3][0] = True
				self.data_saves[2][3][1][0] = True
				self.data_saves[2][3][2][0] = True
				self.data_saves[2][3][3][0] = True
			else:
				self.data_saves[1][1][int(general.diff_level)][1] += 1
			self.saves = open("save/"+str(self.sav)+"/general.sa", "w")
			pickle.dump(self.data_saves,self.saves)
			self.saves.close()
	
	def BossRush(self):
		return self.data_saves[2][1][1][0] + self.data_saves[2][1][1][1]
	
	def BossRushes(self):
		return [self.data_saves[2][1][1][0] + self.data_saves[2][1][1][1],self.data_saves[2][2][1][0] + self.data_saves[2][2][1][1],self.data_saves[2][3][1][0] + self.data_saves[2][3][1][1]]
	
	def BossRushesDifficulty(self,pers):
		return self.data_saves[2][pers][1]	
	
	def History(self,pers):
		return [self.data_saves[1][pers][1][0],self.data_saves[1][pers][2][0],self.data_saves[1][pers][3][0]]


	
