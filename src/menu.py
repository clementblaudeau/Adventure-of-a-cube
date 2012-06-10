# -*- coding: utf-8 -*-
'''
Copyright (c) 2012 Clément Blaudeau
This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
'''
#------------------------------
#	menu.py			   
#	Clement Blaudeau       
#	******	       
#------------------------------
#	Fichier important qui se charge
#	des menu de level, des cinématiques
#	des pauses, des game-over et des 
#	barres de Load
#------------------------------


import pygame
from pygame.locals import *
import general
from cub import *
from boutons import *


class Menu:
	
	def __init__(self):
		self.fond = pygame.image.load("../images/menu.png").convert_alpha()
		self.gagne = pygame.image.load("../images/fin_niveau.png").convert()
		self.Load = pygame.image.load("../images/chargement.png").convert()
		self.boutons = Bouton_Nb()
		self.boutons2 = Bouton_Text()
		self.lastclic = 0
		self.lastevent = 0
		self.ok = 0
		self.lastpos = (0,0)
		self.font = pygame.font.Font("../polices/Coalition.ttf", 17)
		self.x = 30
		self.y = 150
		self.vrai = False
		self.cube = Cub()
		self.Progress = 0
		self.cube.position = self.cube.position.move(100,100)
		self.sound_win = pygame.mixer.Sound("../son/win.ogg")
		self.sound_win = pygame.mixer.Sound("../son/lose.ogg")
		#self.boutons.NewBouton((30,160), 1)
		#self.boutons.NewBouton((30,210), 2)
		
	def Menu_Display(self,window,nb):
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
			self.boutons.NewBouton((self.x,self.y), self.nb)
			self.y += 50
			nb -= 1
		
		self.boutons2.NewBouton((general.w/2 + 100,370), "< Retour")
		window.blit(self.fond,(0,0))
		_continue = 1
		self.boutons.Display(window, (0,0), 0)
		self.boutons2.Display(window, (0,0), 0)
		self.ok = 0
		self.ok2 = 0
		while _continue:
			window.blit(self.fond,(0,0))
			self.cube.Rotation()
			self.cube.Display2(window)
			
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
				self.ok = self.boutons.Display(window, self.lastpos, 1)
				self.ok2 = self.boutons2.Display(window, self.lastpos, 1)
			else:
				self.boutons.Display(window, self.lastpos, 0)
				self.boutons2.Display(window, self.lastpos, 0)
			
			pygame.display.flip()
				
	def DebutLevel(self, window,lvl):
		try:
			movie = pygame.movie.Movie ('../videos/'+str(lvl)+'.mpg')
		except:
			movie = pygame.movie.Movie ('../videos/intro.mpg')
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
		#window = pygame.display.set_mode((general.w+200, general.h), DOUBLEBUF)
				

	def FinLevel(self, score, lifes, window, meilleurScore):
		
		
		if lifes > -1:
			image = self.gagne
			vrai = True
			self.vrai = True
		else:
			image = pygame.image.load("../images/game_over.png").convert()
			self.sound_lose.play()
			vrai = False
			self.vrai = False
		window.blit(image,(0,0))
		if vrai:
			self.sound_win.play()
			self.font = pygame.font.Font("../polices/Coalition.ttf", 17)
			window.blit(image,(0,0))
			pygame.time.delay(500)
			window.blit(self.font.render(" Score : " + str(score), 1, (255, 255, 0)), (80, 320))
			pygame.display.flip()
			pygame.time.delay(700)
			window.blit(self.font.render(" + Lifes Restantes : " + str(lifes), 1, (255, 255, 0)), (80, 340))
			pygame.display.flip()
			pygame.time.delay(700)
			window.blit(self.font.render(" + Lifes Restantes : " + str(lifes) + " x 100 : " + str(lifes * 100), 1, (255, 255, 0)), (80, 340))
			window.blit(self.font.render(" - Tirs : " + str(general.tirs), 1, (255, 0, 0)), (80, 360))
			pygame.display.flip()
			pygame.time.delay(700)
			window.blit(self.font.render(" - Tirs : " + str(general.tirs) +" x 2 : " + str(general.tirs*2), 1, (255, 0, 0)), (80, 360))
			pygame.display.flip()
			pygame.time.delay(700)
			window.blit(self.font.render("---------", 1, (255, 255, 0)), (130, 380))
			pygame.display.flip()
			pygame.time.delay(700)
			window.blit(self.font.render(" Total : " +  str((lifes * 100 + score)- (2*general.tirs)), 1, (255, 185, 0)), (80, 400))
			pygame.display.flip()
			pygame.time.delay(700)
			window.blit(self.font.render(str(meilleurScore), 1, (255, 185, 0)), (250, 50))
			pygame.display.flip()
			pygame.time.delay(700)
			
			
		
		_continue = 1
		pygame.event.clear()
		while _continue:
			pygame.time.delay(1)
			window.blit(image,(0,0))
			if vrai:
				window.blit(self.font.render(" Score : " + str(score), 1, (255, 255, 0)), (80, 320))
				window.blit(self.font.render(" + Lifes Restantes : " + str(lifes) + " x 100 : " + str(lifes * 100), 1, (255, 255, 0)), (80, 340))
				window.blit(self.font.render(" - Tirs : " + str(general.tirs) +" x 2 : " + str(general.tirs*2), 1, (255, 0, 0)), (80, 360))
				window.blit(self.font.render("---------", 1, (255, 255, 0)), (130, 380))
				window.blit(self.font.render(" Total : " +  str((lifes * 100 + score)- (2*general.tirs)), 1, (255, 185, 0)), (80, 400))
				window.blit(self.font.render(str(meilleurScore), 1, (255, 185, 0)), (250, 50))
			pygame.display.flip()
			
			for event in pygame.event.get():
				if event.type == QUIT:
					_continue = 0
				if event.type == KEYDOWN:
							_continue = 0
							
	def Pause(self,window):
		window.blit(pygame.image.load("../images/pause.png").convert_alpha(),(0,0));
		pygame.display.flip()
		self.boutons2.Netoyage()
		self.boutons2.NewBouton((general.w/2 + 100,370), "< Retour")
		self.boutons2.Display(window, (0,0), 0)
		self.ok2 = 0
		pygame.time.delay(100)
		_continue = 1
		pygame.event.clear()
		while _continue == 1:
			for event in pygame.event.get():	#Attente des événements
				#print event
				if event.type == KEYDOWN:
					if event.key == 27:
						_continue = 0
						pygame.event.clear()
				elif event.type == QUIT:
					_continue = 0
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
				self.ok2 = self.boutons2.Display(window, self.lastpos, 1)
			else:
				self.boutons2.Display(window, self.lastpos, 0)
			
			pygame.display.flip()
		
		window.blit(self.font.render("3", 1, (255, 255, 0)), ((general.w/2)-50, 320))
		pygame.display.flip()
		pygame.time.delay(700)
		window.blit(self.font.render("2", 1, (255, 255, 0)), ((general.w/2), 320))
		pygame.display.flip()
		pygame.time.delay(700)
		window.blit(self.font.render("1", 1, (255, 255, 0)), ((general.w/2)+50, 320))
		pygame.display.flip()
		pygame.time.delay(700)
		
		
	def Chargement(self, window):
			window.blit(self.Load,(0,0))
			pygame.display.flip()
			
	def Load1(self, window):
			self.team = pygame.image.load("../images/team.png").convert_alpha()
			window.blit(self.team,(0,0))
			self.barre = pygame.image.load("../images/barre-chargement.png").convert()
			window.blit(pygame.image.load("../images/barre-chargement.png").convert(),(-1000,general.h -100))
			self.contour = pygame.image.load("../images/contour_chargement.png").convert_alpha()
			window.blit(self.contour,(0,general.h -150))
			self.contour2 = pygame.image.load("../images/contour_chargement-g.png").convert()
			window.blit(self.contour2,(general.w-25,general.h -150))
			pygame.display.flip()
	
	def LoadProgress(self,window,Progress):
			while general.w/100*Progress > self.Progress:
				window.blit(self.team,(0,0))
				window.blit(self.barre,(self.Progress-1000,general.h - 100))
				window.blit(self.contour,(0,general.h -150))
				window.blit(self.contour2,(general.w-25,general.h -150))
				pygame.time.delay(1)
				self.Progress += 2
				pygame.display.flip()
			
	def Load2(self, window):
			window.blit(pygame.image.load("../images/start.png").convert(),(0,0))
			window.blit(self.barre,(self.Progress-1000,general.h - 100))
			window.blit(self.contour,(0,general.h -150))
			window.blit(self.contour2,(general.w-25,general.h -150))
			pygame.display.flip()
			_continue = 1
			while _continue:
				for event in pygame.event.get():
					if event.type == KEYDOWN:
						_continue = 0
			
			
	def CommencementLevel(self, window):
		window.blit(self.font.render("3", 1, (255, 255, 0)), ((general.w/2)-50, 320))
		pygame.display.flip()
		pygame.time.delay(700)
		window.blit(self.font.render("2", 1, (255, 255, 0)), ((general.w/2), 320))
		pygame.display.flip()
		pygame.time.delay(700)
		window.blit(self.font.render("1", 1, (255, 255, 0)), ((general.w/2)+50, 320))
		pygame.display.flip()
		pygame.time.delay(700)
		
	    

#class DebutLevel:
	#Cinematique
		



			


