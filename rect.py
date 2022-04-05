from conf import RectOL, RSpeed, Rcolor, screen, sHeight, PhyDelay, Rhigh, Rwide, RectX as X, RectY as Y
import pygame as pg

move = [RSpeed, RSpeed]

def moveRect(id, dir, speed):
    global move
    
    def draw():
        pg.draw.rect(screen, Rcolor, (X[0],Y[0], Rhigh,Rwide), RectOL)
        pg.draw.rect(screen, Rcolor, (X[1],Y[1], Rhigh,Rwide), RectOL)
    if speed == 0:
        draw()
        return
    if dir == "u" and Y[id] > 0:
        Y[id] -= move[id] * PhyDelay * speed
    elif dir == "d" and Y[id] < sHeight-Rwide:
        Y[id] += move[id] * PhyDelay * speed
    draw()

def reset():
    Y[0] = sHeight/2 - Rwide/2
    Y[1] = sHeight/2 - Rwide/2