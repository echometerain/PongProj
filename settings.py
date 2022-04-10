import pygame
import pygame as pg
from conf import screen, sHeight, sWidth, BLACK, WHITE, RED, BLUE, settingFont, settingPage, settingPageFontSize, menuRect1H, menuRect1W, menuRect1X, menuRect1Y, menuRect2X, menuRect2Y, font, leftRectX, bottomRectY, bottomRect2Y, bottomRect3Y, outline
mouseX = 0
mouseY = 0
mouse2Y = 0
R1color = WHITE
R2color = WHITE
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
	mouseX, mouseY = pg.mouse.get_pos()
	for event in pg.event.get():
		if event.type == pg.MOUSEMOTION:
			mouseX, mouseY = pg.mouse.get_pos()
			print( "Current mouse location: ", mouseX, mouseY, bottomRectY, bottomRectY + menuRect2X)
	if mouseY > bottomRectY and mouseY < bottomRectY + menuRect2X:
		pg.draw.rect(screen, RED, (sWidth - leftRectX - menuRect2Y, bottomRectY, menuRect2Y, menuRect2X), outline)
		Rcolor = RED
	keys = pg.key.get_pressed()
	if keys[pg.K_l]:
		gamePage = True
		settingPage = False
		R1color = RED
		R2color = RED
		#True