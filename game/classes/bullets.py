import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ Uma classe que administra os projeteis disparados pela espaçonave """

    def __init__(self, settings, screen, ship):
        super().__init__()
        self.screen = screen
        
        # Cria um retângulo para projétil em (0, 0) e, em seguida,
        # define a posição correta
        self.rect = pygame.Rect(
            0, 0, settings.bullet_width, settings.bullet_height
        )
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # armazena a posição do projeto com um valor decimal
        self.y = float(self.rect.y)

        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor

    def update(self):
        """ Move o projétil para cima da tela """

        # Atualiza a posição decimal do projetil
        self.y -= self.speed_factor
        # Atualiza a posição do rect
        self.rect.y = self.y

    def draw_bullet(self):
        """ Desenha o projétil na tela """
        pygame.draw.rect(self.screen, self.color, self.rect)


