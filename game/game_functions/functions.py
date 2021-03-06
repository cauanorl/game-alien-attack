import sys
import pygame
from time import sleep

from classes.bullets import Bullet
from classes.alien import Alien


def check_events(settings, screen, ship, bullets, stats, button, aliens, sb):
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
                    event, settings, screen, ship, bullets, stats, aliens, sb
                )

            case pygame.KEYUP:
                check_keyup_events(event, ship)
            
            case pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                check_play_button(
                    stats, button, mouse_x, mouse_y, aliens, bullets, settings, screen, ship, sb)


def check_keydown_events(event, settings, screen, ship, bullets, stats, aliens, sb):
    match event.key:
        case pygame.K_RIGHT:
            ship.moving_right = True
        case pygame.K_LEFT:
            ship.moving_left = True
        case pygame.K_SPACE:
            fire_bullet(bullets, settings, screen, ship)
        case pygame.K_q:
            sys.exit()
        case pygame.K_p:
            start_game(stats, aliens, bullets, settings, screen, ship, sb)


def check_keyup_events(event, ship):
    match event.key:
        case pygame.K_RIGHT:
            ship.moving_right = False
        case pygame.K_LEFT:
            ship.moving_left = False


def check_play_button(stats, button, mouse_x, mouse_y, aliens, bullet, settings, screen, ship, sb):
    """ Inicia um novo jogo quando o jogador clicar em play """
    if button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
        start_game(stats, aliens, bullet, settings, screen, ship, sb)


def start_game(stats, aliens, bullet, settings, screen, ship, sb):
    # Oculta o cursor do mouse
    pygame.mouse.set_visible(False)

    settings.initialize_dynamic_settings()

    # Reinicia os dados estat??sticos do jogo
    stats.reset_stats()
    stats.game_active = True

    # Reinicia as imagens do painel de pontua????o
    sb.prep_score()
    sb.prep_high_score()
    sb.prep_level()
    sb.prep_ships()

    # Esvazia a lista de aliens e de proj??teis
    aliens.empty()
    bullet.empty()

    # Cria um nova frota e centraliza a espa??onave
    create_fleet(settings, screen, aliens, ship)
    ship.center_ship()


def update_screen(settings, screen, ship, bullets, aliens, button, stats, sb):
    # Redesenha a tela  a cada passagem do la??o
    screen.fill(settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)
    sb.show_score()
    if not stats.game_active:
        button.draw_button()
        pygame.mouse.set_visible(True)

    # Deixa a tela mais recente visivel
    pygame.display.flip()


def update_bullets(bullets, aliens, screen, ship, settings, stats, sb):
    """ Atualiza a posi????o dos proj??teis  e se livra dos proj??teis antigos """
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(settings, screen, ship, aliens, bullets, stats, sb)


def check_bullet_alien_collisions(settings, screen, ship, aliens, bullets, stats, sb):
    """ Responde a colis??es de proj??teis e alien??genas """
    # Remove qualquer proj??til e alien que tenha colidido
    collisions = pygame.sprite.groupcollide(aliens, bullets, True, True)

    if collisions:
        for aliens in  collisions.values():
            stats.score += settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        # Destr??i os proj??teis existentes e cria uma nova frota
        bullets.empty()
        settings.increase_speed()
        create_fleet(settings, screen, aliens, ship)
        stats.level += 1
        sb.prep_level()


def fire_bullet(bullets, settings, screen, ship):
    if len(bullets) < settings.bullets_allowed:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)


def get_number_aliens_x(settings, alien_width):
    """ Determina o n??mero de aliens que cabem em uma linha """
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
    """ Determina o n??mero de linhas com aliens que cabem na tela """
    available_space_y = (
        settings.screen_height - (3 * alien_height) - ship_height
    )
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_fleet(settings, screen, aliens, ship):
    """ Cria uma frota completa de alien??genas """
    # Cria um alien??gena e calcula o n??mero de alien??genas em uma linha
    # O espa??amento entre os alien??genas ?? igual a sua largura
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    number_aliens_x = get_number_aliens_x(settings, alien_width)
    number_rows = get_number_rows(settings, ship.rect.height, alien.rect.height)

    # Cria a primeira linha de alien??genas
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # Cria um alien e o posiciona na linha
            create_alien(settings, screen, aliens, alien_number, row_number)


def update_aliens(aliens, settings, ship, stats, screen, bullets, sb):
    """
     Atualiza a posi????o de todos os alien??genas da frota
     E muda de dire????o se uma borda foi alcan??ada
    """
    check_fleet_edges(settings, aliens)
    aliens.update()

    # Verifica se houve colis??es entre o alien??gena e a espa??onave
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(settings, stats, screen, ship, aliens, bullets, sb)
    
    check_aliens_bottom(settings, stats, screen, ship, aliens, bullets, sb)


def check_fleet_edges(settings, aliens):
    """ Responde apropriadamente se algum alien alcan??ou a borda """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break


def change_fleet_direction(settings, aliens):
    """ Faz toda frota descer e mudar sua  dire????o """
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1


def ship_hit(settings, stats, screen, ship, aliens, bullets, sb):
    """ Reponde a colis??o entre uma nave e um alien """
    if stats.ships_left > 0:
        # Decrementa ships_left
        stats.ships_left -= 1

        # Atualiza o painel de pontua????es
        sb.prep_ships()

        # Esvazia a lista de aliens e de proj??teis
        aliens.empty()
        bullets.empty()

        # Cria uma nova frota e centraliza a espa??onave
        create_fleet(settings, screen, aliens, ship)
        ship.center_ship()

        # Faz uma pausa
        sleep(0.5)
    else:
        stats.game_active = False


def check_aliens_bottom(settings, stats, screen, ship, aliens, bullets, sb):
    """ Verifica se algum alien??gena alcan??ou a parte inferior da tela """
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(settings, stats, screen, ship, aliens, bullets, sb)
            break


def check_high_score(stats, sb):
    """ Verifica se h?? uma nova pontua????o max??ma """
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()