import pygame.image

from code.Const import MENU_PLAYER, WIN_HEIGHT, IMA_SEP_MEA, MENU_OPTION


class PlayerChoiceMenu:
    def __init__(self,window):
        self.window = window
        self.fundo = pygame.image.load('./asset/MenuEscolha.png').convert_alpha()
        self.fundo_rect = self.fundo.get_rect(left=0, top=0)
        self.index_selecionado = 0



    def run(self,):

        while True:
            self.window.blit(source=self.fundo,dest=self.fundo_rect)

            for i in range(len(MENU_PLAYER)):
                imagen_jogador = pygame.image.load('./asset/'+MENU_PLAYER[i]+'.png').convert_alpha()

                if i == self.index_selecionado:
                    imagen_jogador = pygame.transform.scale(imagen_jogador, (int(imagen_jogador.get_width() * 1.5),
                                                                   int(imagen_jogador.get_height() * 1.5)))
                    self.rect = imagen_jogador.get_rect(left=IMA_SEP_MEA + (i * IMA_SEP_MEA), top=WIN_HEIGHT / 2)

                    #self.window.blit(source=self.surf, dest=self.rect)
                else:
                    #self.surf = pygame.image.load(MENU_PLAYER[i]).convert_alpha()
                    self.rect = imagen_jogador.get_rect(left=IMA_SEP_MEA+(i*IMA_SEP_MEA), top=WIN_HEIGHT/2)

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



