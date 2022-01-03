class Settings:
    """ Uma classe para armazenar todas as config do Alien Attack """

    def __init__(self):
        """ Inicializando as configurações do jogo """
        #Configurações de tela
        self.screen_height = 800
        self.screen_width = 1200
        self.bg_color = (230, 230, 230)

        # Configurações da espaçonave
        self.ship_speed_factor = 0.5
        self.ship_limit = 3

        # Configurações dos projeteis
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Configurações dos alienígenas
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction igual a 1 representa direita e -1 esquerda
        self.fleet_direction = 1
