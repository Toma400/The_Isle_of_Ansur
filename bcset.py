import pygame; pygame.init()
from bcs.objects import Screen
from bcs.gui import gui_runner, event_runner
import pygame_gui

def run():
    guitype    = ["login", None]      # gui category being currently used
    dyn_screen = Screen(guitype[0])   # pygame screen
    guiobj     = dyn_screen.gui       # all objects used later to be drawn
    pg_gui     = dyn_screen.gui_manag # pygame_gui manager

    bcs_events = {
        "sl_lbox": None     # selected listbox
    }

    clock = pygame.time.Clock()
    con = []
    while not con:
        delta  = clock.tick(60) / 1000.0
        screen = dyn_screen.screen  # read-only, but simpler value to be used by most features

        pg_events = pygame.event.get()  # variablised so it can be passed to functions w/o calling more than one per frame

        gui_runner(screen, con, guitype, guiobj, pg_events, dyn_screen) # manager for everything on screen
        event_runner(con, guitype, pg_events, bcs_events, dyn_screen)

        pg_gui.update(delta)
        pg_gui.draw_ui(screen)
        pygame.display.flip()

    pygame.quit()

## RUNNING PROCESS ##############################################################################
run()