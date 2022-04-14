############################
# Filename: settings.py
# Desc: Settings page
# Date created: 04/8/2022
############################

import pygame
import pygame as pg
from conf import screen, sWidth, BLACK, WHITE, RED, BLUE, menuRect1X, menuRect1Y, menuRect2X, menuRect2Y, font, leftRectX, bottomRectY, bottomRect2Y, bottomRect3Y, outline, Rcolor, difficulty
mouseX = 0 #The X value of the mouse is set to 0
mouseY = 0 #The Y value of the mouse is set to 0
def settings():
	pg.display.update()
	screen.fill(BLACK) #Makes the background black
	graphics = font.render("Pong Setting Page", True, WHITE) #Defines graphics as the rendering of "Pong Setting Page"
	graphics2 = font.render("Player 1", True, WHITE) #Defines graphics2 as the rendering of "Player 1"
	graphics3 = font.render("Player 2", True, WHITE) #Defines graphics3 as the rendering of "Player 2"
	graphics4 = font.render("Press 'l' to return", True, WHITE) #Defines graphics4 as the rendering of "Press 'l' to return"
	graphics5 = font.render("to game", True, WHITE) #Defines graphics5 as the rendering of "to game"
	graphics6 = font.render("difficulty", True, WHITE) #Defines graphics6 as the rendering of "difficulty"
	graphics7 = font.render("Easy", True, WHITE) #Defines graphics7 as the rendering of "Easy"
	graphics8 = font.render("Medium", True, WHITE) #Defines graphics8 as the rendering of "Medium"
	graphics9 = font.render("Hard", True, WHITE) #Defines graphics9 as the rendering of "Hard"
	graphics10 = font.render("Very Hard", True, WHITE) #Defines graphics10 as the rendering of "Very Hard"
	graphics11 = font.render("Easy", True, RED) #Defines graphics11 as the rendering of "Easy" in red
	graphics12 = font.render("Medium", True, RED) #Defines graphics12 as the rendering of "Medium" in red
	graphics13 = font.render("Hard", True, RED) #Defines graphics13 as the rendering of "Hard" in red
	graphics14 = font.render("Very Hard", True, RED) #Defines graphics14 as the rendering of "Very Hard" in red
	screen.blit(graphics, (menuRect1Y, menuRect1X)) #Renders "Pong Setting Page" at the top center of the screen
	screen.blit(graphics2, (leftRectX, bottomRect3Y - sWidth/16)) #Renders "Player 1" at the left of the screen above the blue rectangle
	screen.blit(graphics3, (sWidth - menuRect2Y - leftRectX, bottomRect3Y - sWidth/16)) #Renders "Player 2" at the right of the screen above the blue rectangle
	screen.blit(graphics4, (sWidth/4, bottomRectY - sWidth/16)) #Renders "Press 'l' to return" at the bottom center of the screen between the red and white rectangles
	screen.blit(graphics5, (sWidth/4 + sWidth/8 + sWidth/32, bottomRectY)) #Renders "to game" below the "press 'l' to return"
	screen.blit(graphics6,(sWidth/2 - sWidth/8, sWidth/4))
	if difficulty[0] == 4: #checks if the difficulty is 4
		screen.blit(graphics11, (sWidth/2 - sWidth/32, sWidth/4 + sWidth/16)) #makes "Easy" appear red
		screen.blit(graphics8, (sWidth/2 - sWidth/16, sWidth/4 + sWidth/8)) #makes "Medium" appear white
		screen.blit(graphics9, (sWidth/2 - sWidth/32, sWidth/4 + sWidth/8 + sWidth/16)) #makes "hard" appear white
		screen.blit(graphics10, (sWidth/2 - sWidth/16 - sWidth/32, sWidth/2)) #makes "Very Hard" appear white
	elif difficulty[0] == 3: #checks if the difficulty is 3
		screen.blit(graphics7, (sWidth/2 - sWidth/32, sWidth/4 + sWidth/16)) #makes "Easy" appear white
		screen.blit(graphics12, (sWidth/2 - sWidth/16, sWidth/4 + sWidth/8)) #makes "Medium" appear red
		screen.blit(graphics9, (sWidth/2 - sWidth/32, sWidth/4 + sWidth/8 + sWidth/16)) #makes "hard" appear white
		screen.blit(graphics10, (sWidth/2 - sWidth/16 - sWidth/32, sWidth/2)) #makes "Very Hard" appear white
	elif difficulty[0] == 2: #checks if the difficulty is 2
		screen.blit(graphics7, (sWidth/2 - sWidth/32, sWidth/4 + sWidth/16)) #makes "Easy" appear white
		screen.blit(graphics8, (sWidth/2 - sWidth/16, sWidth/4 + sWidth/8)) #makes "Medium" appear white
		screen.blit(graphics13, (sWidth/2 - sWidth/32, sWidth/4 + sWidth/8 + sWidth/16)) #makes "hard" appear red
		screen.blit(graphics10, (sWidth/2 - sWidth/16 - sWidth/32, sWidth/2)) #makes "Very Hard" appear white
	elif difficulty[0] == 1: #checks if the difficulty is 1
		screen.blit(graphics7, (sWidth/2 - sWidth/32, sWidth/4 + sWidth/16)) #makes "Easy" appear white
		screen.blit(graphics8, (sWidth/2 - sWidth/16, sWidth/4 + sWidth/8)) #makes "Medium" appear white
		screen.blit(graphics9, (sWidth/2 - sWidth/32, sWidth/4 + sWidth/8 + sWidth/16)) #makes "hard" appear white
		screen.blit(graphics14, (sWidth/2 - sWidth/16 - sWidth/32, sWidth/2)) #makes "Very Hard" appear red
	else: #checks if the difficulty is anything but 1, 2, 3, or 4
		difficulty[0] = 4 #sets the difficulty to 4 if the difficulty goes below 1
	pg.draw.rect(screen, WHITE, (leftRectX, bottomRectY, menuRect2Y, menuRect2X), outline) #The white rectangle is placed at the bottom left of the screen
	pg.draw.rect(screen, RED, (leftRectX, bottomRect2Y, menuRect2Y, menuRect2X), outline) #The red rectangle is placed above the white rectangle
	pg.draw.rect(screen, BLUE, (leftRectX, bottomRect3Y, menuRect2Y, menuRect2X), outline) #The blue rectangle is placed above the red rectangle
	pg.draw.rect(screen, WHITE, (sWidth - leftRectX - menuRect2Y, bottomRectY, menuRect2Y, menuRect2X), outline) #The second white rectangle os placed at the bottom reight of the screen
	pg.draw.rect(screen, RED, (sWidth - leftRectX - menuRect2Y, bottomRect2Y, menuRect2Y, menuRect2X), outline) #The second red rectangle is placed above the second white rectangle
	pg.draw.rect(screen, BLUE, (sWidth - leftRectX - menuRect2Y, bottomRect3Y, menuRect2Y, menuRect2X), outline) #The second blue rectangle is placed above the second red rectangle
	mouseX, mouseY = pg.mouse.get_pos() #This function gets the X and Y position of the mouse
	mouse_buttons = pg.mouse.get_pressed() #This function checks if the mouse buttons are being pressed
	if mouseY > bottomRectY and mouseY < bottomRectY + menuRect2X and mouseX > leftRectX and mouseX < leftRectX + menuRect2Y and mouse_buttons[0]:
		Rcolor[0] = WHITE #This if statement checks if the mouse is above the left white rectangle and checks if the mouse button is being pressed and if both happen, it changed the color of the left paddle to white
	if mouseY > bottomRect2Y and mouseY < bottomRect2Y + menuRect2X and mouseX > leftRectX and mouseX < leftRectX + menuRect2Y and mouse_buttons[0]:
		Rcolor[0] = RED #This if statement checks if the mouse is above the left red rectangle and checks if the mouse button is being pressed and if both happen, it changed the color of the left paddle to red
	if mouseY > bottomRect3Y and mouseY < bottomRect3Y + menuRect2X and mouseX > leftRectX and mouseX < leftRectX + menuRect2Y and mouse_buttons[0]:
		Rcolor[0] = BLUE #This if statement checks if the mouse is above the left blue rectangle and checks if the mouse button is being pressed and if both happen, it changed the color of the left paddle to blue
	if mouseY > bottomRectY and mouseY < bottomRectY + menuRect2X and mouseX > sWidth - leftRectX - menuRect2Y and mouseX < sWidth - leftRectX and mouse_buttons[0]:
		Rcolor[1] = WHITE #This if statement checks if the mouse is above the left white rectangle and checks if the mouse button is being pressed and if both happen, it changed the color of the right paddle to white
	if mouseY > bottomRect2Y and mouseY < bottomRect2Y + menuRect2X and mouseX > sWidth - leftRectX - menuRect2Y and mouseX < sWidth - leftRectX and mouse_buttons[0]:
		Rcolor[1] = RED #This if statement checks if the mouse is above the right red rectangle and checks if the mouse button is being pressed and if both happen, it changed the color of the right paddle to red
	if mouseY > bottomRect3Y and mouseY < bottomRect3Y + menuRect2X and mouseX > sWidth - leftRectX - menuRect2Y and mouseX < sWidth - leftRectX and mouse_buttons[0]:
		Rcolor[1] = BLUE #This if statement checks if the mouse is above the right blue rectangle and checks if the mouse button is being pressed and if both happen, it changed the color of the left paddle to blue
	keys = pg.key.get_pressed() #checks to see if any keys are pressed
	if keys[pg.K_d]: #only happens if 'd' is pressed
		difficulty[0] = difficulty[0] - 1 #the difficulty decreases by 1 *note: the lower the difficulty the harder it is
		pg.time.delay (100) #prevents the difficulty from changing too fast