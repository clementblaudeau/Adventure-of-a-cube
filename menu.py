
# -*- coding: utf-8 -*-
#------------------------------#
#			Menu.py			   #
#		Clement Blaudeau	   #
#			******			   #
#------------------------------#


import pygame
from pygame.locals import *
import general
from cub import *


class Menu:
	
	def __init__(self):
		self.fond = pygame.image.load("images/menu.png").convert_alpha()
		self.gagne = pygame.image.load("images/fin_niveau.png").convert()
		self.chargement = pygame.image.load("images/chargement.png").convert()
		self.boutons = Bouton()
		self.lastclic = 0
		self.lastevent = 0
		self.ok = 0
		self.lastpos = (0,0)
		self.font = pygame.font.Font("polices/Coalition.ttf", 17)
		self.x = 30
		self.y = 150
		self.vrai = False
		self.cube = Cub()
		self.cube.position = self.cube.position.move(100,100)
		#self.boutons.NouveauBouton((30,160), 1)
		#self.boutons.NouveauBouton((30,210), 2)
		
	def MenuAffichage(self,fenetre,nb):
		self.boutons.Netoyage()
		self.x = 30
		self.y = 150
		self.nb = "0"
		nb = int(nb)
		while nb > 0:
			if self.y >= 460:
				self.y = 150
				self.x += 100
			self.nb = str(int(self.nb)+1)
			self.boutons.NouveauBouton((self.x,self.y), self.nb)
			self.y += 50
			nb -= 1
		fenetre.blit(self.fond,(0,0))
		continuer = 1
		self.boutons.Affichage(fenetre, (0,0), 0)
		self.ok = 0
		while continuer:
			fenetre.blit(self.fond,(0,0))
			self.cube.Rotation()
			if self.cube.ve == 0:
				self.cube.position = self.cube.position.move(0,-2)
				if self.cube.position.y <= 0:
					self.cube.ve = 1
			elif self.cube.ve == 1:
				self.cube.position = self.cube.position.move(0,2)
				if self.cube.position.y + 60 >= general.h:
					self.cube.ve = 0
					
			if self.cube.ho == 0:
				self.cube.position = self.cube.position.move(-2,0)
				if self.cube.position.x <= 0:
					self.cube.ho = 1
			elif self.cube.ho == 1:
				self.cube.position = self.cube.position.move(2,0)
				if self.cube.position.x + 60 >= general.w:
					self.cube.ho = 0
			
			self.cube.Affichage2(fenetre)
			
			for event in pygame.event.get():
				if event.type == QUIT:
					return 0
				if event.type == MOUSEMOTION:
					self.lastevent = event.dict["buttons"][0]
					self.lastpos = event.dict["pos"]
				if event.type == MOUSEBUTTONDOWN:
					self.lastevent = 1
				if event.type == MOUSEBUTTONUP:
					self.lastevent = 0
					if self.ok >= 1:
						return self.ok				
			if self.lastevent == 1:
				self.ok = self.boutons.Affichage(fenetre, self.lastpos, 1)
			else:
				self.boutons.Affichage(fenetre, self.lastpos, 0)
			
			pygame.display.flip()
				
				
				

	def FinNiveau(self, score, vies, fenetre, meilleurScore):
		
		
		if vies > -1:
			image = self.gagne
			vrai = True
			self.vrai = True
		else:
			image = pygame.image.load("images/game_over.png").convert()
			vrai = False
			self.vrai = False
		fenetre.blit(image,(0,0))
		if vrai:
			self.font = pygame.font.Font("polices/Coalition.ttf", 17)
			fenetre.blit(image,(0,0))
			pygame.time.delay(500)
			fenetre.blit(self.font.render(" Score : " + str(score), 1, (255, 255, 0)), (80, 320))
			pygame.display.flip()
			pygame.time.delay(700)
			fenetre.blit(image,(0,0))
			fenetre.blit(self.font.render(" Score : " + str(score), 1, (255, 255, 0)), (80, 320))
			fenetre.blit(self.font.render(" + Vies Restantes : " + str(vies), 1, (255, 255, 0)), (80, 340))
			
			pygame.display.flip()
			
			pygame.time.delay(700)
			fenetre.blit(image,(0,0))
			fenetre.blit(self.font.render(" Score : " + str(score), 1, (255, 255, 0)), (80, 320))
			fenetre.blit(self.font.render(" + Vies Restantes : " + str(vies) + " x 100 : " + str(vies * 100), 1, (255, 255, 0)), (80, 340))
			pygame.display.flip()
			pygame.display.flip()
			
			pygame.time.delay(700)
			fenetre.blit(image,(0,0))
			fenetre.blit(self.font.render(" Score : " + str(score), 1, (255, 255, 0)), (80, 320))
			fenetre.blit(self.font.render(" + Vies Restantes : " + str(vies) + " x 100 : " + str(vies * 100), 1, (255, 255, 0)), (80, 340))
			fenetre.blit(self.font.render(" - Tirs : " + str(general.tirs), 1, (255, 0, 0)), (80, 360))
			pygame.display.flip()
			
			pygame.time.delay(700)
			fenetre.blit(image,(0,0))
			fenetre.blit(self.font.render(" Score : " + str(score), 1, (255, 255, 0)), (80, 320))
			fenetre.blit(self.font.render(" + Vies Restantes : " + str(vies) + " x 100 : " + str(vies * 100), 1, (255, 255, 0)), (80, 340))
			fenetre.blit(self.font.render(" - Tirs : " + str(general.tirs) +" x 2 : " + str(general.tirs*2), 1, (255, 0, 0)), (80, 360))
			pygame.display.flip()
			
			pygame.time.delay(700)
			fenetre.blit(image,(0,0))
			fenetre.blit(self.font.render(" Score : " + str(score), 1, (255, 255, 0)), (80, 320))
			fenetre.blit(self.font.render(" + Vies Restantes : " + str(vies) + " x 100 : " + str(vies * 100), 1, (255, 255, 0)), (80, 340))
			fenetre.blit(self.font.render(" - Tirs : " + str(general.tirs) +" x 2 : " + str(general.tirs*2), 1, (255, 0, 0)), (80, 360))
			fenetre.blit(self.font.render("---------", 1, (255, 255, 0)), (130, 380))
			pygame.display.flip()
			
			pygame.time.delay(700)
			fenetre.blit(image,(0,0))
			fenetre.blit(self.font.render(" Score : " + str(score), 1, (255, 255, 0)), (80, 320))
			fenetre.blit(self.font.render(" + Vies Restantes : " + str(vies) + " x 100 : " + str(vies * 100), 1, (255, 255, 0)), (80, 340))
			fenetre.blit(self.font.render(" - Tirs : " + str(general.tirs) +" x 2 : " + str(general.tirs*2), 1, (255, 0, 0)), (80, 360))
			fenetre.blit(self.font.render("---------", 1, (255, 255, 0)), (130, 380))
			fenetre.blit(self.font.render(" Total : " +  str((vies * 100 + score)- (2*general.tirs)), 1, (255, 185, 0)), (80, 400))
			pygame.display.flip()
			
			
			pygame.time.delay(700)
			fenetre.blit(image,(0,0))
			fenetre.blit(self.font.render(" Score : " + str(score), 1, (255, 255, 0)), (80, 320))
			fenetre.blit(self.font.render(" + Vies Restantes : " + str(vies) + " x 100 : " + str(vies * 100), 1, (255, 255, 0)), (80, 340))
			fenetre.blit(self.font.render(" - Tirs : " + str(general.tirs) +" x 2 : " + str(general.tirs*2), 1, (255, 0, 0)), (80, 360))
			fenetre.blit(self.font.render("---------", 1, (255, 255, 0)), (130, 380))
			fenetre.blit(self.font.render(" Total : " +  str((vies * 100 + score)- (2*general.tirs)), 1, (255, 185, 0)), (80, 400))
			fenetre.blit(self.font.render(str(meilleurScore), 1, (255, 185, 0)), (250, 50))
			pygame.display.flip()
			
			pygame.time.delay(700)
			
			
		
		continuer = 1
		pygame.event.clear()
		while continuer:
			pygame.time.delay(1)
			fenetre.blit(image,(0,0))
			if vrai:
				fenetre.blit(self.font.render(" Score : " + str(score), 1, (255, 255, 0)), (80, 320))
				fenetre.blit(self.font.render(" + Vies Restantes : " + str(vies) + " x 100 : " + str(vies * 100), 1, (255, 255, 0)), (80, 340))
				fenetre.blit(self.font.render(" - Tirs : " + str(general.tirs) +" x 2 : " + str(general.tirs*2), 1, (255, 0, 0)), (80, 360))
				fenetre.blit(self.font.render("---------", 1, (255, 255, 0)), (130, 380))
				fenetre.blit(self.font.render(" Total : " +  str((vies * 100 + score)- (2*general.tirs)), 1, (255, 185, 0)), (80, 400))
				fenetre.blit(self.font.render(str(meilleurScore), 1, (255, 185, 0)), (250, 50))
			pygame.display.flip()
			
			for event in pygame.event.get():
				if event.type == QUIT:
					continuer = 0
				if event.type == KEYDOWN:
							continuer = 0
							
	def Pause(self,fenetre):
		fenetre.blit(pygame.image.load("images/pause.png").convert_alpha(),(0,0));
		pygame.display.flip()
		pygame.time.delay(100)
		continuer = 1
		pygame.event.clear()
		while continuer == 1:
			for event in pygame.event.get():	#Attente des événements
				#print event
				if event.type == KEYDOWN:
					if event.key == 27:
						continuer = 0
						pygame.event.clear()
				elif event.type == QUIT:
					continuer = 0
					pygame.event.clear()
					break
		
		fenetre.blit(self.font.render("3", 1, (255, 255, 0)), ((general.w/2)-50, 320))
		pygame.display.flip()
		pygame.time.delay(700)
		
		fenetre.blit(self.font.render("3", 1, (255, 255, 0)), ((general.w/2)-50, 320))
		fenetre.blit(self.font.render("2", 1, (255, 255, 0)), ((general.w/2), 320))
		pygame.display.flip()
		pygame.time.delay(700)
		
		
		fenetre.blit(self.font.render("3", 1, (255, 255, 0)), ((general.w/2)-50, 320))
		fenetre.blit(self.font.render("2", 1, (255, 255, 0)), ((general.w/2), 320))
		fenetre.blit(self.font.render("1", 1, (255, 255, 0)), ((general.w/2)+50, 320))
		pygame.display.flip()
		pygame.time.delay(700)
		
		
	def Chargement(self, fenetre):
			fenetre.blit(self.chargement,(0,0))
			pygame.display.flip()
			
	def CommencementNiveau(self, fenetre):
		fenetre.blit(self.font.render("3", 1, (255, 255, 0)), ((general.w/2)-50, 320))
		pygame.display.flip()
		pygame.time.delay(700)
		
		fenetre.blit(self.font.render("3", 1, (255, 255, 0)), ((general.w/2)-50, 320))
		fenetre.blit(self.font.render("2", 1, (255, 255, 0)), ((general.w/2), 320))
		pygame.display.flip()
		pygame.time.delay(700)
		
		
		fenetre.blit(self.font.render("3", 1, (255, 255, 0)), ((general.w/2)-50, 320))
		fenetre.blit(self.font.render("2", 1, (255, 255, 0)), ((general.w/2), 320))
		fenetre.blit(self.font.render("1", 1, (255, 255, 0)), ((general.w/2)+50, 320))
		pygame.display.flip()
		pygame.time.delay(700)
		
	    

#class DebutNiveau:
	#Cinematique
		



class Bouton:
	
	def __init__(self):
		self.off = pygame.image.load("images/bouton.png").convert_alpha()
		self.hover = pygame.image.load("images/bouton-hover.png").convert_alpha()
		self.on = pygame.image.load("images/bouton-on.png").convert_alpha()
		self.positions = []
		self.numeros = []
		self.num = []
		self.font = pygame.font.Font("polices/Coalition.ttf", 32)
		
	
	def NouveauBouton(self, position, numero):
		temp = self.off.get_rect()
		self.positions.append(temp.move(position))
		self.numeros.append(self.font.render(str(numero), 1, (0, 0, 0)))
		self.num.append(numero)
	
	def Affichage(self,fenetre, souris, clic):
		i = 0
		for element in self.positions:
			fenetre.blit(self.off,element)
		for element in self.positions:
			fenetre.blit(self.numeros[i], (element.centerx - 15, element.centery-10))
			if souris[0] > element.left and souris[0] < element.right:
				if souris[1] > element.top and souris[1] < element.bottom:
					if clic == 1:
						fenetre.blit(self.on, element)
						fenetre.blit(self.numeros[i], (element.centerx - 15, element.centery-10))
						
						return int(self.num[i])
					else:
						fenetre.blit(self.hover, element)
						fenetre.blit(self.numeros[i], (element.centerx - 15, element.centery-10))
			i +=1
	def Netoyage(self):
		self.positions = []
		self.numeros = []
		self.num = []
			


