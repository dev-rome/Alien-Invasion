import pygame

from settings import Settings
from ship import Ship
from alien import Alien
from pygame.sprite import Group
import game_functions as gf


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Ship.
    ship = Ship(ai_settings, screen)

    # Make a group to store bullets in.
    bullets = Group()
    aliens = Group()

    # Create the fleet if aliens.
    gf.create_fleet(ai_settings, screen, aliens)

    # Main loop for game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
