############################
# Filename: main.py
# Desc: Main game loop
# Date created: 03/31/2022
############################

from conf import BLACK, WHITE, screen, PhyDelay, font, score, scoreX, scoreY, Lfont, sWidth, sHeight, overScore, settingPage, Rwide, RectX, RectY
from settings import settings
from ball import moveBall, set as setBall, isdead
from rect import moveRect, reset, draw
from gun import delta, gun, addGun, clear
import pygame as pg
import sys
import time

R1color = WHITE
R2color = WHITE
gtime0 = time.time() # gun time delay for paddle 0
gtime1 = time.time() # gun time delay for paddle 1

def Key(): # handles key strokes
	global gtime0
	global gtime1
	keys = pg.key.get_pressed()
	if not (keys[pg.K_s] and keys[pg.K_w]): # paddle 0 key strokes
		if keys[pg.K_w]:
			moveRect(0, "u")
		elif keys[pg.K_s]:
			moveRect(0, "d")
	if not (keys[pg.K_UP] and keys[pg.K_DOWN]): # paddle 1 key strokes
		if keys[pg.K_DOWN]:
			moveRect(1, "d")
		elif keys[pg.K_UP]:
			moveRect(1, "u")
	if not isdead(): # gun keystrokes
		if keys[pg.K_d] and time.time()-gtime0 > 2 :
			addGun(gun(RectX[0], RectY[0]+Rwide/2, 0))
			gtime0 = time.time()
		if keys[pg.K_LEFT] and time.time()-gtime1 > 2:
			addGun(gun(RectX[1], RectY[1]+Rwide/2, 1))
			gtime1 = time.time()
def next(over): # updates frame
	pg.display.update()
	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			sys.exit()
			exit(0)
	pg.event.clear()
	pg.time.delay(PhyDelay)
	if over:
		screen.blit(Lfont.render("GAME OVER", True, WHITE, BLACK), (sWidth*11//64, sHeight*3//8))
	else:
		screen.fill(BLACK)

def anyKey(): # press any key to continue
	pg.display.update()
	while True:
		for event in pg.event.get():
			if event.type == pg.KEYDOWN:
				return
		pg.time.delay(PhyDelay)


screen.fill(BLACK) # splash screen
screen.blit(Lfont.render("PLAY PONG", True, WHITE, BLACK), (sWidth*11//64, sHeight*3//8))
screen.blit(font.render("Press any key...", True, WHITE, BLACK), (sWidth*5//16, sHeight*5//8))
anyKey()
setBall()

gamePage=True
while True: 
	while settingPage: #only happens while the settingPage is True
		next() #calls the next function
		settings() #calls the setting page
		keys = pg.key.get_pressed() #checks to see if any keys are pressed
		if keys[pg.K_l]: #only happens if 'l' is pressed
			draw() #call draw function
			gamePage = True #makes gamePage True
			settingPage = False #makes settingPage False
			
	while gamePage: # pong game loop
		score0 = font.render(str(score[0]), True, WHITE, BLACK) # renders scoreboard
		score1 = font.render(str(score[1]), True, WHITE, BLACK)
		screen.blit(score0, (scoreX[0], scoreY))
		screen.blit(score1, (scoreX[1], scoreY))
		if score[0] >= overScore or score[1] >= overScore: # handle game over
			next(True)
			anyKey()
			score[0] = 0
			score[1] = 0
			next(False)
			reset()
			setBall()
			clear()
			continue
	
		Key()
		moveRect(0, "N/A")
		moveBall(1)
		delta()
		next(False)
		keys = pg.key.get_pressed() #checks to see if any keys are pressed
		if keys[pg.K_h]: #happens if the 'h' key is pressed
			gamePage = False #makes the gamePage False
			settingPage = True #makes the settingPage True
pg.quit()
sys.exit()