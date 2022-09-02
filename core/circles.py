import pygame; pygame.init()
from core.graphics.gh_system import bg_screen
from core.graphics.gh_manag import *

def main_circle():
    screen = pygame.display.set_mode([svx, svy])
    bgs = bg_screen()

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        imgFull(screen, folderpath=bgs[0], imgname=bgs[1])
        imgPut(screen, folderpath="utils/assets/", imgname="logo.png", size_x=70, size_y=16, pos_x=15, pos_y=5, alpha=True)
        #imgPut(screen, folderpath="", imgname="button.jpg", size_x=14, size_y=9, pos_x=43, pos_y=35)
        #imgPut(screen, folderpath="", imgname="button.jpg", size_x=14, size_y=9, pos_x=43, pos_y=45)
        #imgPut(screen, folderpath="", imgname="button.jpg", size_x=14, size_y=9, pos_x=43, pos_y=55)
        #imgPut(screen, folderpath="", imgname="button.jpg", size_x=14, size_y=9, pos_x=43, pos_y=65)
        #imgPut(screen, folderpath="", imgname="button.jpg", size_x=14, size_y=9, pos_x=43, pos_y=75)

        pygame.display.flip()

    temp_remover(); pygame.quit()