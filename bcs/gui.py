from bcs.objects import Screen, GUI_Helper
from bcs.operators import langstr, cells
import pygame, pygame_gui

def event_runner(con, guitype, pg_events, bcs_events, dyn_screen):
    guiobj = dyn_screen.gui        # all objects used later to be drawn
    pg_gui = dyn_screen.gui_manag  # pygame_gui manager

    for event in pg_events:
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            con.append("end")

        if event.type == pygame_gui.UI_SELECTION_LIST_NEW_SELECTION:
            bcs_events["sl_lbox"] = event.ui_element

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == guiobj.login__enter and bcs_events["sl_lbox"].get_single_selection() is not None:
                print(bcs_events["sl_lbox"].get_single_selection())
                guitype[0] = "logged"; dyn_screen.guitype_switch(guitype[0])

        pg_gui.process_events(event)


def gui_runner(screen, con, guitype, guiobj, pg_events, dyn_screen: Screen):

    match guitype:

        case "menu":

            #if GUI_Helper.is_clicked(pg_events)["login__enter"]: print ("Hello!")
            print ("!")