#!/usr/bin/env python
# -*- coding: utf-8 -*-

#------------------------------#
#             Main.py          #
#	Clement Blaudeau       #
#	    ******	       #
#------------------------------#

import pygame
from pygame.locals import *	

from cub import *
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
import general

pygame.init()

#Ouverture de la fenetre Pygame
fenetre = pygame.display.set_mode((general.w+200, general.h), DOUBLEBUF)

#Chargement du niveau

#Chargement des menus et crédits
menu = Menu()
menuprincipal = MenuPrincipal()
cred = Credits()

#Affichage de l'image du chargement
menu.Chargement(fenetre)

#Icone et titre
icone = pygame.image.load("images/cub121.png")
pygame.display.set_icon(icone)
pygame.display.set_caption("The adventure of Cub !")

#Chargement des sauvegardes
sauvegarde = Sauvegarde()

#Chargement du scrool
scrool = fenetre.get_rect()

#Variables diverses
j = 0
g = 0

#Chargement du chrono
chrono = Chrono()

#Chargement du son
#son = pygame.mixer.Sound("son/son_stressant.wav")
#son.play()
repeter = 1;

#Chargement et collage du personnage, chargement de variables relatives au personnage
cub = Cub()
cub.position = cub.position.move(275,350)
cub.hitbox = cub.hitbox.move(303,373)
fenetre.blit(cub.image, cub.position)
mode = "rapide"
delai = 0
mode_lent = pygame.image.load("images/m_lent.png").convert_alpha()

#Chargement du timer de début de boucle
surcharge_boucle = pygame.time.get_ticks()

#Chargement du panneau de d'informations de jeu
paneau = pygame.image.load("images/paneau.png").convert_alpha()
fenetre.blit(paneau,(general.w,0))

#Rafraîchissement de l'écran
pygame.time.delay(500)
pygame.display.flip()

#Variable de boucle de jeu
continuer = 1

#Ouverture du menu général
modejeu = menuprincipal.MenuAffichage(fenetre, sauvegarde.NiveauActuel())

#Début de la boucle de jeu (enfin ^^)
while modejeu:
    
    #Choix du niveau ou ouverture des crédits ou passage en mode Boss Rush
    
    if modejeu == 2:
	#Mode Fast Play : Choix du niveau
	lvl = menu.MenuAffichage(fenetre, sauvegarde.NiveauActuel())	
#   elif modejeu == 3:
#	boss rush...
    elif modejeu == 4:
	#Affichage des crédits
	lvl = 0
	cred.Affichage(fenetre)
    else:
	#Mode histoire : Niveau 1
	lvl = 1
	
    #Boucle des niveaux
    while lvl != 0:
		#Nettoyage pour commencer le niveau
		menu.Chargement(fenetre)
		niveau = Niveau(str(lvl))
		continuer = 1
		cub.Nettoyage()
		mode = "rapide"
		pygame.display.set_caption(niveau.nom)
		avancement = 0
		scrool = fenetre.get_rect()
		scrool = scrool.move(0,-544)
		pygame.time.delay(100)
		
		#Premier Affichage	
		niveau.Affichage(fenetre,scrool)
		fenetre.blit(paneau,(general.w,0))
		chrono.Affichage(pygame.time.get_ticks(), fenetre, "")
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
						pygame.event.clear()
		
			if key[122] == True and ((pygame.time.get_ticks() - delai) > general.h+10):
				delai = pygame.time.get_ticks()
				if mode == "lent":
					mode = "rapide"
				else:
					mode = "lent"
			if mode == "lent":
				if key[273] == True:
					cub.DeplaceLent('haut', niveau.obstacles)
				if key[274] == True:
					cub.DeplaceLent('bas', niveau.obstacles)
				if key[276] == True:
					cub.DeplaceLent('gauche', niveau.obstacles)
				if key[275] == True:
					cub.DeplaceLent('droite', niveau.obstacles)
				#Tirs
				if key[97] == True:
					cub.tir2.Tir(cub.position)
			else:
				if key[273] == True:
					cub.Deplace('haut', niveau.obstacles)
				if key[274] == True:
					cub.Deplace('bas', niveau.obstacles)
				if key[276] == True:
					cub.Deplace('gauche', niveau.obstacles)
				if key[275] == True:
					cub.Deplace('droite', niveau.obstacles)
				#Tirs
				if key[97] == True:
					cub.tir1.Tir(cub.position)
		    
		    
			g += 1
	
			#Test des colisions avec les obstacles
			cub.tir1.positions = niveau.obstacles.ColisionsTir(cub.tir1.positions, 1+general.niv)
			cub.tir2.positions = niveau.obstacles.ColisionsTir(cub.tir2.positions, 6+general.niv)
			cub.tir1.positions = niveau.ennemis.CollisionsTirs(cub.tir1.positions, 1+general.niv)
			cub.tir2.positions = niveau.ennemis.CollisionsTirs(cub.tir2.positions, 6+general.niv)
			niveau.boss.CollisionTirs(cub.tir1.positions)
			niveau.boss.CollisionTirs(cub.tir2.positions)
			cub.score.score += niveau.obstacles.eclat.Absorption(cub)
			cub.score.score += niveau.ennemis.eclats.Absorption(cub)
			
			if (niveau.ennemis.CollisionCube(cub.hitbox) == True):
			    if cub.degats == 0:
				cub.vie.vie += -1
				cub.degats +=200
				cub.Reboot()
			if (niveau.boss.CollisionCube(cub.hitbox) == True):
			    if cub.degats == 0:
				cub.vie.vie += -1
				cub.degats +=200
				cub.Reboot()
			if cub.vie.vie < 0:
				continuer = 0
	
			#Scrool
			j += 1
			if j > 15:
			    if scrool.top < 0:
					scrool = scrool.move(0,1)
					j = 0
					avancement += 1
					niveau.ennemis.ScroolEnnemisFixes()
					niveau.boss.Scrool()

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
				cub.modelent.Affichage(fenetre)
			chrono.Affichage(pygame.time.get_ticks(), fenetre, "")
			cub.Affichage(fenetre)
			#Rafraichissement
			pygame.display.flip()
	
	
			#Survie
			if cub.position.top < -50:
				continuer = 0
			if cub.position.top > general.h+10:
				continuer = 0
				cub.vie.vie = -1
			if niveau.Fini() == True:
				continuer = 0
				pygame.time.delay(500)
		
	    
			#Attendre (contre la surcharge du processeur et l'acceleration trop brutale)
			tps_fin_boucle = pygame.time.get_ticks()
			if tps_fin_boucle - tps_debut_boucle < 9:
				pygame.time.delay(9 -(tps_fin_boucle - tps_debut_boucle))
		#Fin de la boucle Continuer
		if lvl == 0:
			lvl = menu.MenuAffichage(fenetre, sauvegarde.NiveauActuel())
		else:
		    menu.FinNiveau(cub.score.score, cub.vie.vie, fenetre, sauvegarde.MeilleurScore(lvl, cub.score.CalculScore(cub.vie.vie)))
		    if cub.vie.vie >= 0:
			    if modejeu == 1:
				    if lvl < 30:
					    if (int(lvl) + 1) > int(sauvegarde.NiveauActuel()):
						    sauvegarde.NouveauNiveau()
					    lvl += 1
			    elif modejeu == 2:
				    lvl = menu.MenuAffichage(fenetre, sauvegarde.NiveauActuel())
		    else:
			    lvl = menu.MenuAffichage(fenetre, sauvegarde.NiveauActuel())
	    
    modejeu = menuprincipal.MenuAffichage(fenetre, sauvegarde.NiveauActuel())
pygame.quit()

