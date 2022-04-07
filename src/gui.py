import pygame

class GUI:

    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode((800,600))
        inGame = True

        while (inGame): 
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    inGame = False