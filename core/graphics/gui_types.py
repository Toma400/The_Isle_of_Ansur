from system.ref_systems.system_ref import SysRef
from core.graphics.text_manag import put_text, put_ftext, langstring
from core.graphics.gh_system import bg_screen
from core.graphics.gh_manag import *

#===========|==================================================================================================
# GUI       | Handles rendering of elements on the screen, putting out respective set of images and texts.
# HANDLER   |
#--------------------------------------------------------------------------------------------------------------
# ARGUMENTS:
#------------
# pg_events | Those used here should ONLY refer to their display functionalities related to actually used GUI
#==============================================================================================================
def gui_handler(screen, guitype, pg_events):

    match guitype:

        case "menu":
            bgs = bg_screen() # selects menu panorama

            imgFull(screen, folderpath=bgs[0], imgname=bgs[1])
            imgPut(screen, folderpath="core/assets/visuals/", imgname="logo.png", size_x=80, size_y=16, pos_x=10, pos_y=3, alpha=True)
            put_text(screen, text=f"{SysRef.status} {SysRef.version}", font_cat="menu", size=20, pos_x=0.5, pos_y=97, colour="#4F3920")

            put_text(screen, text=langstring("menu__button_start"),    font_cat="menu", size=30, pos_x=44, pos_y=28, colour="#654619")
            put_text(screen, text=langstring("menu__button_load"),     font_cat="menu", size=30, pos_x=44, pos_y=34, colour="#654619")
            put_text(screen, text=langstring("menu__button_settings"), font_cat="menu", size=30, pos_x=44, pos_y=40, colour="#654619")
            put_text(screen, text=langstring("menu__button_packs"),    font_cat="menu", size=30, pos_x=44, pos_y=46, colour="#654619")
            put_text(screen, text=langstring("menu__button_exit"),     font_cat="menu", size=30, pos_x=44, pos_y=52, colour="#654619")

            if mouseCollider(44, 28, 54, 31.5):
                put_text(screen, text=langstring("menu__button_start"),    font_cat="menu", size=30, pos_x=44, pos_y=28, colour="#7C613B")
            if mouseCollider(44, 34, 55, 37.5):
                put_text(screen, text=langstring("menu__button_load"),     font_cat="menu", size=30, pos_x=44, pos_y=34, colour="#7C613B")
            if mouseCollider(44, 40, 52.5, 43.5):
                put_text(screen, text=langstring("menu__button_settings"), font_cat="menu", size=30, pos_x=44, pos_y=40, colour="#7C613B")
            if mouseCollider(44, 46, 49.5, 49.5):
                put_text(screen, text=langstring("menu__button_packs"),    font_cat="menu", size=30, pos_x=44, pos_y=46, colour="#7C613B")
            if mouseCollider(44, 52, 48, 55.5):
                put_text(screen, text=langstring("menu__button_exit"),     font_cat="menu", size=30, pos_x=44, pos_y=52, colour="#7C613B")
                for event in pg_events:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: pygame.quit()