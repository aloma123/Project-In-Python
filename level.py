import pygame
from settinggame import *
from tie import Tile
from player import Player
from tree import Tree
from debug import debug
from support import *
from random import choice
class Level:
	def __init__(self):

		self.display_surface = pygame.display.get_surface()


		self.visible_sprites = YSortCameraGroup()
		self.obstacle_sprites = pygame.sprite.Group()

		self.create_map()


	def create_map(self):
		layouts = {
		'farm': farm_map , #import_csv_layout('farm.csv'), 
		'grass':import_csv_layout('farm.csv'),
		}
		graphics = {
		'grass': import_folder(),
		'objects': import_folder()
		}
		for style,layout in layouts.items():
			for row_index,row in enumerate(layout):
				for col_index,col in enumerate(row):
					if col =='x':
						x = col_index * tilesize
						y = row_index * tilesize
						
						if style == 'farm':
							Tile((x,y), [self.obstacle_sprites], 'invisible')
						if style == 'grass':
							random_grass_image = choice(graphics['grass'])
							Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'grass',random_grass_image)
						if style == 'objects':
							surf = graphics['objects'][int(col)]
							Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'objects',surf)


						# if col == 'x':
						# 	Tile((x,y),[self.visible_sprites,self.obstacle_sprites])
						# if col == 't':
						#if col == 'p':
						# 	Tree((x,y),[self.visible_sprites,self.obstacle_sprites])
				# 			self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites)

		self.player = Player((500,300),[self.visible_sprites],self.obstacle_sprites)

	def run(self):

		self.visible_sprites.custom_draw(self.player)
		self.visible_sprites.update()
		debug(self.player.status)
		#debug(self.player.direction)

class YSortCameraGroup(pygame.sprite.Group):
	def __init__(self):

		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.half_width = self.display_surface.get_size()[0] // 2
		self.half_heigth = self.display_surface.get_size()[1] // 2
		self.offset = pygame.math.Vector2()

		self.floor_surf = pygame.image.load('farm.png').convert() #pygame.transform.scale(pygame.image.load('farm.png').convert(),(2000,2000))
		self.floor_rect = self.floor_surf.get_rect(topleft =(0,0))

	def custom_draw(self,player):

		self.offset.x = player.rect.centerx - self.half_width
		self.offset.y = player.rect.centery - self.half_heigth

		floor_offset_pos = self.floor_rect.topleft - self.offset
		self.display_surface.blit(self.floor_surf,floor_offset_pos)

		# for sprite in self.sprites():
		for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
			offset_pos = sprite.rect.topleft - self.offset
			self.display_surface.blit(sprite.image,offset_pos)

