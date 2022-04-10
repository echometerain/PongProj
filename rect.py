############################
# Filename: rect.py
# Desc: Paddle movement implementation
# Date created: 04/03/2022
############################

<<<<<<< HEAD
from conf import RectOL, RSpeed, Rcolor, screen, sHeight, PhyDelay, Rhigh, Rwide, RectX as X, RectY as Y, RED
<<<<<<< HEAD
from settings import R1color, R2color
=======
>>>>>>> 1d8cdcb2d1b1cef2c06aaf18495197b1f860fa05
||||||| 27f5486
from conf import RectOL, RSpeed, Rcolor, screen, sHeight, PhyDelay, Rhigh, Rwide, RectX as X, RectY as Y
=======
from conf import RectOL, RSpeed, Rcolor, screen, sHeight, PhyDelay, Rhigh, Rwide, RectX as X, RectY as Y, RED
>>>>>>> 1d8cdcb2d1b1cef2c06aaf18495197b1f860fa05
import pygame as pg

move = [RSpeed, RSpeed]

<<<<<<< HEAD
def draw():
	pg.draw.rect(screen, R1color, (X[0],Y[0], Rhigh,Rwide), RectOL)
	pg.draw.rect(screen, R2color, (X[1],Y[1], Rhigh,Rwide), RectOL)
=======
def moveRect(id, dir):
	global move
	def draw():
		pg.draw.rect(screen, Rcolor, (X[0],Y[0], Rhigh,Rwide), RectOL)
		pg.draw.rect(screen, Rcolor, (X[1],Y[1], Rhigh,Rwide), RectOL)
>>>>>>> 1d8cdcb2d1b1cef2c06aaf18495197b1f860fa05
	if dir == "u" and Y[id] > 0:
		Y[id] -= move[id] * PhyDelay
	elif dir == "d" and Y[id] < sHeight-Rwide:
		Y[id] += move[id] * PhyDelay
	print("draw()", R1color, R2color)

def moveRect(id, dir):
	global move
	
	draw()

def reset():
	global move
	
	Y[0] = sHeight/2 - Rwide/2
	Y[1] = sHeight/2 - Rwide/2
	move = [RSpeed, RSpeed]