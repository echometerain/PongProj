from conf import BLACK, WHITE, screen, PhyDelay, font, score, scoreX, scoreY, Lfont, sWidth, sHeight, overScore
from ball import moveBall, set as setBall
from rect import moveRect, reset
import pygame as pg
import sys
pg.init()

def rectKey():
    keys = pg.key.get_pressed()
    if not (keys[pg.K_s] and keys[pg.K_w]):
        if keys[pg.K_w]:
            moveRect(0, "u", 1)
        elif keys[pg.K_s]:
            moveRect(0, "d", 1)
    if not (keys[pg.K_UP] and keys[pg.K_DOWN]):
        if keys[pg.K_DOWN]:
            moveRect(1, "d", 1)
        elif keys[pg.K_UP]:
            moveRect(1, "u", 1)
def next():
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
            exit(0)
    pg.event.clear()
    pg.time.delay(PhyDelay)

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
    screen.fill(BLACK)
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
    
    rectKey()
    moveRect(0, 0, 0)
    moveBall(1)
    next()
    
pg.quit()
sys.exit()