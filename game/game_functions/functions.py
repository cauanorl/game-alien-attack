import sys
import pygame

def check_events():
    """ 
    responde a eventos de pressionamento de teclas e
    de mouse
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(settings, screen, ship):
    # Redesenha a tela  a cada passagem do laço
    screen.fill(settings.bg_color)
    ship.blitme()

    # Deixa a tela mais recente visivel
    pygame.display.flip()
