from bcs.objects import Screen, GUI_Helper
from bcs.operators import langstr, cells
import pygame, pygame_gui

def gui_runner(screen, con, guitype, guiobj, pg_events, dyn_screen: Screen):

    match guitype:

        case "menu":

            #if GUI_Helper.is_clicked(pg_events)["login__enter"]: print ("Hello!")
            print ("!")