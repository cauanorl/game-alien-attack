import sys
import pygame

from classes.bullets import Bullet
from classes.alien import Alien


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
        case pygame.K_q:
            sys.exit()


def check_keyup_events(event, ship):
    match event.key:
        case pygame.K_RIGHT:
            ship.moving_right = False
        case pygame.K_LEFT:
            ship.moving_left = False


def update_screen(settings, screen, ship, bullets, aliens):
    # Redesenha a tela  a cada passagem do laço
    screen.fill(settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

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


def get_number_aliens_x(settings, alien_width):
    """ Determina o número de aliens que cabem em uma linha """
    available_space_x = settings.screen_width - (2 * alien_width)
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(settings, screen, aliens, alien_number, row_number):
    # Cria um alien e o posiciona na linha
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_rows(settings, ship_height, alien_height):
    """ Determina o número de linhas com aliens que cabem na tela """
    available_space_y = (
        settings.screen_height - (3 * alien_height) - ship_height
    )
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_fleet(settings, screen, aliens, ship):
    """ Cria uma frota completa de alienígenas """
    # Cria um alienígena e calcula o número de alienígenas em uma linha
    # O espaçamento entre os alienígenas é igual a sua largura
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    number_aliens_x = get_number_aliens_x(settings, alien_width)
    number_rows = get_number_rows(settings, ship.rect.height, alien.rect.height)

    # Cria a primeira linha de alienígenas
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # Cria um alien e o posiciona na linha
            create_alien(settings, screen, aliens, alien_number, row_number)


def update_aliens(aliens, settings):
    """ Atualiza a posição de todos os alienígenas da frota """
    check_fleet_edges(settings, aliens)
    aliens.update()


def check_fleet_edges(settings, aliens):
    """ Responde apropriadamente se algum alien alcançou a borda """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break


def change_fleet_direction(settings, aliens):
    """ Faz toda frota descer e mudar sua  direção """
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1
