import random

import pygame

from code.Const import ENTITY_SPEED, WIN_WIDTH
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple, ani_index: int,can_jump:bool=False):
        super().__init__(name, position, ani_index)
        self.ani_index = str(ani_index)
        self.entity_speed = ENTITY_SPEED[self.name]
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

    def move(self):
        self.rect.centerx -= self.entity_speed #movimento do enemies de direita a esquerda

        # if not self.is_jumping:
        #     self.current_frame += self.animation_speed
        #
        #     # Se o contador passar do número de imagens (2), volta para o zero
        #     if self.current_frame >= len(self.animation_frames):
        #         self.current_frame = 0
        #
        #     # Atualiza a imagem atual do inimigo (o "surf")
        #     self.surf = self.animation_frames[int(self.current_frame)]
        #     self.image =  self.surf
        # else:
        #     # Opcional: Se estiver pulando, fixa na imagem 1 (pés no ar)
        #     self.surf = self.animation_frames[0]
        #     self.image =self.surf

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



        if self.rect.right <=0:
            self.rect.left = WIN_WIDTH
