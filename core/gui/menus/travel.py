from core.graphics.gh_manag import mouseColliderPx, mouseRec, switch_gscr
from core.file_system.theme_manag import FontColour as fCol
from core.data.world.location import getLocation
from core.graphics.text_manag import put_text
from core.gui.manag.langstr import langstring
from core.data.world.location import getDestinations

def travelScreen(screen, guitype, fg_events, pg_events, tev, dyn_screen):
    loc = getLocation(dyn_screen.journey.location)

    dyn_screen.gui("loc__gh_background").full().put(screen) # background sprite

    # buttons
    bex = put_text(screen, text=loc.langstr(),                font_cat="menu", size=35, align_x="right",  pos_x=15, pos_y=10, colour=fCol.BACKGROUND.value)
    bex = put_text(screen, text=langstring("game__gen_back"), font_cat="menu", size=35, align_x="center",           pos_y=85, colour=fCol.ENABLED.value)

    dyn_screen.put_pgui("map__travel_dest")
    if dyn_screen.get_pgui_options("map__travel_dest") == []:
        dyn_screen.set_pgui_element("map__travel_dest", getDestinations(dyn_screen.journey.location))

    #===============================================================
    # EVENTS
    #===============================================================
    if mouseColliderPx(bex[0], bex[1], bex[2], bex[3]):
        put_text(screen, text=langstring("game__gen_back"), font_cat="menu", size=35, align_x="center", pos_y=85, colour=fCol.HOVERED.value)
        if mouseRec(pg_events):
            guitype[0] = switch_gscr(dyn_screen, screen, "location")
            guitype[1] = None
            dyn_screen.set_pgui_element("map__travel_dest", [])
