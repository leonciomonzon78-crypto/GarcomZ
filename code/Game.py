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


            #menu_player = PlayerChoiceMenu(self.window)
            #play_return = menu_player.run()


            if menu_return == MENU_OPTION[0]:
                menuPlayer = PlayerChoiceMenu(self.window)
                play_return = menuPlayer.run()
                if play_return == MENU_OPTION[2]:
                    level = Level(self.window)
                    level.run()




