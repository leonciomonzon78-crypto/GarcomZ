from code.Const import WIN_HEIGHT
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name:str,position=(0,0)):
        match entity_name:
            case 'JogadorA':
                return Player('JogadorA',(10,WIN_HEIGHT-122))
            case 'ChefZumbi1a':
                return Player('ChefZumbi1a', (10, WIN_HEIGHT - 122))
            case 'Zumbi1a':
                return Player('Zumbi1a', (10, WIN_HEIGHT - 122))
