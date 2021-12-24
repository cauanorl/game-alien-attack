import pygame
from pygame.sprite import Group

from config.settings import Settings
from classes.ship import Ship

# from classes.bullets import Bullet
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

    # Cria um grupo no qual serão armazenados os projéteis
    bullets = Group()

    # Inicia o laço principal do jogo
    while True:

        # Observa eventos de teclado e de mouse
        gm_function.check_events(game_settings, screen, ship, bullets)
        ship.update()
        bullets.update()

        # Livra-se dos projéteis  q ue desapareceram
        gm_function.update_bullets(bullets)

        gm_function.update_screen(game_settings, screen, ship, bullets)

run_game()
