############################
# Filename: conf.py
# Desc: Global configuration
# Date created: 04/02/2022
############################

import pygame as pg
from settings import R1color, R2color

RED = 255,0,0
WHITE = 255,255,255
BLACK = 0,0,0
BLUE = 130, 238, 253

sWidth = 400
sHeight = 300

pg.init()
screen = pg.display.set_mode((sWidth,sHeight))
pg.display.set_caption("Pong!")
pg.font.init()
pg.mixer.init()

BallOL = 0				# ball outline
BallR = sWidth/60	 	# ball radius

RectOL = 0				# rect outline
BSpeed = sWidth/4000	# ball speed
RSpeed = sWidth/2000	# rect speed
Rwide = sHeight/5		# rect width
Rhigh = sWidth/40		# rect height
RectX = [sWidth/8, sWidth*7/8]		# rect start x
RectY = [sHeight/2 - Rwide/2, sHeight/2 - Rwide/2]
# rect start y

Bcolor = RED		# ball colorRcolor = WHITE
Rcolor = WHITE		# rect color
PhyDelay = 40		# physics delay (game speed)
score = [0,0]

scoreSize = sWidth//20				# score font size
scoreX = [sWidth/4, sWidth*3/4]		# scoreboard x position
scoreY = sHeight/8					# scoreboard y
overScore = 7						# max score

Glong = sWidth/40
Ghigh = sHeight/40
Gspeed = sWidth/4000
Gcolor = RED

font = pg.font.Font('font.ttf', scoreSize)
Lfont = pg.font.Font('font.ttf', scoreSize*3)

pg.mixer.music.load("Parking Lot.ogg")
pg.mixer.music.play(-1)

settingPage = False
gamePage = True

menuRect1W = sWidth/2
menuRect1H = sHeight/3
menuRect1X = sHeight/16
menuRect1Y = sWidth/4
outline = 0
rectColour = WHITE
settingPageFontSize = sHeight/6
menuRect2X = sWidth/16
menuRect2Y = sHeight/4
leftRectX = sWidth/32
bottomRectY = sHeight - sHeight/8
bottomRect2Y = sHeight - sHeight/4 - sHeight/16
bottomRect3Y = sHeight - sHeight/2
settingPageFontSize = sHeight/6
settingFont = pg.font.SysFont("CROCHET PATTERN", 60)

R1color