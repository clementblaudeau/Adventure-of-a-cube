
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
from boutons import *


class Menu:
	
	def __init__(self):
		self.fond = pygame.image.load("images/"+general.screen+"/menu.png").convert_alpha()
		self.gagne = pygame.image.load("images/"+general.screen+"/fin_niveau.png").convert()
		self.chargement = pygame.image.load("images/"+general.screen+"/chargement.png").convert()
		self.boutons = Bouton_Nb()
		self.boutons2 = Bouton_Text()
		self.lastclic = 0
		self.lastevent = 0
		self.ok = 0
		self.lastpos = (0,0)
		self.font = pygame.font.Font("polices/Coalition.ttf", 17)
		self.x = 30
		self.y = 150
		self.vrai = False
		self.cube = Cub()
		self.progression = 0
		self.cube.position = self.cube.position.move(100,100)
		#self.boutons.NouveauBouton((30,160), 1)
		#self.boutons.NouveauBouton((30,210), 2)
		
	def MenuAffichage(self,fenetre,nb):
		self.boutons.Netoyage()
		self.titre = (self.font.render(str("Choix du level"), 1, (0, 0, 0)))
		self.x = 30
		self.y = 150
		self.nb = "0"
		nb = int(nb)
		while nb > 0:
			if self.y >= 440:
				self.y = 150
				self.x += 200
			self.nb = str(int(self.nb)+1)
			self.boutons.NouveauBouton((self.x,self.y), self.nb)
			self.y += 50
			nb -= 1
		
		self.boutons2.NouveauBouton((general.w/2 + 100,370), "< Retour")
		fenetre.blit(self.fond,(0,0))
		continuer = 1
		self.boutons.Affichage(fenetre, (0,0), 0)
		self.boutons2.Affichage(fenetre, (0,0), 0)
		self.ok = 0
		self.ok2 = 0
		while continuer:
			fenetre.blit(self.fond,(0,0))
			self.cube.Rotation()
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
					if self.ok2 >= 1:
						general.back = False
						return 0				
			if self.lastevent == 1:
				self.ok = self.boutons.Affichage(fenetre, self.lastpos, 1)
				self.ok2 = self.boutons2.Affichage(fenetre, self.lastpos, 1)
			else:
				self.boutons.Affichage(fenetre, self.lastpos, 0)
				self.boutons2.Affichage(fenetre, self.lastpos, 0)
			
			pygame.display.flip()
				
	def DebutNiveau(self, fenetre,lvl):
		try:
			movie = pygame.movie.Movie ('videos/'+str(lvl)+'.mpg')
		except:
			movie = pygame.movie.Movie ('videos/intro.mpg')
		movie_resolution = movie.get_size ()
		#pygame.display.set_mode (movie_resolution)
		movie.set_display(pygame.display.get_surface())
		movie.play ()
		while movie.get_busy ():
			pygame.time.wait (200)
			for event in pygame.event.get():	#Attente des événements
				#print event
				if event.type == KEYDOWN:
					return 0
		#fenetre = pygame.display.set_mode((general.w+200, general.h), DOUBLEBUF)
				

	def FinNiveau(self, score, vies, fenetre, meilleurScore):
		
		
		if vies > -1:
			image = self.gagne
			vrai = True
			self.vrai = True
		else:
			image = pygame.image.load("images/"+general.screen+"/game_over.png").convert()
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
			fenetre.blit(self.font.render(" + Vies Restantes : " + str(vies), 1, (255, 255, 0)), (80, 340))
			pygame.display.flip()
			pygame.time.delay(700)
			fenetre.blit(self.font.render(" + Vies Restantes : " + str(vies) + " x 100 : " + str(vies * 100), 1, (255, 255, 0)), (80, 340))
			fenetre.blit(self.font.render(" - Tirs : " + str(general.tirs), 1, (255, 0, 0)), (80, 360))
			pygame.display.flip()
			pygame.time.delay(700)
			fenetre.blit(self.font.render(" - Tirs : " + str(general.tirs) +" x 2 : " + str(general.tirs*2), 1, (255, 0, 0)), (80, 360))
			pygame.display.flip()
			pygame.time.delay(700)
			fenetre.blit(self.font.render("---------", 1, (255, 255, 0)), (130, 380))
			pygame.display.flip()
			pygame.time.delay(700)
			fenetre.blit(self.font.render(" Total : " +  str((vies * 100 + score)- (2*general.tirs)), 1, (255, 185, 0)), (80, 400))
			pygame.display.flip()
			pygame.time.delay(700)
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
		fenetre.blit(pygame.image.load("images/"+general.screen+"/pause.png").convert_alpha(),(0,0));
		pygame.display.flip()
		self.boutons2.Netoyage()
		self.boutons2.NouveauBouton((general.w/2 + 100,370), "< Retour")
		self.boutons2.Affichage(fenetre, (0,0), 0)
		self.ok2 = 0
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
				if event.type == MOUSEMOTION:
					self.lastevent = event.dict["buttons"][0]
					self.lastpos = event.dict["pos"]
				if event.type == MOUSEBUTTONDOWN:
					self.lastevent = 1
				if event.type == MOUSEBUTTONUP:
					self.lastevent = 0		
					if self.ok2 >= 1:
						general.back = False
						return 0				
			if self.lastevent == 1:
				self.ok2 = self.boutons2.Affichage(fenetre, self.lastpos, 1)
			else:
				self.boutons2.Affichage(fenetre, self.lastpos, 0)
			
			pygame.display.flip()
		
		fenetre.blit(self.font.render("3", 1, (255, 255, 0)), ((general.w/2)-50, 320))
		pygame.display.flip()
		pygame.time.delay(700)
		fenetre.blit(self.font.render("2", 1, (255, 255, 0)), ((general.w/2), 320))
		pygame.display.flip()
		pygame.time.delay(700)
		fenetre.blit(self.font.render("1", 1, (255, 255, 0)), ((general.w/2)+50, 320))
		pygame.display.flip()
		pygame.time.delay(700)
		
		
	def Chargement(self, fenetre):
			fenetre.blit(self.chargement,(0,0))
			pygame.display.flip()
			
	def Chargement1(self, fenetre):
			self.team = pygame.image.load("images/"+general.screen+"/team.png").convert_alpha()
			fenetre.blit(self.team,(0,0))
			self.barre = pygame.image.load("images/"+general.screen+"/barre-chargement.png").convert()
			fenetre.blit(pygame.image.load("images/"+general.screen+"/barre-chargement.png").convert(),(-1000,general.h -100))
			self.contour = pygame.image.load("images/"+general.screen+"/contour_chargement.png").convert_alpha()
			fenetre.blit(self.contour,(0,general.h -150))
			self.contour2 = pygame.image.load("images/"+general.screen+"/contour_chargement-g.png").convert()
			fenetre.blit(self.contour2,(general.w-25,general.h -150))
			pygame.display.flip()
	
	def ChargementProgression(self,fenetre,progression):
			while general.w/100*progression > self.progression:
				fenetre.blit(self.team,(0,0))
				fenetre.blit(self.barre,(self.progression-1000,general.h - 100))
				fenetre.blit(self.contour,(0,general.h -150))
				fenetre.blit(self.contour2,(general.w-25,general.h -150))
				pygame.time.delay(1)
				self.progression += 1
				pygame.display.flip()
			
	def Chargement2(self, fenetre):
			fenetre.blit(pygame.image.load("images/"+general.screen+"/start.png").convert(),(0,0))
			fenetre.blit(self.barre,(self.progression-1000,general.h - 100))
			fenetre.blit(self.contour,(0,general.h -150))
			fenetre.blit(self.contour2,(general.w-25,general.h -150))
			pygame.display.flip()
			continuer = 1
			while continuer:
				for event in pygame.event.get():
					if event.type == KEYDOWN:
						continuer = 0
			
			
	def CommencementNiveau(self, fenetre):
		fenetre.blit(self.font.render("3", 1, (255, 255, 0)), ((general.w/2)-50, 320))
		pygame.display.flip()
		pygame.time.delay(700)
		fenetre.blit(self.font.render("2", 1, (255, 255, 0)), ((general.w/2), 320))
		pygame.display.flip()
		pygame.time.delay(700)
		fenetre.blit(self.font.render("1", 1, (255, 255, 0)), ((general.w/2)+50, 320))
		pygame.display.flip()
		pygame.time.delay(700)
		
	    

#class DebutNiveau:
	#Cinematique
		



			


