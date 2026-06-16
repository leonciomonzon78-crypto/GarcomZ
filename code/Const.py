#C
import pygame

C_YELLOW = (247, 201, 0)
C_WHITE = (255, 255, 255)

#E
ENTITY_SPEED={  'jogadorA' : 6,
                'enemyA': 2,
                'enemyB': 3,
                'TiroDejogador': 9,
                'XicaraDeFogo':6

              }

ENTITY_HEALTH = {
    'enemyA':50,
    'enemyB':60,
}

ENTITY_SHOT_DELAY={'jogadorA':20,
                   'enemyA':100,
                   'enemyB':80,
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

PLAYER_KEY_SHOOT ={'jogadorA1':pygame.K_SPACE}

#S
SPAWN_TIME = 4000 # O TEMPO QUE OS ENEMIES SÃO CRIADO



#W
WIN_WIDTH = 1200 #COMPRIMENTO
WIN_HEIGHT = 800 #ALTURA


