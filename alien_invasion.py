import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
	#INITIALIZE PYGAME, SETTINGS, SCREEN OBJECT
	pygame.init()
	settings = Settings()
	screen = pygame.display.set_mode(
		(settings.screen_width, settings.screen_height))
	pygame.display.set_caption("xAlien Invasion")
	
	#CREATE AN INSTANCE TO STORE GAME STATS
	stats = GameStats(settings)
	
	#MAKE A SHIP, BULLET GROUP, ALIEN GROUP
	ship = Ship(settings, screen)
	bullets = Group()
	aliens = Group()
	
	#CREATE ALIEN FLEET
	gf.create_fleet(settings, screen, ship, aliens)
	
	#START MAIN GAME LOOP
	while True:
		gf.check_events(settings, screen, ship, bullets)
		
		if stats.game_active:
			ship.update()
			gf.update_bullets(settings, screen, ship, aliens, bullets)
			gf.update_aliens(settings, stats, screen, 
								ship, aliens, bullets)
		
		gf.update_screen(settings, screen, ship, aliens, bullets)				
		
run_game()


