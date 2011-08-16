#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *	

from cub import *
from tir import *
from onde import *
from obstacles import *

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640, 480))

#Icone et titre
icone = pygame.image.load("images/cub121.png")
pygame.display.set_icon(icone)
pygame.display.set_caption("The Adventure Of Cub - Episode 1")

avancement = 0

#Chargement et collage du fond
fond = pygame.image.load("images/espace.jpg").convert()
scrool = fenetre.get_rect()
scrool = scrool.move(0,-720)
j = 0
g = 0
fenetre.blit(fond, scrool)

#Chargement du son
son = pygame.mixer.Sound("son/son_stressant.wav")
son.play()
repeter = 1;

#Chargement et collage du personnage
cub = Cube()
cub.position = cub.position.move(275,350)
cub.hitbox = cub.hitbox.move(290,360)
fenetre.blit(cub.image, cub.position)


#Chargement des attaques
i = 0
onde = Onde()
tir1 = tir1()
tir2 = tir2()

k = 0

#Murs
obstacles = Obstacles()
obstacles.NouvelObjet(1, 230,230, 2)
obstacles.NouvelObjet(1, 260,230, 2)
obstacles.NouvelObjet(1, 200,230, 2)
obstacles.NouvelObjet(1, 260,230, 2)
obstacles.NouvelObjet(1, 260,260, 2)
obstacles.NouvelObjet(1, 260,290, 2)
obstacles.NouvelObjet(1, 60,90, 2)



#Rafraîchissement de l'écran
pygame.display.flip()

#Maintiend des touches
pygame.key.set_repeat(2, 10)

#Nombre de frames par secondes
pygame.time.Clock().tick(3)

#BOUCLE INFINIE
continuer = 1
while continuer:
	for event in pygame.event.get():	#Attente des événements
		
		if event.type == QUIT:
			continuer = 0
		if event.type == KEYDOWN:
			if event.key == K_DOWN:
			     if cub.position.bottom <= 500 and not obstacles.ColisionsCube(cub.hitbox.move(0,3)):
				cub.position = cub.position.move(0,3)
				cub.hitbox = cub.hitbox.move(0,3)
			if event.key == K_UP:
			    if cub.position.top >= 20 and not obstacles.ColisionsCube(cub.hitbox.move(0,-3)):
				cub.position = cub.position.move(0,-3)
				cub.hitbox = cub.hitbox.move(0,-3)
			if event.key == K_LEFT:
			     if cub.position.left >= -15 and not obstacles.ColisionsCube(cub.hitbox.move(-3,0)):
				cub.position = cub.position.move(-3,0)
				cub.hitbox = cub.hitbox.move(-3,0)
			if event.key == K_RIGHT:
			     if cub.position.right <= 655 and not obstacles.ColisionsCube(cub.hitbox.move(3,0)):
				cub.position = cub.position.move(3,0)
				cub.hitbox = cub.hitbox.move(3,0)
			    
	key = pygame.key.get_pressed()
	if key[303] == True or key[304] == True:
		if k >= 20:
		    tir2.positions.append(Rect(0,0,20,50).move(cub.position.left + 25, cub.position.top))
		    k = 0
		k += 1
	elif key[306] == True or key[305] == True:
		if k >= 15:
		    tir1.positions.append(Rect(0,0,20,30).move(cub.position.left + 30, cub.position.top))
		    k = 0
		k += 1
	g += 1
	
	#Test des colisions avec les obstacles
	tir1.positions = obstacles.ColisionsTir(tir1.positions)
	tir2.positions = obstacles.ColisionsTir(tir2.positions)
	
	#Scrool
	j += 1
	if j > 15:
	    if scrool.top < 0:
		scrool = scrool.move(0,1)
	    j = 0
	    avancement += 1
	
	print obstacles.mur.get_rect()
	
	
	#Avance des attaques et des ondes
	tir1.Progression()
	tir2.Progression()
	onde.Progression()
	
	#Rotation du cube
	cub.rotation()
	
	#Scrool des obstacles
	obstacles.Scrool(cub.position)
	if obstacles.ColisionsCube(cub.hitbox) == True:
	    cub.position = cub.position.move(0,1)
	    cub.hitbox = cub.hitbox.move(0,1)
	
	#Re-collage
	fenetre.blit(fond, scrool)	
	tir1.Affichage(fenetre)
	tir2.Affichage(fenetre)
	onde.Affichage(fenetre)
		
	cub.Affichage(fenetre)
	
	
	#Affichage des murs
	obstacles.Affichage(fenetre)
	
	
	#Rafraichissement
	pygame.display.flip()
	
	
	#Survie
	if cub.position.top < 0:
	    continuer = 0
	if cub.position.top > 490:
	    continuer = 0
	
	#Son
	repeter = pygame.time.get_ticks() % 157000
	if repeter > 100000:
	    repet = 0
	if repeter > 0 and repeter < 100 and repet == 0:
	    son = pygame.mixer.Sound("son/son_stressant.wav")
	    son.play()
	    repet = 1
	    
	




