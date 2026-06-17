import random
from operator import index

from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.Enemy import Enemy
from code.Player import Player
from code.Vitima import Vitima


class EntityFactory:

    @staticmethod
    def get_entity(entity_name:str, position=(0, 0),ani_index=0):
        match entity_name:
            case 'JogadorA':
                return Player('jogadorA', (10,WIN_HEIGHT-122),1)
            case 'ChefZumbi1a':
                return Player('ChefZumbi1a', (10, WIN_HEIGHT - 122))
            case 'Zumbi1a':
                return Player('Zumbi1a', (10, WIN_HEIGHT - 122))
            case 'enemyA1':
                chance_de_pular = random.choice((True,False))
                return Enemy('enemyA', (WIN_WIDTH-50, WIN_HEIGHT - 122),1,can_jump=chance_de_pular)
            case 'enemyB1':
                return Enemy('enemyB', (WIN_WIDTH-50, WIN_HEIGHT - 122), 1)
            case 'vitima0':
                return Vitima('vitima', (WIN_WIDTH - 50, WIN_HEIGHT - 122), 0)

