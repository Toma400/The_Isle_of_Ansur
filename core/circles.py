import pygame; pygame.init(); pygame.mixer.init()
from core.graphics.gui_types import gui_handler
from core.sounds.music import music_handler
from core.scripts import script_handler
from core.scripts import event_handler
from core.graphics.gh_manag import *

def main_circle():
    screen = pygame.display.set_mode([svx, svy])
    forged_events = [] # event system inspired partly by Forge API
    guitype = "menu"  # tells gui_handler which menu you are at
    music = None

    run = True
    while run:

        pg_events = pygame.event.get() # variablised so it can be passed to functions w/o calling more than one per frame
        for event in pg_events:
            if event.type == pygame.QUIT:
                run = False

        gui_handler(screen, guitype, pg_events) # draws elements on a screen
        music_handler(music, guitype) # controls music
        event_handler(forged_events, guitype) # handles forged_events additions
        script_handler(forged_events) # handles forged_events -> scripts runs

        pygame.display.flip()

    temp_remover(); pygame.quit()