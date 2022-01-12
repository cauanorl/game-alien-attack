class GameStats:
    """ Armazena dados estátisticos de alien_attack """

    def __init__(self, settings):
        self.settings = settings
        self.reset_stats()

        self.game_active = False

        self.high_score = 0

    def reset_stats(self):
        """ 
         Inicializa os dados estatisticos que
         podem mudar durente o jogo
        """
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
