#------------------------------#
#	       Chrono.py           #
#   	Clement Blaudeau       #
#            ******	           #
#------------------------------#


import pygame
from pygame.locals import *

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
		self.position = self.position.move(560, 15)




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
		self.position = self.position.move(560, 45)
		self.score = 0
		self.r = 0
		self.b = 0
		self.v = 0

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

