class Settings():
	'''STORE ALL SETTINGS FOR ALIEN INVASION X'''
	
	def __init__(self):
		'''INITIALIZE GAME SETTINGS'''
		#SCREEN SETTINGS
		self.screen_width = 1200
		self.screen_height = 650
		self.bg_color = (25,0,50)
		
		#SHIP SETTINGS
		self.ship_speed_factorx = 1.6
		self.ship_speed_factory = .8
		self.ship_limit = 3
		
		#ALIEN SETTINGS
		self.alien_speed_factor = .5
		self.fleet_drop_speed = 10
		#DIRECTION: 1 = RIGHT, -1 = LEFT
		self.fleet_direction = 1
		
		#BULLET SETTINGS
		self.bullet_speed_factor = 1
		self.bullet_width = 2
		self.bullet_height = 5
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 50
		
		#LASER SETTINGS
		self.laser_speed_factor = 10
		self.laser_width = 3
		self.laser_height = 15
		self.laser_color = 25, 250, 150
		self.lasers_allowed = 5
