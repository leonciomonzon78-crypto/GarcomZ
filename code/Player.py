import pygame.key

from code.Const import WIN_WIDTH
from code.Entity import Entity


class Player(Entity):

    def __init__(self,name:str,position:tuple):
        super().__init__(name,position)
        # VARIÁVEIS DO SALTO
        self.is_jumping = False  # Indica se o jogador está no ar
        self.jump_speed = 20  # A força inicial do pulo (quantos pixels ele sobe no primeiro frame)
        self.v_speed = 0  # Velocidade vertical atual (sofre ação da gravidade)
        self.gravity = 1  # O quanto a gravidade puxa ele para baixo a cada frame
        # Guardar a posição do chão (ajuste conforme o seu cenário)
        # Aqui assume que ele começa no chão na posição original do spawn
        self.floor_y = position[1]


    def move(self,):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_RIGHT] and self.rect.right< WIN_WIDTH:
            self.rect.centerx +=6
        if pressed_key[pygame.K_LEFT] and self.rect.left>0:
            self.rect.centerx -=6

            # COMANDO DE SALTO (Tecla Espaço ou Seta para Cima)
        if pressed_key[pygame.K_UP] and not self.is_jumping:
            self.is_jumping = True
            self.v_speed = -self.jump_speed  # Valor negativo faz subir no Pygame

            # FÍSICA DO SALTO (Acontece se ele estiver no ar)
        if self.is_jumping:
            self.rect.centery += self.v_speed  # Aplica o movimento vertical atual
            self.v_speed += self.gravity  # Gravidade age reduzindo a subida e iniciando a descida

            # Checa se o jogador voltou para o chão
            if self.rect.top >= self.floor_y:
                self.rect.top = self.floor_y  # Garante que ele não passe do chão
                self.is_jumping = False  # Permite que ele pule de novo
                self.v_speed = 0  # Zera a velocidade vertical
