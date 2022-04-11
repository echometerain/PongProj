############################
# Filename: rect.py
# Desc: Paddle movement implementation
# Date created: 04/03/2022
############################

from conf import RectOL, RSpeed, Rcolor, screen, sHeight, PhyDelay, Rhigh, Rwide, RectX as X, RectY as Y
import pygame as pg

# paddle 0 is left paddle, paddle 1 is right paddle

move = [RSpeed, RSpeed] # y speed for paddle 0 & 1

def draw(): # draws paddle
	pg.draw.rect(screen, Rcolor[0], (X[0],Y[0], Rhigh,Rwide), RectOL)
	pg.draw.rect(screen, Rcolor[1], (X[1],Y[1], Rhigh,Rwide), RectOL)
	
def moveRect(id, dir): # calculates paddle movement
	global move
	if dir == "u" and Y[id] > 0:
		Y[id] -= move[id] * PhyDelay
	elif dir == "d" and Y[id] < sHeight-Rwide:
		Y[id] += move[id] * PhyDelay
	draw()

def reset(): # reset paddle position
	global move
	Y[0] = sHeight/2 - Rwide/2 # paddle 0 y position
	Y[1] = sHeight/2 - Rwide/2 # paddle 1 y position
	move = [RSpeed, RSpeed]