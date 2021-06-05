class GameStats():
	'''TRACK STATS'''
	def __init__(self, settings):
		'''INITIALIZE STATS'''
		self.settings = settings
		self.reset_stats()
		#START GAME IN AN ACTIVE STATE
		self.game_active = True
		
	def reset_stats(self):
		'''INITIALIZE STATS THAT CAN CHANGE DURING GAME'''
		self.ships_left = self.settings.ship_limit
		
	
		
