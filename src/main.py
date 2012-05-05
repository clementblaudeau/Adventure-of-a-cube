#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Copyright (c) 2012 Clément Blaudeau
This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.
<<<<<<< HEAD
=======

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
#from sneeze import *
from tir import *
from onde import *
from obstacles import *
from animations import *
from niveau import *
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

#Ouverture de la fenetre Pygame
fenetre = pygame.display.set_mode((general.w+200, general.h), DOUBLEBUF)
#fenetre = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
#taille = fenetre.get_rect()
#general.h = fenetre.get_height()
#general.w = int(fenetre.get_width()) - 200
#general.screen = "full"

#Chargement des elements du moteur
#jeu = Game()

#Chargement des menus et crédits
menu = Menu()
menuprincipal = MenuPrincipal()
cred = Credits()

#Affichage de l'image du chargement
menu.Chargement1(fenetre)

#Icone et titre
icone = pygame.image.load("../images/Cub/cub121.png")
pygame.display.set_icon(icone)
pygame.display.set_caption("The adventure of Cub !")
menu.ChargementProgression(fenetre,30)

#Chargement des sauvegardes
sauvegarde = Sauvegarde()

menu.ChargementProgression(fenetre,40)

#Chargement du scrool
scrool = fenetre.get_rect()

#Variables diverses
j = 0
g = 0

#Chargement du ../son/
pygame.mixer.init()
#son = pygame.mixer.Sound("../son/../son/_stressant.wav")
#son.play()
repeter = 1;

#Chargement et collage du personnage, chargement de variables relatives au personnage
cub = Cub()
cub.position = cub.position.move(275,350)
cub.hitbox = cub.hitbox.move(303,373)
mode = "rapide"
delai = 0
mode_lent = pygame.image.load("../images/"+general.screen+"/m_lent.png").convert_alpha()
mode_lent2 = pygame.image.load("../images/"+general.screen+"/m_lent2.png").convert_alpha()
menu.ChargementProgression(fenetre,50)
#Chargement du timer de début de boucle
surcharge_boucle = pygame.time.get_ticks()

#Chargement du panneau de d'informations de jeu
paneau = pygame.image.load("../images/"+general.screen+"/paneau(0).png").convert_alpha()

menu.ChargementProgression(fenetre,95)
#Rafraîchissement de l'écran
menu.ChargementProgression(fenetre,105)
menu.Chargement2(fenetre)

modejeu = 1
#Variable de boucle de jeu
continuer = 1
#Ouverture du menu général
#Début de la boucle de jeu (enfin ^^)
while modejeu:
    general.back = False
    while general.back == False:
	modejeu = menuprincipal.MenuAffichage(fenetre,sauvegarde.BossRush())
	#Choix du niveau ou ouverture des crédits ou passage en mode Boss Rush
	if modejeu == 1:
	    #Mode Histoire
	    personnage = menuprincipal.Choixpersonnage(fenetre, "Campagne")
	    if general.back == True:
		general.back = False
		continue
	    general.diff_level = menuprincipal.ChoixNiveau(fenetre, sauvegarde.Difficulte(personnage - 1),sauvegarde.History(personnage))
	    if general.back == True: 
		general.back = False
		continue
	    paneau = pygame.image.load("../images/"+general.screen+"/paneau("+str(general.diff_level)+").png").convert_alpha()
	    general.back = True
	    lvl = sauvegarde.NiveauActuel(str(personnage))
	elif modejeu == 2:
	    #Mode Fast Play : Choix du niveau
	    campagne = menuprincipal.Choixpersonnage(fenetre, "Campagne ")
	    if general.back == True:
		general.back = False
		continue
	    general.diff_level = menuprincipal.ChoixNiveau(fenetre, sauvegarde.Difficulte(campagne - 1),sauvegarde.History(campagne))
	    if general.back == True:
		general.back = False
		continue
	    paneau = pygame.image.load("../images/"+general.screen+"/paneau("+str(general.diff_level)+").png").convert_alpha()
	    lvl = menu.MenuAffichage(fenetre, sauvegarde.NiveauActuel(campagne))	
	    if general.back == True:
		general.back = False
		continue
	    personnage = menuprincipal.Choixpersonnage(fenetre)
	    if general.back == True:
		general.back = False
		continue
	    general.back = True
	elif modejeu == 3:
	    #Mode Boss Rush
	    campagne = menuprincipal.Choixpersonnage(fenetre,sauvegarde.BossRushes(), "Campagne ")
	    if general.back == True:
		general.back = False
		continue
	    lvl = 1
	    general.scrool = -100
	    general.diff_level = menuprincipal.ChoixNiveau(fenetre, sauvegarde.Difficulte(campagne - 1),sauvegarde.BossRushesDifficulty(campagne))
	    if general.back == True:
		general.back = False
		continue
	    paneau = pygame.image.load("../images/"+general.screen+"/paneau("+str(general.diff_level)+").png").convert_alpha()
	    personnage = menuprincipal.Choixpersonnage(fenetre)
	    if general.back == True:
		general.back = False
		continue
	    general.back = True
	elif modejeu == 4:
	    #Affichage des crédits
	    lvl = 0
	    cred.Affichage(fenetre)
	
	
	#Boucle des niveaux
	while lvl != 0:
		#Nettoyage pour commencer le niveau
		if personnage == 1:
		    cub = Cub()
		elif personnage == 2:
		    cub = Perl()
		else:
		    cub = Sneeze()
		menu.Chargement(fenetre)
		if modejeu != 3:
		    niveau = Niveau(str(lvl), str(general.caracters[personnage - 1]))
		    general.scrool = -544
		    menu.DebutNiveau(fenetre,lvl)
		else:
		    niveau = BossRush(general.caracters[campagne - 1])
		    general.scrool = -100
		continuer = 1
		cub.Nettoyage()
		mode = "rapide"
		pygame.display.set_caption(niveau.nom)
		avancement = 0
		scrool = fenetre.get_rect()
		scrool = scrool.move(0,general.scrool)
		pygame.time.delay(100)
		niveau.son.play(-1)
		niveau.son.set_volume(0.9)
		
		#ReAffichage	
		niveau.Affichage(fenetre,scrool)
		fenetre.blit(paneau,(general.w,0))
		cub.Affichage(fenetre)
		#Rafraichissement
		pygame.display.flip()
		menu.CommencementNiveau(fenetre)
		
		while continuer:
			tps_debut_boucle = pygame.time.get_ticks()
			key = pygame.key.get_pressed()
			for event in pygame.event.get():	#Attente des événements
				#print event
				if event.type == QUIT:
					lvl = 0
					continuer = 0
					break
				elif event.type == KEYDOWN:
					if event.key == 27:
						menu.Pause(fenetre)
						if general.back == False:
						    lvl = 0
						    cub.vie.vie = 0
						    continuer = 0
						    continue
						pygame.event.clear()
		
			if ((key[general.k_slow] == True) or (key[122] == True)) and ((pygame.time.get_ticks() - delai) > general.h+10):
				delai = pygame.time.get_ticks()
				if mode == "lent":
					mode = "rapide"
				else:
					mode = "lent"
					cub.Reboot()
			if mode == "lent":
				if key[general.k_up] == True:
					cub.DeplaceLent('haut', niveau.obstacles)
				if key[general.k_down] == True:
					cub.DeplaceLent('bas', niveau.obstacles)
				if key[general.k_left] == True:
					cub.DeplaceLent('gauche', niveau.obstacles)
				if key[general.k_right] == True:
					cub.DeplaceLent('droite', niveau.obstacles)
				#Tirs
				if (key[general.k_shot] == True) or (key[97] == True):
					cub.tir2.Tir(cub.position)
				if (key[general.k_shot2] == True) or (key[101] == True):
					cub.onde.NouvelleOnde(cub.position.move(-70,-50))
				if (key[general.k_shot3] == True) or (key[114] == True):
					cub.bomb.Tir(niveau.ennemis, fenetre)
			else:
				if key[general.k_up] == True:
					cub.Deplace('haut', niveau.obstacles)
				if key[general.k_down] == True:
					cub.Deplace('bas', niveau.obstacles)
				if key[general.k_left] == True:
					cub.Deplace('gauche', niveau.obstacles)
				if key[general.k_right] == True:
					cub.Deplace('droite', niveau.obstacles)
				#Tirs
				if (key[general.k_shot] == True) or (key[97] == True):
					cub.tir1.Tir(cub.position)
				if (key[general.k_shot2] == True) or (key[101] == True):
					cub.onde.NouvelleOnde(cub.position.move(-70,-50))
				if (key[general.k_shot3] == True) or (key[114] == True):
					cub.bomb.Tir(niveau.ennemis, fenetre)
		    
		    
			g += 1
	
			#Test des colisions avec les obstacles
			if general.c_protect == False:
			    niveau.Collisions(cub)
			if cub.vie.vie < 0:
				continuer = 0
			
			if niveau.clear == True:
			    niveau.Cleaner(cub)
			    scrool = fenetre.get_rect()
			    scrool = scrool.move(0,general.scrool)
			#Scrool
			j += 1
			if j > 15:
			    if scrool.top < 0:
					scrool = scrool.move(0,1)
					j = 0
					avancement += 1
					niveau.ennemis.ScroolEnnemisFixes()
					try:
					    niveau.boss.Scrool()
					except:
					    pass
			
			
			cub.Glissement(niveau.obstacles)
	    
			#Avance des attaques
			cub.AvanceTirs()
	
			#Rotation du cube
			cub.Rotation()
	
			#Scrool des obstacles
			niveau.obstacles.Scrool(cub.position)
			if niveau.obstacles.ColisionsCube(cub.hitbox) == True:
				cub.position = cub.position.move(0,1)
				cub.hitbox = cub.hitbox.move(0,1)
			
			#Re-collage + Affichage des murs et ennemis
			niveau.Affichage(fenetre, scrool)
			fenetre.blit(paneau,(general.w,0))
			if mode == "lent":
				fenetre.blit(mode_lent, (0,0))
				fenetre.blit(mode_lent2, (general.w,0))
				cub.modelent.Affichage(fenetre)
			#niveau.chrono.Affichage(pygame.time.get_ticks(), fenetre, "")
			cub.Affichage(fenetre)
			#Rafraichissement
			pygame.display.flip()
	
	
			#Survie
			if cub.position.top < -50:
				continuer = 0
				niveau.son.stop()
			if cub.position.top > general.h+10:
				continuer = 0
				niveau.son.stop()
				cub.vie.vie = -1
			if niveau.Fini() == True:
				continuer = 0
				if modejeu == 3:
				    lvl = "bossrush"
				pygame.time.delay(500)
				niveau.son.stop()
		
	    
			#Attendre (contre la surcharge du processeur et l'acceleration trop brutale)
			tps_fin_boucle = pygame.time.get_ticks()
			if tps_fin_boucle - tps_debut_boucle < 9:
				pygame.time.delay(9 -(tps_fin_boucle - tps_debut_boucle))
				
		#Fin de la boucle Continuer
		
		niveau.son.stop()
		if lvl == 0:
			continue
		else:
		    if modejeu != 3:
			menu.FinNiveau(cub.score.score, cub.vie.vie, fenetre, sauvegarde.MeilleurScore(lvl, cub.score.CalculScore(cub.vie.vie), general.caracters[personnage - 1]))
		    elif modejeu == 3:
			menu.FinNiveau(cub.score.score, 40 - cub.vie.vies_utilisees - cub.vie.vie, fenetre, sauvegarde.MeilleurScore(lvl, cub.score.CalculScore(cub.vie.vie), general.caracters[personnage - 1]))
		    if cub.vie.vie >= 0:
			    if modejeu == 1:
				if int(int(lvl) + 1) > int(sauvegarde.NiveauActuel(personnage)):
				    sauvegarde.NouveauNiveau(general.caracters[personnage - 1])
				if lvl != 16:
				    lvl = str(int(lvl) + 1)
				else:
				    menu.DebutNiveau(fenetre,"final")
				    lvl = 0
			    elif modejeu == 2:
				    lvl = menu.MenuAffichage(fenetre, sauvegarde.NiveauActuel(personnage))
			    elif modejeu == 3:
				    lvl = 0
		    else:
			lvl = 0
			continue
	    

pygame.quit()

