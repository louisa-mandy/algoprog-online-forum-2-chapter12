# importing the other python to run to this main python file 

import pygame 
from pygame.sprite import Group 

from settings import Settings 
from ship import Ship 
import game_functions as gf 

def run_game():
  #activating pygame, settings and screen
  pygame.init()
  ai_settings = Settings()
  
  screen = pygame.display.set_mode(
    (ai_settings.screen_width, ai_settings.screen_height))
  pygame.display.set_caption("Alien Invasion")

  #setting up the background color 
  bg_color = (230, 230, 230)

  #creating the ship for the game
  ship = Ship(ai_settings, screen)

  #for storing bullets 
  bullets = Group()

  #creating a loop for the game to start 
  while True:
    gf.check_events(ai_settings, screen, ship, bullets)
    ship.update()
    gf.update_bullets(bullets)
    gf.update_screen(ai_settings, screen, ship, bullets)

run_game()
