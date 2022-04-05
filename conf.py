import pygame as pg

RED = 255,0,0
WHITE = 255,255,255
BLACK = 0,0,0

sWidth = 600          # screen width
sHeight = 400         # screen height

screen = pg.display.set_mode((sWidth,sHeight))
pg.display.set_caption("Pong!")
pg.font.init()

BallOL = 0            # ball outline
BallR = sWidth/60     # ball radius

RectOL = 0            # rect outline
BSpeed = sWidth/4000          # ball speed
RSpeed = sWidth/2000          # rect speed
Rwide = sHeight/5     # rect width
Rhigh = sWidth/40     # rect height
RectX = [sWidth/8, sWidth*7/8]    # rect start x
RectY = [sHeight/2 - Rwide/2, sHeight/2 - Rwide/2]
# rect start y

Bcolor = RED          # ball colorRcolor = WHITE
Rcolor = WHITE        # rect color
PhyDelay = 40         # physics delay (game speed)
score = [0,0]

scoreSize = sWidth//20
scoreX = [sWidth/4, sWidth*3/4]
scoreY = sHeight/8
overScore = 1

font = pg.font.Font('font.ttf', scoreSize)
Lfont = pg.font.Font('font.ttf', scoreSize*3)