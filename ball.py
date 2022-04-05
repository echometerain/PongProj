from conf import sWidth, sHeight, BSpeed, screen, Bcolor, BallR, BallOL, PhyDelay, Rwide, Rhigh, RectX, RectY, score
import pygame as pg
import random
import time

moveX = BSpeed if random.randint(0, 1) else -BSpeed
moveY = BSpeed if random.randint(0, 1) else -BSpeed
X=sWidth/2
Y=sHeight/2
dead = time.time()

def moveBall(speed):
    global X
    global Y
    global moveX
    global moveY
    global dead
    def draw():
        pg.draw.circle(screen, Bcolor, (X, Y), BallR, BallOL)
    
    if time.time()-dead < 3:
        draw()
        return
    if X > sWidth+BallR:
        score[0]+=1
        set()
    if X < -BallR:
        score[1]+=1
        set()
    elif (X<RectX[0]+Rhigh+BallR and X>RectX[0]-BallR and Y>RectY[0] and Y<RectY[0]+Rwide and moveX<0) \
    or (X>RectX[1]-BallR and X<RectX[1]+Rhigh+BallR and Y>RectY[1] and Y<RectY[1]+Rwide and moveX>0):
        if X<RectX[0]+Rhigh+BallR:
            X = RectX[0]+Rhigh+BallR
        elif X>RectX[1]-BallR:
            X = RectX[1]-BallR
        moveX = random.uniform(-moveX*5/4, -moveX*7/8)
    if Y > sHeight - BallR or Y < BallR:
        if Y > sHeight - BallR:
            Y = sHeight - BallR
        elif Y < BallR:
            Y = BallR
        moveY = random.uniform(-moveY*5/4, -moveY*7/8)
    X += (moveX*speed) * PhyDelay
    Y += (moveY*speed) * PhyDelay
    draw()

def set():
    global X
    global Y
    global moveX
    global moveY
    global dead
    
    moveX = BSpeed if random.randint(0, 1) else -BSpeed
    moveY = BSpeed if random.randint(0, 1) else -BSpeed
    X=sWidth/2
    Y=sHeight/2
    dead = time.time()