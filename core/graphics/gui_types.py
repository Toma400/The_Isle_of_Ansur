from system.ref_systems.system_ref import SysRef
from core.scrolls.text_manag import put_text
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
            put_text(screen, text=f"{SysRef.status} {SysRef.version}", font="ferrum.otf", size=20, pos_x=0.5, pos_y=97, colour="#4F3920")
            #put_text(screen, text=f"Dudu!", font="ferrum.otf", size=20, pos_x=0, pos_y=0, colour="#4F3920")

            for event in pg_events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pass
                    #put_text(screen, text=f"We won that!", font="ferrum.otf", size=20, pos_x=5, pos_y=0, colour="#4F3920")
                if event.type == pygame.MOUSEMOTION and mouseCollider(0, 0, 10, 10):
                    pass
                    #put_text(screen, text=f"{SysRef.status} {SysRef.version}", font="ferrum.otf", size=21, pos_x=0.5, pos_y=97, colour="#654724")