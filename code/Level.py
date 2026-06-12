import pygame



class Level:
    def __init__(self,window):
        self.window = window
        self.surf = pygame.image.load('./asset/BackgroundJogo.png')
        self.rect = self.surf.get_rect(left=0 , top=0)

    def run(self):
        while True:
            pygame.display.flip()
            pass