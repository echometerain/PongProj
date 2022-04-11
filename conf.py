############################
# Filename: conf.py
# Desc: Global configuration
# Date created: 04/02/2022
############################

import pygame as pg

RED = 255,0,0 # list colors
WHITE = 255,255,255
BLACK = 0,0,0
BLUE = 130, 238, 253

sWidth = 400 # screen width and height
sHeight = 300

pg.init() # starts pygame and functions
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
FPS = 25
difficulty = 4			# lower = more difficult
BInc = 1/difficulty		# ball percent increase

Bcolor = RED		# ball colorRcolor = WHITE
Rcolor = [WHITE, WHITE]		# rect colors
PhyDelay = 1000//FPS	# physics delay (game speed)
score = [0,0]

scoreSize = sWidth//20				# score font size
scoreX = [sWidth/4, sWidth*3/4]		# scoreboard x position
scoreY = sHeight/8					# scoreboard y
overScore = 7						# max score

# gun section
Glong = sWidth/40					# bullet length
Ghigh = sHeight/40					# bullet height
Gspeed = sWidth/2000				# bullet speed
Gcolor = RED						# bullet color
deadTime = 2

font = pg.font.Font('font.ttf', scoreSize)
Lfont = pg.font.Font('font.ttf', scoreSize*3) # large font

pg.mixer.music.load("Parking Lot.ogg") # play music
pg.mixer.music.play(-1)	# loop music

settingPage = False #initializes settingPage as False
gamePage = True #initializes gamePage as True

menuRect1W = sWidth/2 #sets the value menuRect1W as 1/2 the width of the screen
menuRect1H = sHeight/3 #sets the value of menuRect1H as a 1/3 of the height of the screen
menuRect1X = sHeight/16 #sets the value menuRect1X as a 1/16 of the height of the screen
menuRect1Y = sWidth/4 #sets the value of menuRect1Y as a 1/4 of the width of the screen
outline = 0 #the outlines of the rectangles are 0
rectColour = WHITE 
settingPageFontSize = sHeight/6
menuRect2X = sWidth/16 #sets the height of the rectangles on the setting page to a 1/16 of the screen's height
menuRect2Y = sHeight/4 #sets the width of the rectangles on the setting page to a 1/4 of the width of the screen
leftRectX = sWidth/32 #sets the gap from the end of the screen to the rectangle to 1/32 of the screen
bottomRectY = sHeight - sHeight/8 #sets the location of the bottom two rectangles
bottomRect2Y = sHeight - sHeight/4 - sHeight/16 #sets the location of the middle two rectangles
bottomRect3Y = sHeight - sHeight/2 #sets the location of the top two rectangles
settingFont = pg.font.SysFont("CROCHET PATTERN", 60) #sets the font and font size of the font on the settings page