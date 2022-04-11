############################
# Filename: ball.py
# Desc: Ball, laser movement and collision implementation
# Date created: 04/03/2022
############################

from conf import sWidth, sHeight, BSpeed, screen, Bcolor, BallR, BallOL, PhyDelay, Rwide, Rhigh, RectX, RectY, score, deadTime, BInc
import pygame as pg
from gun import clear
from rect import reset
import random
import time

set()

def isdead(): # whether the ball is allowed to move or not
	if time.time()-dead < deadTime:
		return True
	return False

def touchRect0(tmpX, tmpY): # check if ball touch paddle 0
	if (tmpX<RectX[0]+Rhigh+BallR and tmpX>RectX[0]-BallR and tmpY>RectY[0] and tmpY<RectY[0]+Rwide):
		return True
	return False
def touchRect1(tmpX, tmpY): # check if ball touch paddle 1
	if (tmpX>RectX[1]-BallR and tmpX<RectX[1]+Rhigh+BallR and tmpY>RectY[1] and tmpY<RectY[1]+Rwide):
		return True
	return False

def touchBall(tmpX, tmpY): # check if cordinate touches ball
	if BallR*BallR >= (X-tmpX)*(X-tmpX) + (Y-tmpY)*(Y-tmpY):
		return True
	return False

def moveBall(speed): # moves ball
	global X
	global Y
	global moveX
	global moveY
	global dead

	def draw(): # draw ball
		pg.draw.circle(screen, Bcolor, (X, Y), BallR, BallOL)
	if isdead():
		draw()
		return
	if X > sWidth+BallR: # check if offscreen
		score[0]+=1
		set()
	if X < -BallR:
		score[1]+=1
		set()
	elif touchRect0(X, Y): # check if ball touch paddle 0
		X = RectX[0]+Rhigh+BallR
		moveX = random.uniform(-moveX*(1+BInc), -moveX*(1-BInc/2))
	elif touchRect1(X, Y): # check if ball touch paddle 1
		X = RectX[1]-BallR
		moveX = random.uniform(-moveX*(1+BInc), -moveX*(1-BInc/2))
	if Y > sHeight - BallR or Y < BallR: # check if ball touch ceiling
		if Y > sHeight - BallR:
			Y = sHeight - BallR
		elif Y < BallR:
			Y = BallR
		moveY = random.uniform(-moveY*(1+BInc), -moveY*(1-BInc/2))
	X += (moveX*speed) * PhyDelay # change speed
	Y += (moveY*speed) * PhyDelay
	draw()

def set(): # reset ball position
	global X
	global Y
	global moveX
	global moveY
	global dead		# the ball isn't allowed to move a certain amount of time after someone loses
	
	moveX = BSpeed if random.randint(0, 1) else -BSpeed
	moveY = BSpeed if random.randint(0, 1) else -BSpeed
	X=sWidth/2
	Y=sHeight/2
	dead = time.time()
	clear()
	reset()
	