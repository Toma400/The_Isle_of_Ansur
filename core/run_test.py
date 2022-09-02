import pygame; pygame.init()
from core.utils import *
from core.graphics.gh_manag import *
from pygame.locals import QUIT

def testpyg():
    screen = pygame.display.set_mode([svx, svy])

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        imgFull(screen, "", "map.png")

        pygame.display.flip()

    pygame.quit()