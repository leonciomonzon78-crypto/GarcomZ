import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu
from code.PlayerChoiceMenu import PlayerChoiceMenu




class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        
    def run(self):

        while True:
            menu = Menu(self.window)
            menu_return = menu.run()


            if menu_return == MENU_OPTION[0]:
                menuPlayer = PlayerChoiceMenu(self.window)
                player_return,jogador_escolhido  = menuPlayer.run()


                if player_return == MENU_OPTION[2]:
                    level1 = Level(self.window, jogador_escolhido)
                    level1.run()









