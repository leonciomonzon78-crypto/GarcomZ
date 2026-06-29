import pygame.image

from code.Const import MENU_PLAYER, WIN_HEIGHT, IMA_SEP_MEA, MENU_OPTION


class PlayerChoiceMenu:
    def __init__(self,window):
        self.rect = None
        self.window = window
        self.fundo = pygame.image.load('./asset/MenuEscolha.png').convert_alpha()
        self.fundo_rect = self.fundo.get_rect(left=0, top=0)
        self.index_selecionado = 0



    def run(self,):

        while True:
            self.window.blit(source=self.fundo,dest=self.fundo_rect)

            for i in range(len(MENU_PLAYER)):
                imagen_jogador = pygame.image.load('./asset/'+MENU_PLAYER[i]+'.png').convert_alpha()
                posicao_central_x = (IMA_SEP_MEA + (i * IMA_SEP_MEA)) + (imagen_jogador.get_width()-200 )
                posicao_central_y = (WIN_HEIGHT -380) + (imagen_jogador.get_height() // 2)

                if i == self.index_selecionado:
                    # Aumenta a imagem em 1.5x
                    imagen_jogador = pygame.transform.scale(imagen_jogador, (int(imagen_jogador.get_width() * 1.5),
                                                                   int(imagen_jogador.get_height() * 1.5)))
                    
                    # 2. Em vez de usar 'left', posicionamos usando 'center' com o ponto central fixo!
                    self.rect = imagen_jogador.get_rect(center=(posicao_central_x, posicao_central_y))

                else:
                    # 3. Para os personagens não selecionados, também ancoramos pelo centro fixo
                    self.rect = imagen_jogador.get_rect(center=(posicao_central_x, posicao_central_y))

                self.window.blit(source=imagen_jogador, dest=self.rect)


            # check all event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # close screen
                    quit()  # end pygame

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT: #se presiona a tecla a direita a selecão vai rodando de para a direita.
                        if self.index_selecionado < len(MENU_PLAYER)-1:
                            self.index_selecionado +=1
                        else:
                            self.index_selecionado = 0

                    if event.key == pygame.K_LEFT:# se presiona a tecla a isquerda a seleção vai rodando a direita
                        if self.index_selecionado > 0:
                            self.index_selecionado -=1
                        else:
                            self.index_selecionado = len(MENU_PLAYER)-1

                        print(self.index_selecionado)

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            return MENU_OPTION[2],self.index_selecionado


            pygame.display.flip()



