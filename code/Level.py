import pygame



class Level:
    def __init__(self,window,jogador_escolhido):
        self.window = window
        self.surf = pygame.image.load('./asset/BackgroundJogo.png')
        self.rect = self.surf.get_rect(left=0 , top=0)
        self.jogador = jogador_escolhido
        print (self.jogador)

    def run(self):
        while True:
            self.window.blit(self.surf, self.rect)

            # check all event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # close screen
                    quit()  # end pygame


            pygame.display.flip()
