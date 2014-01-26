#!/usr/bin/env python
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
#	main.py          
#	Clement Blaudeau       
#	******	       
#------------------------------
#	Fichier principal
#------------------------------

import pygame
from pygame.locals import *	

from cub import *
from perl import *
from sneeze import *
from tir import *
from onde import *
from obstacles import *
from animations import *
from level import *
from menu import *
from credits import *
from text import *
from ennemis import *
from menu import *
from menuprincipal import *
from sauvegarde import *
from bossrush import *
import general

pygame.init()

#Ouverture de la window Pygame
window = pygame.display.set_mode((general.w+200, general.h), DOUBLEBUF)
#window = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
#taille = window.get_rect()
#general.h = window.get_height()
#general.w = int(window.get_width()) - 200
#general.screen = "full"

#Load des elements du moteur
#jeu = Game()

#Load des menus et crédits
menu = Menu()
menuprincipal = MenuPrincipal()
cred = Credits()

#Display de l'image du Load
menu.Load1(window)

#Icone et titre
icone = pygame.image.load("../images/Cub/cub121.png")
pygame.display.set_icon(icone)
pygame.display.set_caption("The adventure of Cub !")
menu.LoadProgress(window,30)

#Load des sauvegardes
sauvegarde = Sauvegarde()

menu.LoadProgress(window,40)

#Load du scrool
scrool = window.get_rect()

#Variables diverses
j = 0

#Load du ../son/
pygame.mixer.init()

#Load et collage du personnage, Load de variables relatives au personnage
cub = Cub()
cub.position = cub.position.move(275,350)
cub.hitbox = cub.hitbox.move(303,373)
mode = "rapide"
delai = 0
mode_lent = pygame.image.load("../images/m_lent.png").convert_alpha()
mode_lent2 = pygame.image.load("../images/m_lent2.png").convert_alpha()
menu.LoadProgress(window,50)
#Load du timer de début de boucle
surcharge_boucle = pygame.time.get_ticks()

#Load du panneau de d'informations de jeu
paneau = pygame.image.load("../images/paneau(0).png").convert_alpha()

menu.LoadProgress(window,95)
#Rafraîchissement de l'écran
menu.LoadProgress(window,105)
menu.Load2(window)

game_mode = 1
#Variable de boucle de jeu
_continue = 1
#Ouverture du menu général
#Début de la boucle de jeu (enfin ^^)
while game_mode:
    general.back = False
    while general.back == False:
	
	#Choix du level ou ouverture des crédits ou passage en mode Boss Rush
	game_mode = menuprincipal.Menu_Display(window,sauvegarde.BossRush())
	
	if game_mode == 1:
	    #Mode Histoire
	    personnage = menuprincipal.Choixpersonnage(window, "Campagne")
	    print personnage
	    if general.back == True:
		continue
	    general.diff_level = menuprincipal.ChoixLevel(window, sauvegarde.Difficulte(personnage - 1),sauvegarde.History(personnage))

	    if general.back == True: 
		continue
	    paneau = pygame.image.load("../images/paneau("+str(general.diff_level)+").png").convert_alpha()
	    general.back = True
	    lvl = sauvegarde.LevelActuel(str(personnage))

	elif game_mode == 2:
	    #Mode Fast Play : Choix du level
	    campagne = menuprincipal.Choixpersonnage(window, "Campagne ")
	    if general.back == True:
		continue
	    general.diff_level = menuprincipal.ChoixLevel(window, sauvegarde.Difficulte(campagne - 1),sauvegarde.History(campagne))
	    if general.back == True:
		continue
	    paneau = pygame.image.load("../images/paneau("+str(general.diff_level)+").png").convert_alpha()
	    lvl = menu.Menu_Display(window, sauvegarde.LevelActuel(campagne))	
	    if general.back == True:
		continue
	    personnage = menuprincipal.Choixpersonnage(window)
	    if general.back == True:
		continue
	    general.back = True
	elif game_mode == 3:
	    #Mode Boss Rush
	    campagne = menuprincipal.Choixpersonnage(window,sauvegarde.BossRushes(), "Campagne ")
	    if general.back == True:
		continue
	    lvl = 1
	    general.scrool = -100
	    general.diff_level = menuprincipal.ChoixLevel(window, sauvegarde.Difficulte(campagne - 1),sauvegarde.BossRushesDifficulty(campagne))
	    if general.back == True:
		general.back = False
		continue
	    paneau = pygame.image.load("../images/paneau("+str(general.diff_level)+").png").convert_alpha()
	    personnage = menuprincipal.Choixpersonnage(window)
	    if general.back == True:
		general.back = False
		continue
	    general.back = True
	elif game_mode == 4:
	    #Display des crédits
	    lvl = 0
	    cred.Display(window)
	
	print lvl
	#Boucle des niveaux
	while lvl != 0:
		#Nettoyage pour commencer le level
		if personnage == 1:
		    cub = Cub()
		elif personnage == 2:
		    cub = Perl()
		else:
		    cub = Sneeze()
		menu.Chargement(window)
		if game_mode != 3:
		    level = Level(str(lvl), str(general.caracters[personnage - 1]))
		    general.scrool = -544
		    menu.DebutLevel(window,lvl)
		else:
		    level = BossRush(general.caracters[campagne - 1])
		    general.scrool = -100
		_continue = 1
		cub.Nettoyage()
		mode = "rapide"
		pygame.display.set_caption(level.nom)
		avancement = 0
		scrool = window.get_rect()
		scrool = scrool.move(0,general.scrool)
		pygame.time.delay(100)
		level.sound.play(-1)
		level.sound.set_volume(0.9)
		
		#ReDisplay	
		level.Display(window,scrool)
		window.blit(paneau,(general.w,0))
		cub.Display(window)
		#Rafraichissement
		pygame.display.flip()
		menu.CommencementLevel(window)
		
		while _continue:
			tps_debut_boucle = pygame.time.get_ticks()
			key = pygame.key.get_pressed()
			for event in pygame.event.get():	#Attente des événements
				#print event
				if event.type == QUIT:
					lvl = 0
					_continue = 0
					break
				elif event.type == KEYDOWN:
					if event.key == 27:
						menu.Pause(window)
						if general.back == False:
						    lvl = 0
						    cub.life.life = 0
						    _continue = 0
						    continue
						pygame.event.clear()
		
			if ((key[general.k_slow] == True) or (key[122] == True)) and ((pygame.time.get_ticks() - delai) > general.h+10):
				delai = pygame.time.get_ticks()
				if mode == "lent":
					mode = "rapide"
				else:
					mode = "lent"
					cub.Reboot()
			
			cub.Action(key,mode,level.obstacles)
			if mode == "lent":
				#Tirs
				if (key[general.k_shot3] == True) or (key[114] == True):
					cub.bomb.Tir(level.ennemis, window)
			else:
				#Tirs
				if (key[general.k_shot3] == True) or (key[114] == True):
					cub.bomb.Tir(level.ennemis, window)
		    
	
			#Test des colisions avec les obstacles
			if general.c_protect == False:
			    level.Collisions(cub)
			if cub.life.life < 0:
				_continue = 0
			
			if level.clear == True:
			    level.Cleaner(cub)
			    scrool = window.get_rect()
			    scrool = scrool.move(0,general.scrool)
			#Scrool
			j += 1
			if j > 15:
			    if scrool.top < 0:
					scrool = scrool.move(0,1)
					j = 0
					avancement += 1
					level.ennemis.ScroolEnnemisFixes()
					try:
					    if game_mode == 3:
						level.boss.Scrool_BossRush(scrool)
					    else:
						level.boss.Scrool()
					except:
					   pass
			
			
			cub.Glissement(level.obstacles)
	    
			#Avance des attaques
			cub.AvanceTirs()
	
			#Rotation du cube
			cub.Rotation()
	
			#Scrool des obstacles
			level.obstacles.Scrool(cub.position)
			if level.obstacles.ColisionsCube(cub.hitbox) == True:
				cub.position = cub.position.move(0,1)
				cub.hitbox = cub.hitbox.move(0,1)
			
			#Re-collage + Display des murs et ennemis
			level.Display(window, scrool)
			window.blit(paneau,(general.w,0))
			if mode == "lent":
				window.blit(mode_lent, (0,0))
				window.blit(mode_lent2, (general.w,0))
				cub.modelent.Display(window)
			#level.chrono.Display(pygame.time.get_ticks(), window, "")
			cub.Display(window)
			#Rafraichissement
			pygame.display.flip()
	
	
			#Surlife
			if cub.position.top < -50:
				_continue = 0
				level.sound.stop()
			if cub.position.top > general.h+10:
				_continue = 0
				level.sound.stop()
				cub.life.life = -1
			if level.Fini() == True:
				_continue = 0
				if game_mode == 3:
				    lvl = "bossrush"
				pygame.time.delay(500)
				level.sound.stop()
		
	    
			#Attendre (contre la surcharge du processeur et l'acceleration trop brutale)
			tps_fin_boucle = pygame.time.get_ticks()
			if tps_fin_boucle - tps_debut_boucle < 9:
				pygame.time.delay(9 -(tps_fin_boucle - tps_debut_boucle))
				
		#Fin de la boucle _continue
		
		level.sound.stop()
		if lvl == 0:
			continue
		else:
		    if game_mode != 3:
			menu.FinLevel(cub.score.score, cub.life.life, window, sauvegarde.MeilleurScore(lvl, cub.score.CalculScore(cub.life.life), general.caracters[personnage - 1]))
		    elif game_mode == 3:
			menu.FinLevel(cub.score.score, 40 - cub.life.lifes_utilisees - cub.life.life, window, sauvegarde.MeilleurScore(lvl, cub.score.CalculScore(cub.life.life), general.caracters[personnage - 1]))
		    if cub.life.life >= 0:
			    if game_mode == 1:
				if int(int(lvl) + 1) > int(sauvegarde.LevelActuel(personnage)):
				    sauvegarde.NewLevel(general.caracters[personnage - 1])
				if lvl != 16:
				    lvl = str(int(lvl) + 1)
				else:
				    menu.DebutLevel(window,"final")
				    lvl = 0
			    elif game_mode == 2:
				    lvl = menu.Menu_Display(window, sauvegarde.LevelActuel(personnage))
			    elif game_mode == 3:
				    lvl = 0
		    else:
			lvl = 0
			continue
	    

pygame.quit()

