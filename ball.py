############################
# Filename: ball.py
# Desc: Ball, laser movement and collision implementation
# Date created: 04/03/2022
############################

from conf import sWidth, sHeight, BSpeed, screen, Bcolor, BallR, BallOL, PhyDelay, Rwide, Rhigh, RectX, RectY, score
import pygame as pg
from rect import reset
import random
import time

set()

def touchRect(tmpX, tmpY):
	if (tmpX<RectX[0]+Rhigh+BallR and tmpX>RectX[0]-BallR and tmpY>RectY[0] and tmpY<RectY[0]+Rwide and moveX<0) \
	or (tmpX>RectX[1]-BallR and tmpX<RectX[1]+Rhigh+BallR and tmpY>RectY[1] and tmpY<RectY[1]+Rwide and moveX>0):
		return True
	return False

def touchBall(tmpX, tmpY):
	if BallR*BallR >= (X-tmpX)*(X-tmpX) + (Y-tmpY)*(Y-tmpY):
		return True
	return False

def moveBall(speed):
	global X
	global Y
	global moveX
	global moveY
	global dead

	def draw():
		pg.draw.circle(screen, Bcolor, (X, Y), BallR, BallOL)
	if time.time()-dead < 3:
		draw()
		return
	if X > sWidth+BallR:
		score[0]+=1
		set()
	if X < -BallR:
		score[1]+=1
		set()
	elif touchRect(X, Y):
		if X<RectX[0]+Rhigh+BallR:
			X = RectX[0]+Rhigh+BallR
		elif X>RectX[1]-BallR:
			X = RectX[1]-BallR
		moveX = random.uniform(-moveX*5/4, -moveX*7/8)
	if Y > sHeight - BallR or Y < BallR:
		if Y > sHeight - BallR:
			Y = sHeight - BallR
		elif Y < BallR:
			Y = BallR
		moveY = random.uniform(-moveY*5/4, -moveY*7/8)
	X += (moveX*speed) * PhyDelay
	Y += (moveY*speed) * PhyDelay
	draw()

def set():
	global X
	global Y
	global moveX
	global moveY
	global dead
	
	moveX = BSpeed if random.randint(0, 1) else -BSpeed
	moveY = BSpeed if random.randint(0, 1) else -BSpeed
	X=sWidth/2
	Y=sHeight/2
	dead = time.time()
	reset()
	