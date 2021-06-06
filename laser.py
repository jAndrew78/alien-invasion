import pygame
from pygame.sprite import Sprite

class Laser(Sprite):
	'''MANAGE LASERS FIRED FROM SHIP'''
	
	def __init__(self, settings, screen, ship):
		'''CREATE LASER OBJECT AT SHIP'S CURRENT POS'''
		super(Laser, self).__init__()
		self.screen = screen
		
		#CREATE A LASER RECT AT (0,0), THEN SET CORRECT POS
		self.rect = pygame.Rect(0,0, settings.laser_width,
			settings.laser_height)
		self.rect.centerx = ship.rect.centerx - 25
		self.rect.top = ship.rect.top + 50
		
		#STORE THE LASER'S POS AS A DECIMAL VALUE
		self.y = float(self.rect.y)
		self.x = float(self.rect.x)

		self.firing = False
		
		self.color = settings.laser_color
		self.speed_factor = settings.laser_speed_factor
		
	def update(self):
		'''MOVE THE LASER UP THE SCREEN'''
		#UPDATE DECIMAL POS OF LASER
		self.y -= self.speed_factor
		#UPDATE RECT POS
		self.rect.y = self.y
		#AUTO FIRE MODE
		while self.firing:
			for laser in laser.sprites():
				laser.draw_laser()
		
	def draw_laser(self):
		'''DRAW LASER TO THE SCREEN'''
		pygame.draw.rect(self.screen, self.color, self.rect)

