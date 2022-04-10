############################
# Filename: gun.py
# Desc: blaster implementation
# Date created: 04/06/2022
############################
import ball
import rect
import conf
import random
import pygame as pg
gunList = []

def addGun(g):
	global gunList
	gunList.append(g)

def delta():
	global gunList
	for item in gunList:
		item.move()

class gun():
	def __init__(self, x, y, fr):
		self.x = x
		self.y = y
		self.fr = fr #from
	def move(self):
		global gunList
		if self.fr == 0:
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
		if ball.touchBall(self.x+conf.Glong, self.y+conf.Ghigh/2):
			ball.moveX = random.uniform(-ball.moveX*5/4, -ball.moveX*7/8)
			gunList.remove(self)
			del self
		elif self.x > conf.sWidth or self.x < 0 or self.y > conf.sHeight or self.y < 0:
			gunList.remove(self)
			del self
		else:
			if self.fr == 0:
				self.x += conf.Gspeed * conf.PhyDelay
			else:
				self.x -= conf.Gspeed * conf.PhyDelay
			pg.draw.rect(conf.screen, conf.Gcolor, (self.x,self.y, conf.Glong,conf.Ghigh), 0)
def clear():
	global gunList
	for item in gunList:
		del item
	gunList = []