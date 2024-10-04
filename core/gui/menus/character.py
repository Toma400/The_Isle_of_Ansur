from core.graphics.gh_manag import mouseColliderPx, mouseRec, switch_gscr, imgLoad, revCell
from core.file_system.theme_manag import FontColour as fCol
from core.graphics.text_manag import put_text
from core.gui.manag.langstr import langstring
from core.gui.manag.pc import toPxX, toPxY
from os.path import exists

av_spacing = revCell(toPxX(12) + toPxY(30), "x") # based on `pgui_objects` placement for `avatar` element)

def characterScreen(screen, guitype, fg_events, pg_events, tev, dyn_screen):

    dyn_screen.gui("loc__gh_background").full().put(screen) # background sprite

    put_text(screen, text=dyn_screen.journey.get("data.toml | name"), font_cat="menu", size=38, align_x="left", pos_x=14, pos_y=10, colour=fCol.ENABLED.value)
    # buttons

    agl = put_text(screen,     text=langstring("char__av_gall"),  font_cat="menu", size=35, align_x="right", pos_x=av_spacing, pos_y=10, colour=fCol.DISABLED.value)
    if dyn_screen.cache.char_he == 0: # history edit switch
        hsw = put_text(screen, text=langstring("char__his_edit"), font_cat="menu", size=35, align_x="right", pos_x=av_spacing, pos_y=18, colour=fCol.ENABLED.value)
    else:
        hsw = put_text(screen, text=langstring("char__his_save"), font_cat="menu", size=35, align_x="right", pos_x=av_spacing, pos_y=18, colour=fCol.ENABLED.value)

    bex = put_text(screen,     text=langstring("game__gen_back"), font_cat="menu", size=35, align_x="center",                  pos_y=85, colour=fCol.ENABLED.value)

    dyn_screen.put_pgui("chmn__avatar")
    dyn_screen.put_pgui("chmn__history")

    if dyn_screen.cache.char_mn is None:
        dyn_screen.cache.char_mn = ""
        if exists(f"saves/{dyn_screen.journey.name}/buffer/avatar.png"):
            dyn_screen.set_pgui_element("chmn__avatar",  imgLoad(f"saves/{dyn_screen.journey.name}/buffer/avatar.png", alpha=True))
            dyn_screen.set_pgui_element("chmn__history", dyn_screen.journey.get("player.toml | history"))

    #===============================================================
    # EVENTS
    #===============================================================
    if mouseColliderPx(hsw[0], hsw[1], hsw[2], hsw[3]):
        if dyn_screen.cache.char_he == 0:
            put_text(screen, text=langstring("char__his_edit"), font_cat="menu", size=35, align_x="right", pos_x=av_spacing, pos_y=18, colour=fCol.HOVERED.value)
        else:
            put_text(screen, text=langstring("char__his_save"), font_cat="menu", size=35, align_x="right", pos_x=av_spacing, pos_y=18, colour=fCol.HOVERED.value)

        if mouseRec(pg_events):
            if dyn_screen.cache.char_he == 0:
                dyn_screen.pgui_enable("chmn__history")
                dyn_screen.cache.char_he = 1
            else: # save
                dyn_screen.pgui_disable("chmn__history")
                dyn_screen.cache.char_he = 0
                dyn_screen.journey.set("player.toml | history", f'''{dyn_screen.get_pgui_choice("chmn__history")}''')

    elif mouseColliderPx(bex[0], bex[1], bex[2], bex[3]):
        put_text(screen, text=langstring("game__gen_back"), font_cat="menu", size=35, align_x="center", pos_y=85, colour=fCol.HOVERED.value)
        if mouseRec(pg_events):
            guitype[0] = switch_gscr(dyn_screen, screen, "location")
            guitype[1] = None
            dyn_screen.cache.char_mn = None # allows for further refresh
            dyn_screen.pgui_disable("chmn__history") # resets to default
            dyn_screen.cache.char_he = 0             # resets to default
