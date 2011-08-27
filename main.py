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

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640, 480), DOUBLEBUF)

#Chargement du niveau
niveau = Niveau("1")

#Icone et titre
icone = pygame.image.load("images/cub121.png")
pygame.display.set_icon(icone)
pygame.display.set_caption("The Adventure Of Cub - Episode 1")

avancement = 0

#Chargement et collage du fond
scrool = fenetre.get_rect()
scrool = scrool.move(0,-720)
j = 0
g = 0
h = 0
fenetre.blit(niveau.fond, scrool)


#Chargement du son
son = pygame.mixer.Sound("son/son_stressant.wav")
son.play()
repeter = 1;

#Chargement et collage du personnage
cub = Cube()
cub.position = cub.position.move(275,350)
cub.hitbox = cub.hitbox.move(300,370)
fenetre.blit(cub.image, cub.position)

barre = pygame.image.load("images/barre_onde.png").convert_alpha()
poss_barre = barre.get_rect()
poss_barre = poss_barre.move(640,20)
fenetre.blit(barre,poss_barre)


#Chargement des attaques
i = 0
onde = Onde()
tir1 = tir1()
tir2 = tir2()

k = 0

#Murs
obstacles = Obstacles()


#Rafraîchissement de l'écran
pygame.display.flip()

#Maintiend des touches
pygame.key.set_repeat(2, 10)


#BOUCLE INFINIE
continuer = 1
while continuer:
	for event in pygame.event.get():	#Attente des événements
		
		if event.type == QUIT:
			continuer = 0
		if event.type == KEYDOWN:
			if event.key == K_DOWN:
			     cub.Deplace('bas', niveau.obstacles)
			if event.key == K_UP:
			     cub.Deplace('haut', niveau.obstacles)
			if event.key == K_LEFT:
			     cub.Deplace('gauche', niveau.obstacles)
			if event.key == K_RIGHT:
			     cub.Deplace('droite', niveau.obstacles)
			    
	key = pygame.key.get_pressed()
	#Tirs
	if key[303] == True or key[304] == True:
	    tir2.Tir(cub.position)
	elif key[306] == True or key[305] == True:
	    tir1.Tir(cub.position)
	    
	g += 1
	
	#Test des colisions avec les obstacles
	tir1.positions = niveau.obstacles.ColisionsTir(tir1.positions, 1)
	tir2.positions = niveau.obstacles.ColisionsTir(tir2.positions, 3)
	
	#Scrool
	j += 1
	if j > 15:
	    if scrool.top < 0:
		scrool = scrool.move(0,1)
	    j = 0
	    avancement += 1
	
	h +=1
	if h > 1:
	    cub.Glissement(niveau.obstacles)
	    h = 0
	#Avance des attaques et des ondes
	tir1.Progression()
	tir2.Progression()
	onde.Progression()
	
	#Rotation du cube
	cub.rotation()
	
	#Scrool des obstacles
	niveau.obstacles.Scrool(cub.position)
	if niveau.obstacles.ColisionsCube(cub.hitbox) == True:
	    cub.position = cub.position.move(0,1)
	    cub.hitbox = cub.hitbox.move(0,1)
	
	#Re-collage
	fenetre.blit(niveau.fond, scrool)	
	tir1.Affichage(fenetre)
	tir2.Affichage(fenetre)
	onde.Affichage(fenetre)
	fenetre.blit(barre,poss_barre)
	
	
	#Affichage des murs
	niveau.obstacles.Affichage(fenetre)
	
	cub.Affichage(fenetre)
	
	#Rafraichissement
	pygame.display.flip()
	
	
	#Survie
	if cub.position.top < -50:
	    continuer = 0
	if cub.position.top > 500:
	    continuer = 0
	
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




