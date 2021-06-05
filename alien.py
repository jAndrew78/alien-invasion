import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	'''REPRESENT ONE ALIEN IN THE FLEET'''
	
	def __init__(self, settings, screen):
		'''INITIALIZE ALIEN, SET ITS STARTING POS'''
		super(Alien, self).__init__()
		self.screen = screen
		self.settings = settings
		
		#LOAD ALIEN IMAGE, SET ITS RECT ATTRIBUTE
		self.image = pygame.image.load('images/red_alien1small.png')
		self.rect = self.image.get_rect()
		
		#START NEW ALIEN NEAR TOP LEFT 
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		#STORE ALIEN'S EXACT POS
		self.x = float(self.rect.x)
		
	def blitme(self):
		'''DRAW ALIEN AT ITS CURRENT LOC'''
		self.screen.blit(self.image, self.rect)
		
	def check_edges(self):
		'''RETURN TRUE IF ALIEN IS AT EDGE'''
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True
		
		
	def update(self):
		'''MOVE ALIEN RIGHT OR LEFT'''
		self.x += (self.settings.alien_speed_factor *
						self.settings.fleet_direction)
		self.rect.x = self.x
		
