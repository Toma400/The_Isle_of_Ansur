from core.graphics.gh_manag import mouseColliderPx, mouseRec, switch_gscr
from core.file_system.theme_manag import FontColour as fCol
from core.graphics.text_manag import put_text
from core.gui.manag.langstr import langstring

def diaryScreen(screen, guitype, fg_events, pg_events, tev, dyn_screen):

    dyn_screen.gui("loc__gh_background").full().put(screen) # background sprite

    # buttons
    bex = put_text(screen, text=langstring("menu__back"), font_cat="menu", size=35, align_x="center", pos_y=85, colour=fCol.ENABLED.value)

    #===============================================================
    # EVENTS
    #===============================================================
    if mouseColliderPx(bex[0], bex[1], bex[2], bex[3]):
        put_text(screen, text=langstring("menu__back"), font_cat="menu", size=35, align_x="center", pos_y=85, colour=fCol.HOVERED.value)
        if mouseRec(pg_events):
            guitype[0] = switch_gscr(dyn_screen, screen, "menu")
            guitype[1] = None
