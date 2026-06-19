import random

import pygame

from code.Const import ENTITY_SPEED, WIN_WIDTH, ENTITY_SHOT_DELAY, ENTITY_HEALTH
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple, ani_index: int,can_jump:bool=False):
        super().__init__(name, position, ani_index)
        self.ani_index = str(ani_index)
        self.entity_speed = ENTITY_SPEED[self.name]
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.can_jump = can_jump
        #sistema de animação de pés
        self.animation_frames = []
        # carregar as 3 imagens
        for i in range(1):
            frame = pygame.image.load(f'./asset/{name}{i}.png').convert_alpha()
            self.animation_frames.append(frame)
        self.current_frame = 0
        self.animation_speed = 0.1

        #VARIÁVEIS DE FÍSICA DE SALTO
        self.is_jumping = False
        self.jump_speed = 20    #força pulo do zumbi(da para ajustar a altura do pulo)
        self.v_speed = 0
        self.gravity = 1
        self.floor_y = position[1] #guarda a linha do chão
        self.health = ENTITY_HEALTH[name]

    def move(self):
        self.rect.centerx -= self.entity_speed #movimento do enemies de direita a esquerda

        #logica de sorteio de pulo
        if self.can_jump and not self.is_jumping:#o sorteio do pulo só acontece se o enemy tiver a permissão can_jump
            if random.random()< 0.01:#significa 1% de chance a cada frame de iniciar um pulo
                self.is_jumping = True
                self.v_speed = -self.jump_speed

        if self.is_jumping:# se ele tiver na ar, esto aplica a gravidade
            self.rect.centery += self.v_speed
            self.v_speed += self.gravity
            if self.rect.top >= self.floor_y:#checa se o enemy chegou no chão
                self.rect.top = self.floor_y
                self.is_jumping = False
                self.v_speed = 0

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name='XicaraDeFogo', position=(self.rect.centerx, self.rect.centery-10), ani_index=0)



