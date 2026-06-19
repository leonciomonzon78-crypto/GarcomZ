from xml.sax import default_parser_list
import pygame

from code.Const import WIN_WIDTH
from code.Enemy import Enemy
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.Player import Player
from code.PlayerShot import PlayerShot
from code.Vitima import Vitima


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):  # desaparece a entity quando sai da tela
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.right <= 0:
                ent.health = 0
        if isinstance(ent, Vitima):
            if ent.rect.right <= 0:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        valid_interaction = False
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            valid_interaction = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            valid_interaction = True
        elif isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
            valid_interaction = True
        elif isinstance(ent1, Vitima) and isinstance(ent2, PlayerShot):
            valid_interaction = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Vitima):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, Enemy) and isinstance(ent2, Player):
            valid_interaction = True

        if valid_interaction:
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):

                # CÁLCULO: Player vs Enemy (Corpo a Corpo)
                if isinstance(ent1, Player) and isinstance(ent2, Enemy):
                    if not ent1.is_blinking:  # Só toma dano se não estiver brilhando
                        ent1.health -= ent2.damage
                        ent1.last_dmg = ent2.name
                        ent1.is_blinking = True
                        ent1.damaged_timer = pygame.time.get_ticks()

                elif isinstance(ent1, Enemy) and isinstance(ent2, Player):
                    if not ent2.is_blinking:  # Só toma dano se não estiver brilhando
                        ent2.health -= ent1.damage
                        ent2.last_dmg = ent1.name
                        ent2.is_blinking = True
                        ent2.damaged_timer = pygame.time.get_ticks()

                # CÁLCULO: Player vs EnemyShot (Tiro do Inimigo)
                elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
                    ent2.health = 0  # O tiro sempre some ao colidir
                    if not ent1.is_blinking:
                        ent1.health -= ent2.damage
                        ent1.last_dmg = ent2.name
                        ent1.is_blinking = True
                        ent1.damaged_timer = pygame.time.get_ticks()

                elif isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
                    ent1.health = 0  # O tiro sempre some ao colidir
                    if not ent2.is_blinking:
                        ent2.health -= ent1.damage
                        ent2.last_dmg = ent2.name
                        ent2.is_blinking = True
                        ent2.damaged_timer = pygame.time.get_ticks()

                # CÁLCULO: PlayerShot vs Vitima
                elif isinstance(ent1, PlayerShot) and isinstance(ent2, Vitima):
                    ent2.health -= ent1.damage  # A vítima perde vida
                    ent2.last_dmg = ent1.name
                    ent1.health = 0  # O tiro do jogador some

                elif isinstance(ent1, Vitima) and isinstance(ent2, PlayerShot):
                    ent1.health -= ent2.damage  # A vítima perde vida
                    ent1.last_dmg = ent2.name
                    ent2.health = 0  # O tiro do jogador some

                # REGRA GERAL: Para todo o resto (Ex: PlayerShot vs Enemy)
                else:
                    ent1.health -= ent2.damage
                    ent2.health -= ent1.damage
                    ent1.last_dmg = ent2.name

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        alive_entities = [ent for ent in entity_list if ent is not None and ent.health > 0]
        entity_list.clear()
        entity_list.extend(alive_entities)


