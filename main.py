############################
# Filename: main.py
# Desc: Main game loop
# Date created: 03/31/2022
############################

from conf import BLACK, WHITE, RED, screen, PhyDelay, font, score, scoreX, scoreY, Lfont, sWidth, sHeight, overScore, settingPage, gamePage, Rwide, RectX, RectY
from settings import settings
from ball import moveBall, set as setBall
from rect import moveRect, reset, draw
from gun import delta, gun, addGun
import pygame as pg
import sys
import time

R1color = WHITE
R2color = WHITE
guntime = time.time()

def Key():
	global guntime
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
	if time.time()-guntime > 2:
		if keys[pg.K_d]:
			addGun(gun(RectX[0], RectY[0]+Rwide/2, 0))
			guntime = time.time()
		if keys[pg.K_LEFT]:
			addGun(gun(RectX[1], RectY[1]+Rwide/2, 1))
			guntime = time.time()
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