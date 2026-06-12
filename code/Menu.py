import pygame


class Menu:
    def __init__(self,window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuInicio.png')
        self.rect = self.surf.get_rect(left=0 , top=0)



    def run(self):
        pygame.mixer_music.load('./asset/MusicaMenu.mp3')
        pygame.mixer_music.play(-1)  # parametro -1 e para que musica não pare
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            pygame.display.flip()

            # check all event
            for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                    pygame.quit() #close screen
                    quit() #end pygame
