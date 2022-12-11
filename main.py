import pygame, sys
from settinggame import *
from debug import *
from level import Level
from tie import *
from tree import * 

class Game:
	def __init__(self):

		pygame.init()
		self.screen = pygame.display.set_mode((width, heigth))
		pygame.display.set_caption("Farmmer's Adventure")
		self.clock = pygame.time.Clock()

		self.level = Level()
	def run(self):
		while True:
			for event in pygame.event.get():

				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			self.screen.fill('black')
			self.level.run()
			pygame.display.update()
			self.clock.tick(fps)
if __name__ == '__main__':
	game = Game()
	game.run()
