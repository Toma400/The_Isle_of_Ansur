from core.graphics.gh_manag import mouseColliderPx, mouseRec, switch_gscr
from core.file_system.theme_manag import FontColour as fCol
from core.data.world.location import getLocation
from core.graphics.text_manag import put_text
from core.gui.manag.langstr import langstring
from core.data.world.location import getDestinations, checkDestination, getDestinationDescr, travelTo

def travelScreen(screen, guitype, fg_events, pg_events, tev, dyn_screen):
    loc = getLocation(dyn_screen.journey.location)

    dyn_screen.gui("loc__gh_background").full().put(screen) # background sprite

    # travel vars (possible/colour)
    trvp = checkDestination(dyn_screen, dyn_screen.get_pgui_choice("map__travel_dest"))
    trvc = fCol.DISABLED.value if trvp is False else fCol.ENABLED.value

    put_text(screen, text=loc.langstr(), font_cat="menu", size=35, align_x="right", pos_x=15, pos_y=10, colour=fCol.BACKGROUND.value)
    put_text(screen, text="-" * 50,      font_cat="menu", size=20, align_x="right", pos_x=15, pos_y=15, colour=fCol.ENABLED.value)
    # buttons
    trv = put_text(screen, text=langstring("game__map_travel"), font_cat="menu", size=35, align_x="right",  pos_x=15, pos_y=20, colour=trvc)
    bex = put_text(screen, text=langstring("game__gen_back"),   font_cat="menu", size=35, align_x="center",           pos_y=85, colour=fCol.ENABLED.value)

    dyn_screen.put_pgui("map__travel_dest")
    dyn_screen.put_pgui("map__travel_descr")

    if dyn_screen.get_pgui_options("map__travel_dest") == []:
        dyn_screen.set_pgui_element("map__travel_dest", getDestinations(dyn_screen, dyn_screen.journey.location))

    if dyn_screen.get_pgui_choice("map__travel_dest") is not None:
        dyn_screen.set_pgui_element("map__travel_descr", getDestinationDescr(dyn_screen, dyn_screen.get_pgui_choice("map__travel_dest")))
    else: dyn_screen.set_pgui_element("map__travel_descr", "") # clear the menu

    #===============================================================
    # EVENTS
    #===============================================================
    if mouseColliderPx(trv[0], trv[1], trv[2], trv[3]) and trvp:
        put_text(screen, text=langstring("game__map_travel"), font_cat="menu", size=35, align_x="right", pos_x=15, pos_y=20, colour=fCol.HOVERED.value)
        if mouseRec(pg_events):
            travelTo(dyn_screen, dyn_screen.get_pgui_choice("map__travel_dest"))
            guitype[0] = switch_gscr(dyn_screen, screen, "location")
            guitype[1] = None
            # ^ those two above can be removed, but I thought travel should not keep us on map, as to make it *important* and not speedrun jumping through locations
            #   that said, ideally there should be some screen in between, with encounters or something (but that's far future)
            dyn_screen.set_pgui_element("map__travel_dest", []) # should be kept, will refresh destinations either way
            dyn_screen.cache.loc_img = None                     # let location screen be refreshed once

    elif mouseColliderPx(bex[0], bex[1], bex[2], bex[3]):
        put_text(screen, text=langstring("game__gen_back"), font_cat="menu", size=35, align_x="center", pos_y=85, colour=fCol.HOVERED.value)
        if mouseRec(pg_events):
            guitype[0] = switch_gscr(dyn_screen, screen, "location")
            guitype[1] = None
            dyn_screen.set_pgui_element("map__travel_dest", [])
