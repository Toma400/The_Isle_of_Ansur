from core.file_system.theme_manag import FontColour as fCol
from core.graphics.gh_manag import mouseColliderPx, mouseRec, switch_gscr
from core.graphics.text_manag import put_text
from core.gui.manag.langstr import langstring

def loadGame(screen, guitype, fg_events, pg_events, tev, dyn_screen):
    # background sprite
    dyn_screen.gui("menu__gh_background").full().put(screen)

    gtx = put_text(screen, text=langstring("menu__sett_back"), font_cat="menu", size=30, align_x="center", pos_y=92, colour=fCol.ENABLED.value)

    dyn_screen.put_pgui("load__saves")

    # GUI EXPECTED
    # - Image                            | I guess location image? Currently placeholder maybe
    # - Basic data                       | Name, race, class, location, etc.
    # - List of mods                     | It explains itself
    #
    # BUTTONS EXPECTED
    # - Load game                        | Checks integrity and loads if correct
    # - Overwrite from cache             | Writes from cached save
    # - Delete game                      | Deletes the folder

    #===============================================================
    # EVENTS
    #===============================================================
    if mouseColliderPx(gtx[0], gtx[1], gtx[2], gtx[3]):
        put_text(screen, text=langstring("menu__sett_back"), font_cat="menu", size=30, align_x="center", pos_y=92, colour=fCol.HOVERED.value)
        if mouseRec(pg_events):
            guitype[0] = switch_gscr(dyn_screen, screen, "menu")
            guitype[1] = None