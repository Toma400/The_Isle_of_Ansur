from core.graphics.gh_system import bg_screen
from core.graphics.gh_manag import *

def gui_handler(screen, guitype):

    match guitype:

        case "menu":
            bgs = bg_screen() # selects menu panorama

            imgFull(screen, folderpath=bgs[0], imgname=bgs[1])
            imgPut(screen, folderpath="core/assets/visuals/", imgname="logo.png", size_x=70, size_y=16, pos_x=15, pos_y=5, alpha=True)