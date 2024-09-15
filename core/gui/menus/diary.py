from core.graphics.gh_manag import mouseColliderPx, mouseRec, switch_gscr
from core.file_system.theme_manag import FontColour as fCol
from core.graphics.text_manag import put_text
from core.gui.manag.langstr import langstring
from core.data.save_system.buffer import saveBuffer

def diaryScreen(screen, guitype, fg_events, pg_events, tev, dyn_screen):

    dyn_screen.gui("loc__gh_background").full().put(screen) # background sprite

    # buttons
    dsv = put_text(screen, text=langstring("game__diary_save"), font_cat="menu", size=35,                   pos_x=10, pos_y=25, colour=fCol.ENABLED.value)
    bex = put_text(screen, text=langstring("game__gen_back"),   font_cat="menu", size=35, align_x="center",           pos_y=85, colour=fCol.ENABLED.value)
    gex = put_text(screen, text=langstring("menu__back"),       font_cat="menu", size=35,                   pos_x=10, pos_y=35, colour=fCol.ENABLED.value)

    #===============================================================
    # EVENTS
    #===============================================================
    if mouseColliderPx(dsv[0], dsv[1], dsv[2], dsv[3]):
        put_text(screen, text=langstring("game__diary_save"), font_cat="menu", size=35, pos_x=10, pos_y=25, colour=fCol.HOVERED.value)
        if mouseRec(pg_events):
            saveBuffer(dyn_screen.journey.name)

    elif mouseColliderPx(bex[0], bex[1], bex[2], bex[3]):
        put_text(screen, text=langstring("game__gen_back"), font_cat="menu", size=35, align_x="center", pos_y=85, colour=fCol.HOVERED.value)
        if mouseRec(pg_events):
            guitype[0] = switch_gscr(dyn_screen, screen, "location")
            guitype[1] = None

    elif mouseColliderPx(gex[0], gex[1], gex[2], gex[3]):
        put_text(screen, text=langstring("menu__back"), font_cat="menu", size=35, pos_x=10, pos_y=35, colour=fCol.HOVERED.value)
        if mouseRec(pg_events):
            guitype[0] = switch_gscr(dyn_screen, screen, "menu")
            guitype[1] = None
