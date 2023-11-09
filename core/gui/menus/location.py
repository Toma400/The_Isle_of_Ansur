from core.graphics.gh_manag import mouseColliderPx, mouseRec, switch_gscr
from core.file_system.theme_manag import FontColour as fCol
from core.data.world.location import getLocation
from core.graphics.text_manag import put_text
from core.gui.manag.langstr import langstring

def locationScreen(screen, guitype, fg_events, pg_events, tev, dyn_screen):
    # background sprite
    dyn_screen.gui("menu__gh_background").full().put(screen)
    loc = getLocation(dyn_screen.journey.location)

    gtx = put_text(screen, text=langstring("menu__sett_back"), font_cat="menu", size=30, align_x="center", pos_y=92, colour=fCol.ENABLED.value)
    put_text      (screen, text=loc.langstr(),                 font_cat="menu", size=35, align_x="center", pos_y=1,  colour=fCol.ENABLED.value)

    #===============================================================
    # EVENTS
    #===============================================================
    if mouseColliderPx(gtx[0], gtx[1], gtx[2], gtx[3]):
        put_text(screen, text=langstring("menu__sett_back"), font_cat="menu", size=30, align_x="center", pos_y=92, colour=fCol.HOVERED.value)
        if mouseRec(pg_events):
            guitype[0] = switch_gscr(dyn_screen, screen, "menu")
            guitype[1] = None