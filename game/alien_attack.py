import pygame

from config.settings import Settings
from ships.ship import Ship
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
    ship = Ship(screen)

    # Inicia o laço principal do jogo
    while True:

        # Observa eventos de teclado e de mouse
        gm_function.check_events()
        
        gm_function.update_screen(game_settings, screen, ship)

run_game()
