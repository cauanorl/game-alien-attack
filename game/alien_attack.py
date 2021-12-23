import sys
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
        
        # Redesenha a tela  a cada passagem do laço
        screen.fill(game_settings.bg_color)
        ship.blitme()
        
        # Deixa a tela mais recente visivel
        pygame.display.flip()

run_game()
