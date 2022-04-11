############################
# Filename: gun.py
# Desc: Blaster implementation
# Function: when gun hits paddle, paddle speed/2. when gun hits ball, ball bounce
# Date created: 04/06/2022
############################
import ball
import rect
import conf
import random
import pygame as pg
gunList = [] # list of bullets

def addGun(g): # add bullet
	global gunList
	gunList.append(g)

def delta(): # renders all bullets (named after the godot func)
	global gunList
	for item in gunList:
		item.move()

class gun(): # oop yay
	def __init__(self, x, y, fr): # create bullet
		self.x = x
		self.y = y
		self.fr = fr # from paddle #
	def move(self): # move bullet
		global gunList
		if self.fr == 0: # handle paddle hit
			if ball.touchRect1(self.x+conf.Glong, self.y+conf.Ghigh/2):
				rect.move[1] /= 2
				gunList.remove(self)
				del self
				return
		else:
			if ball.touchRect0(self.x+conf.Glong, self.y+conf.Ghigh/2):
				rect.move[0] /= 2
				gunList.remove(self)
				del self
				return
		if ball.touchBall(self.x+conf.Glong, self.y+conf.Ghigh/2): # handle ball hit
			ball.moveX = random.uniform(ball.moveX*(1+conf.BInc*2), ball.moveX)
			if ball.moveX > 0:
				if self.fr == 1:
					ball.moveX *= -1
			else:
				if self.fr == 0:
					ball.moveX *= -1
			gunList.remove(self)
			del self
		elif self.x > conf.sWidth or self.x < 0 or self.y > conf.sHeight or self.y < 0: # handle go offscreen
			gunList.remove(self)
			del self
		else: # move bullets
			if self.fr == 0:
				self.x += conf.Gspeed * conf.PhyDelay
			else:
				self.x -= conf.Gspeed * conf.PhyDelay
			pg.draw.rect(conf.screen, conf.Gcolor, (self.x,self.y, conf.Glong,conf.Ghigh), 0)
def clear(): # reset bullets
	global gunList
	for item in gunList:
		del item
	gunList = []