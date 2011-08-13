import pygame
from pygame.locals import *


class Cube:
	
	
	def __init__(self):
		self.image = pygame.image.load("images/cub001.png").convert_alpha()
		self.position = self.image.get_rect()
		self.i = 1
		self.cube_actuel = "images/cub002.png"
		self.nbattaque = 0
		
		
	def rotation(self):
		if self.i < 10:
			self.cube_actuel = "images/cub00"+ str(self.i) +".png"
			self.i +=1
		elif self.i < 100:
			self.cube_actuel = "images/cub0"+ str(self.i) +".png"
			self.i +=1
		elif self.i < 200:
			self.cube_actuel = "images/cub"+ str(self.i) +".png"
			self.i +=1
		elif self.i == 200:
			self.cube_actuel = "images/cub"+ str(self.i) +".png"
			self.i = 1
		self.image = pygame.image.load(self.cube_actuel).convert_alpha()
		
	


		







