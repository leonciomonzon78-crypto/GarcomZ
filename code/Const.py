#C
import pygame

C_YELLOW = (247, 201, 0)
C_WHITE = (255, 255, 255)

#E
ENTITY_SPEED={'jogadorA' : 6,
              'enemyA': 4,
              'enemyB': 3,
              }

EVENT_ENEMY = pygame.USEREVENT +1
#I
IMA_SEP_MEA = 270 #image separation measure(Separação de imagen do menu escolha jogador)

#M
MENU_OPTION = ('COMEÇAR',
               'SAIR',
               'JOGAR')

MOVE_PLAYER ={'jogadorA',
              }


#P
MENU_PLAYER =('JogadorA',
              'ChefZumbi1a',
              'Zumbi1a',
              )

#S
SPAWN_TIME = 4000 # O TEMPO QUE OS ENEMIES SÃO CRIADO



#W
WIN_WIDTH = 1200 #COMPRIMENTO
WIN_HEIGHT = 800 #ALTURA


