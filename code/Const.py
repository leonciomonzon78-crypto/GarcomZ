#C
import pygame

C_YELLOW = (247, 201, 0)
C_WHITE = (255, 255, 255)

#E
ENTITY_DAMAGE={'jogadorA':1,
               'jogadorB':1,
               'jogadorC':1,
               'TiroDejogador':25,
               'enemyA':1,
               'XicaraDeFogo':20,
               'enemyB':1,
               'XicaraDeFogo':20,
               'vitima':1,
               }

ENTITY_SPEED={  'jogadorA' : 6,
                'jogadorB' : 6,
                'jogadorC' : 6,
                'enemyA': 6,
                'enemyB': 6,
                'TiroDejogador': 9,
                'XicaraDeFogo':9,
                'vitima':2,
              }

ENTITY_HEALTH = {
    'jogadorA':300,
    'jogadorB':300,
    'jogadorC':300,
    'enemyA':100,
    'enemyB':50,
    'vitima':1,
}

ENTITY_SHOT_DELAY={'jogadorA':10,
                   'jogadorB':10,
                    'jogadorC':10,
                   'enemyA':100,
                   'enemyB':80,
                   }

EVENT_ENEMY = pygame.USEREVENT +1
EVENT_TIMEOUT = pygame.USEREVENT +2
#I
IMA_SEP_MEA = 270 #image separation measure(Separação de imagen do menu escolha jogador)

#M
MENU_OPTION = ('COMEÇAR',
               'SAIR',
               'JOGAR')

MOVE_PLAYER ={'jogadorA',
              'jogadorB',
              'jogadorC',
              }


#P
MENU_PLAYER =('JogadorA',
              'jogadorB',
              'jogadorC',
              )

PLAYER_KEY_SHOOT ={'jogadorA1':pygame.K_SPACE,
                   'jogadorB1':pygame.K_SPACE,
                   'jogadorC1':pygame.K_SPACE}

#S
SPAWN_TIME = 4000 # O TEMPO QUE OS ENEMIES SÃO CRIADO

#T
TIMEOUT_STEP = 100 # 1 segundo ou 100 mili segundos
TIMEOUT_LEVEL = 20000  #20 segundos



#W
WIN_WIDTH = 1200 #COMPRIMENTO
WIN_HEIGHT = 800 #ALTURA


