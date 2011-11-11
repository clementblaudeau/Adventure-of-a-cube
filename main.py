#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *	

from cub import *
from tir import *
from onde import *
from obstacles import *
from animations import *
from niveau import *
from menu import *
from text import *
from ennemis import *
from menu import *
from sauvegarde import *

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640, 480), DOUBLEBUF)

#Chargement du niveau
niveau = Niveau("1")
menu = Menu()

#Icone et titre
icone = pygame.image.load("images/cub121.png")
pygame.display.set_icon(icone)
pygame.display.set_caption(niveau.nom)

#Sauvegardes
sauvegarde = Sauvegarde()

#Chargement et collage du fond
scrool = fenetre.get_rect()
scrool = scrool.move(0,0)
j = 0
g = 0
fenetre.blit(niveau.fond, scrool)

chrono = Chrono()

#Chargement du son
#son = pygame.mixer.Sound("son/son_stressant.wav")
#son.play()
repeter = 1;

#Chargement et collage du personnage
cub = Cube()
cub.position = cub.position.move(275,350)
cub.hitbox = cub.hitbox.move(303,373)
fenetre.blit(cub.image, cub.position)
mode = "rapide"
delai = 0
mode_lent = pygame.image.load("images/m_lent.png").convert_alpha()


#Rafraîchissement de l'écran
pygame.display.flip()


continuer = 1
lvl = menu.MenuAffichage(fenetre, sauvegarde.NiveauActuel())
#BOUCLE INFINIE
while lvl:
    niveau = Niveau(str(lvl))
    continuer = 1
    cub.position.x = 0
    cub.position.y = 0
    cub.hitbox.x = 0
    cub.hitbox.y = 0
    cub.position = cub.position.move(275,350)
    cub.hitbox = cub.hitbox.move(303,373)
    cub.vie.vie = 5
    cub.score.score = 0
    pygame.display.set_caption(niveau.nom)
    avancement = 0
    scrool = fenetre.get_rect()
    scrool = scrool.move(0,-544)
    while continuer:
	    key = pygame.key.get_pressed()
	    
	    for event in pygame.event.get():	#Attente des événements
		    #print event
		    if event.type == QUIT:
			    continuer = 0
			    pygame.quit()
			    break
	
	    if key[122] == True and ((pygame.time.get_ticks() - delai) > 500):
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
	    cub.tir1.positions = niveau.obstacles.ColisionsTir(cub.tir1.positions, 1)
	    cub.tir2.positions = niveau.obstacles.ColisionsTir(cub.tir2.positions, 6)
	    cub.tir1.positions = niveau.ennemis.CollisionsTirs(cub.tir1.positions, 1)
	    cub.tir2.positions = niveau.ennemis.CollisionsTirs(cub.tir2.positions, 6)
	    cub.score.score += niveau.obstacles.eclat.Absorption(cub)
	    cub.score.score += niveau.ennemis.eclats.Absorption(cub)
	    
	    if (niveau.ennemis.CollisionCube(cub.hitbox) == True):
		cub.vie.vie += -1
		cub.degat +=80
		if cub.vie.vie < 0:
		    continuer = 0
	
	    #Scrool
	    j += 1
	    if cub.position.top < 10:
		j += 5
		if j > 15:
		    niveau.obstacles.Scrool(cub.position)
		    if niveau.obstacles.ColisionsCube(cub.hitbox) == True:
			cub.position = cub.position.move(0,1)
			cub.hitbox = cub.hitbox.move(0,1)
			niveau.Affichage(fenetre)
	    if j > 15:
		if scrool.top < 0:
		    scrool = scrool.move(0,1)
		j = 0

		avancement += 1

	   
	    
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
	    fenetre.blit(niveau.fond, scrool)	
	    if mode == "lent":
		fenetre.blit(mode_lent, (0,0))
	    chrono.Affichage(pygame.time.get_ticks(), fenetre, "")
	    cub.Affichage(fenetre)
	    niveau.Affichage(fenetre)
	    
	    
	    #Rafraichissement
	    pygame.display.flip()
	
	
	    #Survie
	    if cub.position.top < -50:
		continuer = 0
	    if cub.position.top > 500:
		continuer = 0
		cub.vie.vie = - 1
	    if niveau.Fini == True:
		continuer = 0
		pygame.time.delay(500)
		
	    
	    #Attendre (contre la surcharge du processeur et l'acceleration trop brutale)
	    pygame.time.delay(5)
	    
    menu.FinNiveau(cub.score.score, cub.vie.vie, fenetre)
    if int(lvl) + 1 > int(sauvegarde.NiveauActuel()):
	sauvegarde.NouveauNiveau()
    if menu.vrai == True :
	lvl +=1
    else :
	lvl = menu.MenuAffichage(fenetre, sauvegarde.NiveauActuel())
pygame.quit()

