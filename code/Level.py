import pygame
from pygame import Surface, Rect
from pygame.ftfont import Font

from code.Const import C_WHITE, WIN_HEIGHT, MENU_PLAYER
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self,window,jogador_escolhido):
        self.window = window
        self.surf = pygame.image.load('./asset/BackgroundJogo.png')
        self.rect = self.surf.get_rect(left=0 , top=0)
        self.jogador = jogador_escolhido#indice do jogador
        self.entity_list:list[Entity]=[]
        self.entity_list.append(EntityFactory.get_entity(MENU_PLAYER[self.jogador]))
        #self.name = name
        self.timeout = 20000
        print(self.jogador)


    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            self.window.blit(source=self.surf,dest= self.rect)
            for entity in self.entity_list:
                entity.move()
                self.window.blit(source=entity.surf, dest=entity.rect)#jogador



            # check all event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # close screen
                    quit()  # end pygame

            pygame.display.flip()




