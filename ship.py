import pygame

class Ship():
	def __init__(self, settings, screen):
		'''INITIALIZE SHIP AND SET STARTING POS'''
		self.screen = screen
		self.settings = settings

		#LOAD SHIP IMAGE AND GET ITS RECT
		self.image = pygame.image.load('images/ship_neo.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		#START NEW SHIP AT BOTTOM CENTER
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		#STORE A DECIMAL VALUE FOR THE SHIP'S CENTER
		self.centerx = float(self.rect.centerx)
		self.centery = float(self.rect.centery)

		#MOVEMENT FLAG
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		
	def reset_ship(self):
		'''CENTER SHIP'''
		self.centerx = self.screen_rect.centerx
		self.centery = self.screen_rect.bottom - 30
		
	def update(self):
		'''UPDATE SHIP'S POS BASED ON MOVEMENT FLAGS'''
		# #UPDATE SHIP'S CENTER VALUE INSTEAD OF RECT
		# if self.moving_right and (self.rect.right < 
		# 							self.screen_rect.right):
		# 	self.center += self.settings.ship_speed_factor
		# if self.moving_left and self.rect.left > 0:
		# 	self.center -= self.settings.ship_speed_factor
	
		# #UPDATE RECT OBJECT FROM SELF.CENTER
		# self.rect.centerx = self.center


		if self.moving_right and self.rect.right < (15 + self.screen_rect.right):
			self.centerx += self.settings.ship_speed_factorx
		if self.moving_left and self.rect.left > -15:
			self.centerx -= self.settings.ship_speed_factorx
		if self.moving_up and self.rect.top > 0:
			self.centery -= self.settings.ship_speed_factory
		if self.moving_down and self.rect.bottom < (self.screen_rect.bottom):
			self.centery += self.settings.ship_speed_factory		
			
		#UPDATE RECT OBJ FROM SELF.CENTER
		self.rect.centerx = self.centerx
		self.rect.centery = self.centery
		
	def blitme(self):
		'''DRAW SHIP AT ITS CURRENT LOC'''
		self.screen.blit(self.image, self.rect)
