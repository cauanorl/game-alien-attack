import sys
import pygame
from classes.bullets import Bullet
# from game.classes.ship import Ship

def check_events(settings, screen, ship, bullets):
    """ 
    responde a eventos de pressionamento de teclas e
    de mouse
    """
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                sys.exit()

            case pygame.KEYDOWN:
                check_keydown_events(
                    event, settings, screen, ship, bullets
                )

            case pygame.KEYUP:
                check_keyup_events(event, ship)


def check_keydown_events(event, settings, screen, ship, bullets):
    match event.key:
        case pygame.K_RIGHT:
            ship.moving_right = True
        case pygame.K_LEFT:
            ship.moving_left = True
        case pygame.K_SPACE:
            fire_bullet(bullets, settings, screen, ship)


def check_keyup_events(event, ship):
    match event.key:
        case pygame.K_RIGHT:
            ship.moving_right = False
        case pygame.K_LEFT:
            ship.moving_left = False


def update_screen(settings, screen, ship, bullets):
    # Redesenha a tela  a cada passagem do laço
    screen.fill(settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()

    # Deixa a tela mais recente visivel
    pygame.display.flip()


# Livra-se dos projéteis  que desapareceram
def update_bullets(bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(bullets, settings, screen, ship):
    if len(bullets) < settings.bullets_allowed:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)
