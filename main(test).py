import pygame
from setting import *
pygame.init()
screen = pygame.display.set_mode((screen_w,screen_l))
pygame.display.set_caption("ไผ่ทอง")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

while True:

	pygame.time.delay(12)

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			quit()

	keys = pygame.key.get_pressed()

#Left
	if keys[pygame.K_LEFT] and player_x > 0:
		if pos_x < 0 and player_x == 400:
			pos_x += move
		else:
			player_x -= move

	if keys[pygame.K_a] and player_x > 0:
		if pos_x < 0 and player_x == 400:
			pos_x += move
		else:
			player_x -= move

#Right
	if keys[pygame.K_RIGHT] and player_x < 800:
	    if pos_x > screen_w - map_w and player_x == 400:
	    	pos_x -= move
	    else:
	    	player_x += move

	if keys[pygame.K_d] and player_x < 800:
		if pos_x > screen_w - map_w and player_x == 400:
			pos_x -= move
		else:
			player_x += move

#Up
	if keys[pygame.K_UP] and player_y > 0:
		if pos_y < 0 and player_y == 225:
			pos_y += move
		else:
			player_y -= move

	if keys[pygame.K_w] and player_y > 0:
		if pos_y < 0 and player_y == 225:
			pos_y += move
		else:
			player_y -= move

#Down
	if keys[pygame.K_DOWN] and player_y < 450:
		if pos_y > screen_l - map_l and player_y == 225:
			pos_y -= move
		else:
			player_y += move

	if keys[pygame.K_s] and player_y < 450:
		if pos_y > screen_l - map_l and player_y == 225:
			pos_y -= move
		else:
			player_y += move


	screen.blit(map_bg,(pos_x,pos_y))
	screen.blit(player,(player_x, player_y))
	pygame.display.update()
