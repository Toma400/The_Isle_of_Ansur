import pygame; pygame.init(); pygame.mixer.init()
from core.graphics.gh_system import run_screen, bgm_screen, Screen
from core.graphics.gui_types import gui_handler
from core.sounds.music import music_handler
from core.scripts import script_handler
from core.scripts import event_handler
from core.utils import *

def main_circle():
    #dyn_screen = [run_screen()] # list instead of variable allows for further use of run_screen() in gui_handler (both read-write, unlike 'screen' below)
    #bgs = bgm_screen()  # selects menu panorama
    dyn_screen = Screen()

    script_loader() # loads all scripts to be used by script_handler
    forged_events = [] # event system inspired partly by Forge API
    guitype = ["menu", None]  # tells gui_handler which menu you are at | can use positions 1-... for submenus (use 'switch_scr()' to change)
    music = None

    tev = []
    while not tev:

        screen = dyn_screen.screen # read-only, but simpler value to be used by most features

        pg_events = pygame.event.get() # variablised so it can be passed to functions w/o calling more than one per frame
        for event in pg_events:
            if event.type == pygame.QUIT:
                tev.append("end")

        music = music_handler(music, guitype, forged_events)  # controls music
        gui_handler(screen, guitype, forged_events, pg_events, tev, dyn_screen) # draws elements on a screen and sets interactions
        event_handler(forged_events, guitype) # handles forged_events additions
        script_handler(forged_events, screen, pg_events) # handles forged_events -> scripts runs

        pygame.display.flip()

    temp_remover(); pygame.quit()