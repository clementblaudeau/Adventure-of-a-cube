# -*- coding: utf-8 -*-

#------------------------------
#	text.py
#	Clement Blaudeau       
#	******	       
#------------------------------
#	Fichier utilisé pour les 
#	affichages de certains textes
#------------------------------


import general
import pygame
from pygame.locals import *

class Textes:
	def __init__(self):
		self.chrono = Chrono()
		self.score = Score()
		self.vie = Vie()
		self.nivtirs = NivTirs()
	
	def Affichage(self, time, fenetre, sorte):
		self.chrono.Affichage(time, fenetre, sorte)
		self.vie.Affichage(fenetre)
		self.chrono.Affichage(fenetre)
		self.nivtirs.Affichage(fenetre)

class Chrono:
	
	def __init__(self):
		self.temps_trop = pygame.time.get_ticks()
		self.chrono_ml = 0
		self.chrono_s = 0
		self.chrono_m = 0
		self.temps = str(self.chrono_m) + ":" + str(self.chrono_s) + ":" + str(self.chrono_ml)
		self.font = pygame.font.Font(None, 36)
		self.text = self.font.render(self.temps, 1, (255, 180, 10))
		self.position = self.text.get_rect()
		self.position = self.position.move(general.w+65, 20)

	def Affichage(self, time, fenetre, sorte):
		self.chrono_ml = time
		self.chrono_s = self.chrono_ml / 1000
		self.chrono_m = self.chrono_s / 60
		self.chrono_s %= 60
		self.chrono_ml %= 1000
		if self.chrono_s < 10:
			self.chrono_s = "0" + str(self.chrono_s)
		self.temps = str(self.chrono_m) + ":" + str(self.chrono_s) + ":" + str(self.chrono_ml)
		self.text = self.font.render(self.temps, 1, (255,180,10))
		if sorte == "boss":
			self.text = self.font.render(self.temps, 1, (255,10,10))
		fenetre.blit(self.text, self.position)
		

class Score:
	
	
	def __init__(self):
		self.font = pygame.font.Font(None, 36)
		self.text = self.font.render("0", 1, (255, 255, 255))
		self.position = self.text.get_rect()
		self.position = self.position.move(general.w+65, 55)
		self.score = 0
		self.r = 0
		self.b = 0
		self.v = 0
		
	def CalculScore(self, vies):
		return (self.score + (vies * 100) - (general.tirs*2))

	def Affichage(self, fenetre):
		
		self.r = self.score/2
		if self.r > 255:
			self.r = 255
			self.b = self.score/4
			if self.b > 255:
				self.b = 255
				self.v = self.score/8
				if self.v > 255:
					self.v = 255
		self.text = self.font.render(str(self.score), 1, (self.r, self.v, self.b))
		fenetre.blit(self.text, self.position)




class Vie:
	
	def __init__(self):
		self.font = pygame.font.Font(None, 36)
		self.text = self.font.render("0", 1, (255, 255, 255))
		self.position = self.text.get_rect()
		self.position = self.position.move(general.w+65, 85)
		self.vie = 5
		self.vies_utilisees = 0
		self.r = 0
		self.b = 0
		self.v = 0

	def Affichage(self, fenetre):
		
		if self.vie == 5:
			self.v = 255
		if self.vie == 4:
			self.v = 250
			self.r = 250
		if self.vie == 3:
			self.v = 200
			self.r = 255
		if self.vie == 2:
			self.r = 255
			self.v = 155
		if self.vie == 1:
			self.r = 255
			self.v = 50
		if self.vie == 0:
			self.r = 255
			self.v = 0
		self.text = self.font.render(str(self.vie), 1, (self.r, self.v, self.b))
		fenetre.blit(self.text, self.position)


class NivTirs:
	
	def __init__(self):
		self.font = pygame.font.Font("polices/Bank.ttf", 20)
		self.text = self.font.render("", 1, (0,0,0))
		self.position = self.text.get_rect()
		self.position = self.position.move(general.w+70, 200)

	def Affichage(self, fenetre):
		chaine = ""
		i = 0
		if (general.ennemis/15 == 1):
			general.niv = 1
			i = 15
		if (general.ennemis/15 == 2):
			general.niv = 2
			i = 30
		while i < general.ennemis:
			chaine += "|"
			i += 1
		if i >= 30:
			chaine = "***"
		
		self.text = self.font.render(chaine, 1, (0, 0, 0))
		fenetre.blit(self.text, self.position)
		self.text = self.font.render(str("Tirs : "+str(general.tirs)), 1, (0, 0, 0))
		fenetre.blit(self.text, self.position.move(0,50))

		self.text = self.font.render(str("Bombes : "+str(general.n_bomb + 1)), 1, (0, 0, 0))
		fenetre.blit(self.text, self.position.move(0,80))



class ModeLent:
	
	def __init__(self):
		self.font = pygame.font.Font("polices/Bank.ttf", 20)
		self.text = self.font.render("Mode Lent", 1, (1,1,0))
		
		
	def Affichage(self,fenetre):
		fenetre.blit(self.text, (general.w+50,general.h-100))
		
	
	
	
	
	
	

