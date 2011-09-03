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

avancement = 0



#Chargement et collage du fond
scrool = fenetre.get_rect()
scrool = scrool.move(0,-720)
j = 0
g = 0
w = 0
h = 0
fenetre.blit(niveau.fond, scrool)

chrono = Chrono()

#Chargement du son
son = pygame.mixer.Sound("son/son_stressant.wav")
son.play()
repeter = 1;

#Chargement et collage du personnage
cub = Cube()
cub.position = cub.position.move(275,350)
cub.hitbox = cub.hitbox.move(303,373)
fenetre.blit(cub.image, cub.position)
mode = "rapide"
delai = 0
mode_lent = pygame.image.load("images/m_lent.png").convert_alpha()


#Chargement des attaques
i = 0
onde = Onde()
#tir1 = tir1()
#tir2 = tir2()

k = 0



#Rafraîchissement de l'écran
pygame.display.flip()



continuer = 1
#BOUCLE INFINIE
while menu.MenuAffichage(fenetre) != 0:
    
    niveau = Niveau("1")
    continuer = 1
    while continuer:
	    key = pygame.key.get_pressed()
	    for event in pygame.event.get():	#Attente des événements
		    #print event
		    if event.type == QUIT:
			    continuer = 0
	
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
		print "fin !!"
		cub.vie.vie += -1
		if cub.vie.vie < 0:
		    continuer = 0
	
	    #Scrool
	    j += 1
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
	    if avancement >= 500:
		continuer = 0
	    if niveau.ennemis.positions == []:
		continuer = 0
	    else:
		print niveau.ennemis.positions
		
		
		
	    #Son
	    repeter = pygame.time.get_ticks() % 157000
	    if repeter > 100000:
		repet = 0
	    if repeter > 0 and repeter < 100 and repet == 0:
		son = pygame.mixer.Sound("son/son_stressant.wav")
		son.play()
		repet = 1
	    
	    #Attendre (contre la surcharge du processeur et l'acceleration trop brutale)
	    pygame.time.delay(1)
    menu.FinNiveau(cub.score.score, cub.vie.vie, fenetre)



