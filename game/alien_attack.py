import pygame
from pygame.sprite import Group

from config.settings import Settings
from classes.ship import Ship
from classes.bullets import Bullet
import game_functions.functions as gm_function

def run_game():
    # Inicializa o pygame, as config e o objeto screen
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((
        game_settings.screen_width,
        game_settings.screen_height
    ))
    pygame.display.set_caption('Alien Attack')

    # Cria uma espaçonave
    ship = Ship(screen, game_settings)

    # Inicia o laço principal do jogo
    while True:

        # Observa eventos de teclado e de mouse
        gm_function.check_events(ship)
        ship.update()
        gm_function.update_screen(game_settings, screen, ship)

run_game()
