import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Ship
    ship = Ship(screen)

    # Main loop for game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)


run_game()
