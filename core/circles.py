import pygame; pygame.init(); pygame.mixer.init()
from core.graphics.gui_types import gui_handler
from core.sounds.music import music_handler
from core.graphics.gh_manag import *

def main_circle():
    screen = pygame.display.set_mode([svx, svy])
    guitype = "menu"  # tells gui_handler which menu you are at
    music = None

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        gui_handler(screen, guitype) # draws elements on a screen
        music_handler(music, guitype) # controls music

        pygame.display.flip()

    temp_remover(); pygame.quit()