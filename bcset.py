import pygame; pygame.init()
from bcs.objects import Screen
from bcs.gui import gui_runner
import pygame_gui

def run():
    dyn_screen = Screen()             # pygame screen
    guitype    = ["login", None]      # gui category being currently used
    guiobj     = dyn_screen.gui       # all objects used later to be drawn
    pg_gui     = dyn_screen.gui_manag # pygame_gui manager

    bcs_events = {
        "sl_in": None
    }

    clock = pygame.time.Clock()
    con = []
    while not con:
        delta  = clock.tick(60) / 1000.0
        screen = dyn_screen.screen  # read-only, but simpler value to be used by most features

        pg_events = pygame.event.get()  # variablised so it can be passed to functions w/o calling more than one per frame
        for event in pg_events:
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                con.append("end")

            if event.type == pygame_gui.UI_SELECTION_LIST_NEW_SELECTION:
                bcs_events["sl_in"] = event.text
            if event.type == pygame_gui.UI_SELECTION_LIST_DROPPED_SELECTION:
                bcs_events["sl_in"] = None

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == guiobj.login__enter and bcs_events["sl_in"] is not None:
                    print (bcs_events["sl_in"])

            pg_gui.process_events(event)


        gui_runner(screen, con, guitype, guiobj, pg_events, dyn_screen) # manager for everything on screen

        pg_gui.update(delta)
        pg_gui.draw_ui(screen)
        pygame.display.flip()

    pygame.quit()

## RUNNING PROCESS ##############################################################################
run()