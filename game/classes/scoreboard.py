import pygame.font
from pygame.sprite import Group

class Scoreboard:
    """ Uma classe para mostrar informações sobre pontuação """

    def __init__(self, settings, screen, stats):
        """ Inicializa os atributos da pontuação. """
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats

        # Configurações de fonte para as informações de pontuação
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepara a imagem das pontuações iniciais
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
    
    def prep_score(self):
        """ Transforma a pontuação em uma imagem renderizada """
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color)
        
        # Exibe a pontuação na parte superior direita da tela
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def prep_high_score(self):
        """ Transforma a pontuação maxíma em uma imagem renderizada """
        high_score = round(self.stats.high_score, -1)
        high_score_str = f'{high_score:,}'
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color, self.settings.bg_color)
        
        # Centraliza a pontuação maxíma na parte superior da tela
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
    
    def prep_level(self):
        """ Transforma o nivel em uma imagem renderizada """
        self.level_image = self.font.render(
            f"Fase {self.stats.level}", True, self.text_color, self.settings.bg_color)
        
        # Posiciona o nivel abaixo da pontuação.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10


    def show_score(self):
        """ Desenha a pontuação na tela """
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
