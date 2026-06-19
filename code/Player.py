import pygame.key

from code.Const import WIN_WIDTH, MOVE_PLAYER, ENTITY_SPEED, PLAYER_KEY_SHOOT, ENTITY_SHOT_DELAY, ENTITY_HEALTH
from code.Entity import Entity
from code.PlayerShot import PlayerShot


class Player(Entity):

    def __init__(self,name:str,position:tuple,ani_index:int):
        super().__init__(name,position,1)
        self.index= str(ani_index)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        #ANIMAÇÃO

        self.animation_frames=[]
        #carregar as 3 imagens
        for i in range(2):
            frame=pygame.image.load(f'./asset/{name}{i}.png').convert_alpha()
            self.animation_frames.append(frame)
        self.current_frame = 0
        self.animation_speed = 0.1
        self.is_moving = False


        # VARIÁVEIS DO SALTO
        self.is_jumping = False  # Indica se o jogador está no ar
        self.jump_speed = 20  # A força inicial do pulo (quantos pixels ele sobe no primeiro frame)
        self.v_speed = 0  # Velocidade vertical atual (sofre ação da gravidade)
        self.gravity = 1  # O quanto a gravidade puxa ele para baixo a cada frame
        # Guardar a posição do chão (ajuste conforme o seu cenário)
        # Aqui assume que ele começa no chão na posição original do spawn
        self.floor_y = position[1]

        self.entity_speed = ENTITY_SPEED[name]
        self.health = ENTITY_HEALTH[name]
        self.damaged_timer = 0  #guarda o momento do dano
        self.is_blinking = False #diz se o jogador está no estado de brilho
        self.blink_duration = 2000  #duração do brilho em milissegundo




    def move(self,):
        pressed_key = pygame.key.get_pressed()
        self.is_moving =False
        if pressed_key[pygame.K_RIGHT] and self.rect.right< WIN_WIDTH:
            self.rect.centerx += self.entity_speed #recebe a velocidade do jogador
            self.is_moving = True #o jogador está andando

        if pressed_key[pygame.K_LEFT] and self.rect.left>0:
            self.rect.centerx -= self.entity_speed #recebe a velocidad do jogador
            self.is_moving = True  # o jogador esta andando

        #Animação Caminhando
        if not self.is_jumping:
            if self.is_moving: #si esta caminhando somamos a velocidade
                self.current_frame += self.animation_speed

                if self.current_frame >=len(self.animation_frames):#se o contador passa o numero de imagen volta a zero
                    self.current_frame = 0

                self.surf = self.animation_frames[int(self.current_frame)]#desenha o surf da imagen atual
            else:
                self.surf = self.animation_frames[1]#se esta parado fica na posição 1 da animation_frames


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


    def shoot(self):

        self.shot_delay -= 1

        if self.shot_delay ==0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            pressed_key = pygame.key.get_pressed()
            if pressed_key[PLAYER_KEY_SHOOT[self.name + self.index]]:
                return PlayerShot(name='TiroDejogador', position=(self.rect.centerx, self.rect.centery-20), ani_index=0)


        return None

# essa logica é do chatgpt
    def update(self):
        current_time = pygame.time.get_ticks()

        # Verifica se o tempo de 2 segundos já acabou
        if self.is_blinking:
            if current_time - self.damaged_timer > self.blink_duration:
                self.is_blinking = False
                self.surf.set_alpha(255)  # Volta a opacidade normal
            else:
                # O segredo está aqui: forçar o set_alpha a cada frame no sprite atualizado
                if (current_time // 100) % 2 == 0:
                    self.surf.set_alpha(60)  # Deixei um pouco mais transparente para destacar
                else:
                    self.surf.set_alpha(255)
        else:
            # Garante que se não estiver piscando, a opacidade permaneça padrão
            self.surf.set_alpha(255)
