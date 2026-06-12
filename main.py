import pygame

pygame.init()
screen = pygame.display.set_mode(size=(1200,800))

while True:
    #check all event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #close screen
            quit() #end pygame