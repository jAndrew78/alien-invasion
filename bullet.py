import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	'''MANAGE BULLETS FIRED FROM SHIP'''
	
	def __init__(self, settings, screen, ship):
		'''CREATE BULLET OBJECT AT SHIP'S CURRENT POS'''
		super(Bullet, self).__init__()
		self.screen = screen
		
		#CREATE A BULLET RECT AT (0,0), THEN SET CORRECT POS
		self.rect = pygame.Rect(0,0, settings.bullet_width,
			settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		
		#STORE THE BULLET'S POS AS A DECIMAL VALUE
		self.y = float(self.rect.y)
		
		self.color = settings.bullet_color
		self.speed_factor = settings.bullet_speed_factor
		
	def update(self):
		'''MOVE THE BULLET UP THE SCREEN'''
		#UPDATE DECIMAL POS OF BULLET
		self.y -= self.speed_factor
		#UPDATE RECT POS
		self.rect.y = self.y
		
	def draw_bullet(self):
		'''DRAW BULLET TO THE SCREEN'''
		pygame.draw.rect(self.screen, self.color, self.rect)
