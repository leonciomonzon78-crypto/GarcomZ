import random

import pygame
from pygame import Surface, Rect
from pygame.ftfont import Font

from code.Const import C_WHITE, WIN_HEIGHT, MENU_PLAYER, EVENT_ENEMY, SPAWN_TIME
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


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
        pygame.time.set_timer(EVENT_ENEMY,SPAWN_TIME)


    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            self.window.blit(source=self.surf,dest= self.rect)
            novos_tiros = []

            for ent in self.entity_list:
                #self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent,(Player,Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        novos_tiros.append(shoot)

                self.window.blit(source=ent.surf, dest=ent.rect)  # jogador

            if novos_tiros:
                self.entity_list.extend(novos_tiros)

            # check all event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # close screen
                    quit() # end pygame

                if event.type == EVENT_ENEMY:
                    choice = random.choice(('enemyA1', 'enemyB1'))
                    self.entity_list.append(EntityFactory.get_entity(choice))


            pygame.display.flip()
            EntityMediator.verify_collision(entity_list=self.entity_list)#chama o EntityMediator (verify_collision)
            EntityMediator.verify_health(entity_list=self.entity_list)




