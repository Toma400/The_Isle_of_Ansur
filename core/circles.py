import pygame; pygame.init(); pygame.mixer.init()
from core.graphics.gui_types import gui_handler
from core.sounds.music import music_handler
from core.scripts import script_handler
from core.scripts import event_handler
from core.graphics.gh_system import *
from core.graphics.gh_manag import *

def main_circle():
    screen = run_screen()
    bgs = bgm_screen()  # selects menu panorama

    script_loader() # loads all scripts to be used by script_handler
    forged_events = [] # event system inspired partly by Forge API
    guitype = ["menu", None]  # tells gui_handler which menu you are at | can use positions 1-... for submenus (use 'switch_scr()' to change)
    music = None

    tev = []
    while not tev:

        pg_events = pygame.event.get() # variablised so it can be passed to functions w/o calling more than one per frame
        for event in pg_events:
            if event.type == pygame.QUIT:
                tev.append("end")

        music = music_handler(music, guitype, forged_events)  # controls music
        gui_handler(screen, guitype, forged_events, pg_events, tev, bgs) # draws elements on a screen and sets interactions
        event_handler(forged_events, guitype) # handles forged_events additions
        script_handler(forged_events, screen, pg_events) # handles forged_events -> scripts runs

        pygame.display.flip()

    temp_remover(); pygame.quit()