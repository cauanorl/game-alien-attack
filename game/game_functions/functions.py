import sys
import pygame

def check_events(ship):
    """ 
    responde a eventos de pressionamento de teclas e
    de mouse
    """
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                sys.exit()

            case pygame.KEYDOWN:
                check_keydown_events(event, ship)
            
            case pygame.KEYUP:
                check_keyup_events(event, ship)


def check_keydown_events(event, ship):
    match event.key:
        case pygame.K_RIGHT:
            ship.moving_right = True
        case pygame.K_LEFT:
            ship.moving_left = True


def check_keyup_events(event, ship):
    match event.key:
        case pygame.K_RIGHT:
            ship.moving_right = False
        case pygame.K_LEFT:
            ship.moving_left = False


def update_screen(settings, screen, ship):
    # Redesenha a tela  a cada passagem do laço
    screen.fill(settings.bg_color)
    ship.blitme()

    # Deixa a tela mais recente visivel
    pygame.display.flip()
