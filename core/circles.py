import pygame; pygame.init(); pygame.mixer.init()
from core.graphics.gui_types import gui_handler
from core.graphics.gh_system import Screen
from core.sounds.music import music_handler
from core.scripts import script_handler
from core.scripts import event_handler
from core.data.pack_manag import packs
from os.path import exists
from core.utils import *
import logging as log

fps_check = exists(".fps")

def main_circle():
    packs.removePacks()
    packs.unpackPacks()
    packs.verifyPacks()
    dyn_screen = Screen()

    script_loader() # loads all scripts to be used by script_handler
    forged_events = [] # event system inspired partly by Forge API
    guitype = ["menu", None]  # tells gui_handler which menu you are at | can use positions 1-... for submenus (use 'switch_scr()' to change)
    music = None

    tev = []
    while not tev:
        dyn_screen.dtime = dyn_screen.clock.tick(60) / 1000.0  # delta time for PyGameGUI
        screen           = dyn_screen.screen                   # read-only, but simpler value to be used by most features

        pg_events = pygame.event.get() # variablised so it can be passed to functions w/o calling more than one per frame
        for event in pg_events:
            if event.type == pygame.QUIT:
                tev.append("end")

            dyn_screen.pgui.process_events(event)  # PyGameGUI handler of events
            dyn_screen.pgui2.process_events(event)
            dyn_screen.pgui3.process_events(event)

        dyn_screen.pgui.update(dyn_screen.dtime) # PyGameGUI updater
        dyn_screen.pgui2.update(dyn_screen.dtime)
        dyn_screen.pgui3.update(dyn_screen.dtime)

        music = music_handler(music, guitype, forged_events)                    # controls music
        gui_handler(screen, guitype, forged_events, pg_events, tev, dyn_screen) # draws elements on a screen and sets interactions
        event_handler(forged_events, guitype)                                   # handles forged_events additions
        script_handler(forged_events, screen, pg_events, dyn_screen)            # handles forged_events -> scripts runs

        dyn_screen.pgui.draw_ui(screen) # PyGameGUI UI handler
        dyn_screen.pgui2.draw_ui(screen)
        dyn_screen.pgui3.draw_ui(screen)
        dyn_screen.tooltip_handler()
        pygame.display.flip()

        if fps_check:
            print(f"FPS: {dyn_screen.dtime}")
            log.info(f"FPS: {dyn_screen.dtime}")

    temp_remover(); pygame.quit()