from abc import abstractmethod, ABC


import pygame


class Entity(ABC):

    def __init__(self, name:str, position :tuple,ani_index:int):
        self.name = name
        self.surf = pygame.image.load(f'./asset/{name}{ani_index}.png').convert_alpha()
        self.rect = self.surf.get_rect(left = position[0],top=position[1])
        self.speed = 0

    @abstractmethod
    def move (self,):
        pass

