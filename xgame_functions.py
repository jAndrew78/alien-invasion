


import sys
from time import sleep

import pygame

from xbullet import Bullet
from xalien import Alien


def check_keydown_events(event, settings, screen, ship, bullets):
	'''RESPOND TO KEYDOWNS'''
	if event.key == pygame.K_q:
		sys.exit()
	elif event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(settings, screen, ship, bullets)

def check_keyup_events(event, ship):
	'''RESPOND TO KEYUPS'''
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False				

def check_events(settings, screen, ship, bullets):
	'''RESPOND TO KEYBOARD AND MOUSE EVENTS'''
	#WATCH FOR KEYBOARD AND MOUSE EVENTS
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)


def fire_bullet(settings, screen, ship, bullets):
	'''FIRE BULLET IF LIMIT NOT REACHED'''
	#CREATE NEW BULLET, ADD IT TO BULLETS GROUP
	if len(bullets) < settings.bullets_allowed:
		new_bullet = Bullet(settings, screen, ship)
		bullets.add(new_bullet)

def update_bullets(settings, screen, ship, aliens, bullets):
	'''UPDATE POS OF BULLETS, GET RID OF OLD BULLETS'''
	#UPDATE BULLET POS
	bullets.update()
		
	#GET RID OF OLD BULLETS
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	#print(len(bullets))
	
	check_bullet_alien_collisions(settings, screen, ship, 
									aliens, bullets)
	
def check_bullet_alien_collisions(settings, screen, ship, 
									aliens, bullets):	
	'''RESPOND TO BULLET/ALIEN COLLISIONS'''
	#REMOVE BULLETS & ALIENS ON COLLISIONS
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

	if len(aliens) == 0: 
		#REMOVE EXISTING BULLETS, CREATE NEW FLEET
		bullets.empty()
		create_fleet(settings, screen, ship, aliens)

def get_number_aliens_x(settings, alien_width):
	'''DETERMINE NUMBER OF ALIENS THAT FIT IN A ROW'''
	available_space_x = settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x
	
def get_number_rows(settings, ship_height, alien_height):
	'''DETERMINE NUMBER OF ROWS OF ALIENS'''
	available_space_y = (settings.screen_height - 
							(3 * alien_height) - ship_height)
	number_rows = int(available_space_y / (2 * alien_height) - 1)
	return number_rows
	
def create_alien(settings, screen, aliens, alien_number, row_number):
	'''CREATE AN ALIEN AND PLACE IT IN THE ROW'''
	alien = Alien(settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2*alien.rect.height * row_number
	aliens.add(alien)
	
def create_fleet(settings, screen, ship, aliens):
	'''CREATE A FLEET OF ALIENS'''
	#CREATE AN ALIEN AND FIND THE NUMBER OF ALIENS IN A ROW
	alien = Alien(settings, screen)
	number_aliens_x = get_number_aliens_x(settings, alien.rect.width)
	number_rows = get_number_rows(settings, ship.rect.height, 
		alien.rect.height)
	
	#CREATE FLEET OF ALIENS
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(settings, screen, aliens, alien_number, 
				row_number)

def check_fleet_edges(settings, aliens):
	'''RESPOND IF ANY ALIENS REACH AN EDGE'''
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(settings, aliens)
			break
			
def change_fleet_direction(settings, aliens):
	'''DROP FLEET, CHANGE DIRECTION'''
	for alien in aliens.sprites():
		alien.rect.y += settings.fleet_drop_speed
	settings.fleet_direction *= -1

def check_aliens_bottom(settings, stats, screen, ship, aliens, bullets):
	'''CHECK IF ALIENS HIT BOTTOM'''
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			ship_hit(settings, stats, screen, ship, aliens, bullets)
			break

def ship_hit(settings, stats, screen, ship, aliens, bullets):
	'''RESPOND TO SHIP - ALIEN COLLISION'''
	if stats.ships_left > 0:
		stats.ships_left -= 1
		aliens.empty()
		bullets.empty()
		create_fleet(settings, screen, ship, aliens)
		ship.center_ship()
		sleep(0.5)
	
	else:
		stats.game_active = False

def update_aliens(settings, stats, screen, ship, aliens, bullets):
	'''CHECK EDGES, UPDATE FLEET POS'''
	check_fleet_edges(settings, aliens)
	aliens.update()
	
	#LOOK FOR ALIEN-SHIP COLLISIONS
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(settings, stats, screen, ship, aliens, bullets)
		print('Ship Hit!!')
		
	#LOOK FOR ALIENS HITTING BOTTOM
	check_aliens_bottom(settings, stats, screen, ship, aliens, bullets)
	
def update_screen(settings, screen, ship, aliens, bullets):
	'''UPDATE IMAGES ON SCREEN AND FLIP TO NEW SCREEN'''
	#REDRAW SCREEN DURING EACH PASS THROUGH THE LOOP
	screen.fill(settings.bg_color)
	#REDRAW BULLETS BEHIND SHIP AND ALIENS
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	aliens.draw(screen)
		
	#MAKE MOST RECENTLY DRAWN SCREEN VISABLE
	pygame.display.flip()
	
