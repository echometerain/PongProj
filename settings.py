import pygame
import pygame as pg
from conf import screen, sHeight, sWidth, BLACK, WHITE, RED, BLUE, settingFont, settingPage, settingPageFontSize, menuRect1H, menuRect1W, menuRect1X, menuRect1Y, menuRect2X, menuRect2Y, font, leftRectX, bottomRectY, bottomRect2Y, bottomRect3Y, outline
mouseX = 0
mouseY = 0
def settings():
	pg.display.update()
	screen.fill(BLACK)
	graphics = font.render("Pong Setting Page", True, WHITE)
	screen.blit(graphics, (menuRect1Y, menuRect1X))
	pg.draw.rect(screen, WHITE, (leftRectX, bottomRectY, menuRect2Y, menuRect2X), outline)
	pg.draw.rect(screen, RED, (leftRectX, bottomRect2Y, menuRect2Y, menuRect2X), outline)
	pg.draw.rect(screen, BLUE, (leftRectX, bottomRect3Y, menuRect2Y, menuRect2X), outline)
	pg.draw.rect(screen, WHITE, (sWidth - leftRectX - menuRect2Y, bottomRectY, menuRect2Y, menuRect2X), outline)
	pg.draw.rect(screen, RED, (sWidth - leftRectX - menuRect2Y, bottomRect2Y, menuRect2Y, menuRect2X), outline)
	pg.draw.rect(screen, BLUE, (sWidth - leftRectX - menuRect2Y, bottomRect3Y, menuRect2Y, menuRect2X), outline)
	for event in pg.event.get():
		if event.type == pg.MOUSEMOTION:
			mouseX, mousePosY = pg.mouse.get_pos()
	if mouseY > bottomRectY and mouseY < bottomRectY + menuRect2X:
		True