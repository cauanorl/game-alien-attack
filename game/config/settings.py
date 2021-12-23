class Settings:
    """ Uma classe para armazenar todas as config do Alien Attack """

    def __init__(self):
        """ Inicializando as configurações do jogo """
        #Configurações de tela
        self.screen_height = 800
        self.screen_width = 1200
        self.bg_color = (230, 230, 230)

        # Configurações da espaçonave
        self.ship_speed_factor = 1.5

    