import random

import pygame
from pygame import Surface, Rect
from pygame.ftfont import Font

from code.Const import C_WHITE, WIN_HEIGHT, MENU_PLAYER, EVENT_ENEMY, SPAWN_TIME, WIN_WIDTH, EVENT_TIMEOUT, \
    TIMEOUT_STEP, TIMEOUT_LEVEL
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player



class Level:
    def __init__(self, window, jogador_escolhido):
        self.window = window
        self.surf = pygame.image.load('./asset/BackgroundJogo.png')
        self.rect = self.surf.get_rect(left=0, top=0)
        self.jogador = jogador_escolhido  # indice do jogador
        self.entity_list: list[Entity] = []
        self.entity_list.append(EntityFactory.get_entity(MENU_PLAYER[self.jogador]))
        self.timeout = TIMEOUT_LEVEL
        self.vitimas_mortas = 0
        self.vitimas_salvas =0
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT,TIMEOUT_STEP)

    def run(self):
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            if self.vitimas_mortas >=3:
                self.window.blit(source=self.surf, dest=self.rect)
                self.level_text(200, 'YOU LOSE !!', C_WHITE, (WIN_WIDTH/2-400, WIN_HEIGHT/2-100))
                self.level_text(30, 'Você perdeu, porque mato 3 vitimas', C_WHITE, (WIN_WIDTH / 2-200 , WIN_HEIGHT / 2+100))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                pygame.display.flip()
                continue


            if self.timeout <=0:

                jogador_atual = None
                for entidade in self.entity_list:
                    if isinstance(entidade, Player):
                        jogador_atual = entidade
                        break

                self.window.blit(source=self.surf, dest=self.rect)
                self.level_text(200, 'YOU WIN !!', C_WHITE, (WIN_WIDTH / 2 -400, WIN_HEIGHT / 2 - 100))
                self.level_text(50, f'Você resgatou {self.vitimas_salvas} clientes', C_WHITE, (WIN_WIDTH / 2 - 400, WIN_HEIGHT / 2 - 150))

                if jogador_atual is not None:
                    self.level_text(50, f'Você matou {jogador_atual.score} zumbis', C_WHITE,
                                    (WIN_WIDTH / 2 - 400, WIN_HEIGHT / 2 - 200))
                    self.level_text(50, 'Pressione ENTER para voltar ao menu', C_WHITE, (WIN_WIDTH / 2 - 400, WIN_HEIGHT - 122))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            return
                pygame.display.flip()
                continue


            # 1. DESENHA O FUNDO (Limpa a tela do frame anterior)
            self.window.blit(source=self.surf, dest=self.rect)

            # 2. CAPTURA DE EVENTOS (Fechar jogo, Spawn de inimigos)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == EVENT_ENEMY:
                    choice = random.choice(('enemyA1', 'enemyB1', 'vitima0'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP


            # 3. FÍSICA E COLISÕES (Calcula o dano e altera a vida/score ANTES de atualizar a tela)
            EntityMediator.verify_collision(entity_list=self.entity_list,level_ref=self)
            EntityMediator.verify_health(entity_list=self.entity_list)


            novos_tiros = []

            # 4. MOVIMENTAÇÃO, ATUALIZAÇÃO E DESENHO (Apenas UM loop para tudo)
            for ent in self.entity_list:
                ent.move()

                # Executa o tiro para quem pode atirar
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        novos_tiros.append(shoot)

                # Se for o jogador, atualiza o tempo de piscar e renderiza o texto do Score/Vida
                if isinstance(ent, Player):
                    ent.update()
                    self.level_text(28, f'Tempo do jogo:  {self.timeout / 1000 :.1f}s', C_WHITE, (10, 50))
                    self.level_text(28, f'{ent.name}:  {ent.health}', C_WHITE, (10, 100))
                    self.level_text(28, f'Score : {ent.score}', C_WHITE, (10, 150))
                    self.level_text(28,f'Vitimas Salvas :{self.vitimas_salvas}',C_WHITE, (10, 200))
                    if self.vitimas_mortas ==1:
                        self.level_text(40, f'Você mato {self.vitimas_mortas} VÍTIMA!', C_WHITE, (500, WIN_HEIGHT/2))
                    if self.vitimas_mortas == 2:
                        self.level_text(40, f'Você mato {self.vitimas_mortas} VÍTIMAS!', C_WHITE, (500, WIN_HEIGHT/2))
                        self.level_text(40, f'CUIDADO SE MATAR 3 VITIMAS O JOGO TERMINA!', C_WHITE, (350, WIN_HEIGHT/2+40))

                # Desenha a entidade na tela de forma definitiva
                self.window.blit(source=ent.surf, dest=ent.rect)

            # Se houver novos tiros criados neste frame, adiciona à lista global
            if novos_tiros:
                self.entity_list.extend(novos_tiros)

            # 5. ATUALIZA O MONITOR
            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)


