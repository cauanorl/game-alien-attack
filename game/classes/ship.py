import pygame

class Ship:
    def __init__(self, screen, settings):
        """ Inicializa a espaçonave e define sua posição inicial """
        self.screen = screen

        self.ship_settings = settings

        # Carrega a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load('game/img/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Inicia cada espaçonave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Armazena um valor decimal para o centro da tela
        self.center = float(self.rect.centerx)

        # Flag de movimento
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ Atualiza a posição da espaçonave de acordo com a flag de movimento """

        # Atualiza o valor do centro da espaçonave, e não do retângulo
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ship_settings.ship_speed_factor

        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ship_settings.ship_speed_factor

        # Atualiza o objeto rect de acordo com self.center
        self.rect.centerx = self.center

    def blitme(self):
        """ Desenha a espaçonave em sua posição atual. """
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """ Centraliza a espaçonave """
        self.center = self.screen_rect.centerx