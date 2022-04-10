############################
# Filename: main.py
# Desc: Main game loop
# Date created: 03/31/2022
############################

from conf import BLACK, WHITE, RED, screen, PhyDelay, font, score, scoreX, scoreY, Lfont, sWidth, sHeight, overScore, settingPage, gamePage, Rwide, RectX, RectY
from settings import settings
<<<<<<< HEAD
<<<<<<< HEAD
from ball import moveBall, set as setBall
from rect import moveRect, reset, draw
from gun import delta, gun, addGun
=======
from ball import moveBall, set as setBall, isdead
from rect import moveRect, reset
from gun import delta, gun, addGun, clear
>>>>>>> 1d8cdcb2d1b1cef2c06aaf18495197b1f860fa05
||||||| 27f5486
from ball import moveBall, set as setBall
from rect import moveRect, reset
from gun import delta, gun, addGun
=======
from ball import moveBall, set as setBall, isdead
from rect import moveRect, reset
from gun import delta, gun, addGun, clear
>>>>>>> 1d8cdcb2d1b1cef2c06aaf18495197b1f860fa05
import pygame as pg
import sys
import time

<<<<<<< HEAD
<<<<<<< HEAD
R1color = WHITE
R2color = WHITE
guntime = time.time()
=======
gtime0 = time.time()
gtime1 = time.time()
>>>>>>> 1d8cdcb2d1b1cef2c06aaf18495197b1f860fa05
||||||| 27f5486
guntime = time.time()
=======
gtime0 = time.time()
gtime1 = time.time()
>>>>>>> 1d8cdcb2d1b1cef2c06aaf18495197b1f860fa05

def Key():
	global gtime0
	global gtime1
	keys = pg.key.get_pressed()
	if not (keys[pg.K_s] and keys[pg.K_w]):
		if keys[pg.K_w]:
			moveRect(0, "u")
		elif keys[pg.K_s]:
			moveRect(0, "d")
	if not (keys[pg.K_UP] and keys[pg.K_DOWN]):
		if keys[pg.K_DOWN]:
			moveRect(1, "d")
		elif keys[pg.K_UP]:
			moveRect(1, "u")
	if not isdead():
		if keys[pg.K_d] and time.time()-gtime0 > 2 :
			addGun(gun(RectX[0], RectY[0]+Rwide/2, 0))
			gtime0 = time.time()
		if keys[pg.K_LEFT] and time.time()-gtime1 > 2:
			addGun(gun(RectX[1], RectY[1]+Rwide/2, 1))
			gtime1 = time.time()
def next():
	pg.display.update()
	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			sys.exit()
			exit(0)
	pg.event.clear()
	pg.time.delay(PhyDelay)
	screen.fill(BLACK)

def anyKey():
	pg.display.update()
	while True:
		for event in pg.event.get():
			if event.type == pg.KEYDOWN:
				return
		pg.time.delay(PhyDelay)


screen.fill(BLACK)
screen.blit(Lfont.render("PLAY PONG", True, WHITE, BLACK), (sWidth*11//64, sHeight*3//8))
screen.blit(font.render("Press any key...", True, WHITE, BLACK), (sWidth*5//16, sHeight*5//8))
anyKey()
setBall()

while True: 
	while settingPage:
		#next()
		settings()
		keys = pg.key.get_pressed()
		if keys[pg.K_l]:
			Rcolor = RED
			draw()
			gamePage = True
			settingPage = False
			
	while gamePage:
		score0 = font.render(str(score[0]), True, WHITE, BLACK)
		score1 = font.render(str(score[1]), True, WHITE, BLACK)
		screen.blit(score0, (scoreX[0], scoreY))
		screen.blit(score1, (scoreX[1], scoreY))
		if score[0] >= overScore or score[1] >= overScore:
			screen.blit(Lfont.render("GAME OVER", True, WHITE, BLACK), (sWidth*11//64, sHeight*3//8))
			anyKey()
			score[0] = 0
			score[1] = 0
			next()
			reset()
			setBall()
			clear()
			continue
	
		Key()
		moveRect(0, "N/A")
		moveBall(1)
		delta()
		next()
		keys = pg.key.get_pressed()
		if keys[pg.K_h]:
			gamePage = False
			settingPage = True
pg.quit()
sys.exit()