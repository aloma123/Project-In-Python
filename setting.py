import pygame
screen_w = 900
screen_l = 600
map_w = 2700
map_l = 1800
pos_x = (screen_w - map_w)/2
pos_y = (screen_l - map_l)/2
player_w = 100
player_l = 150
player_x = (screen_w - player_w)/2
player_y = (screen_l - player_l)/2
move = 5
bg = [pygame.image.load("bg.png"), pygame.image.load("bg2-01.png")]
map_bg = pygame.transform.scale(bg[0], (map_w, map_l))
load_player = pygame.image.load("chr.png")
player = pygame.transform.scale(load_player,(player_w, player_l))
