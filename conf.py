import pygame as pg

RED = 255,0,0
WHITE = 255,255,255
BLACK = 0,0,0

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

font = pg.font.Font('font.ttf', scoreSize)
Lfont = pg.font.Font('font.ttf', scoreSize*3)

pg.mixer.music.load("Parking Lot.ogg")
pg.mixer.music.play(-1)

settingPage = False