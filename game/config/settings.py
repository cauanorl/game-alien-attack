class Settings:
    """ Uma classe para armazenar todas as config do Alien Attack """

    def __init__(self):
        """ Inicializando as configurações do jogo """

        # Configurações de tela
        self.screen_height = 800
        self.screen_width = 1200
        self.bg_color = (230, 230, 230)

        # Configurações da espaçonave
        self.ship_limit = 3

        # Configurações dos projeteis
        self.bullet_width = 3
        self.bullet_height = 15 
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Configurações dos alienígenas
        self.fleet_drop_speed = 15

        # A taxa com que velocidade o jogo aumenta
        self.speedup_scale = 1.1

        # A taxa com que os pontos aumentam
        self.score_scale = 1.5


        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1
        self.alien_speed_factor = 0.4
        self.bullet_speed_factor = 1

        # fleet_direction igual a 1 representa direita e -1 esquerda
        self.fleet_direction = 1

        # Pontuação
        self.alien_points = 50

    def increase_speed(self):
        """ Aumenta as configurações de velocidade e os pontos dos aliens """
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
