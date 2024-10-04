from core.graphics.gh_manag import mouseColliderPx, mouseRec, switch_gscr, imgLoad, revCell
from core.file_system.theme_manag import FontColour as fCol
from core.data.player.origin import getOrigin
from core.data.player.religion import getReligion
from core.data.player.profession import getClass
from core.data.player.race import getRace
from core.graphics.text_manag import put_text
from core.gui.manag.langstr import langstring
from core.gui.manag.pc import toPxX, toPxY
from os.path import exists

av_spacing = revCell(toPxX(12) + toPxY(30), "x") # based on `pgui_objects` placement for `avatar` element)

def characterScreen(screen, guitype, fg_events, pg_events, tev, dyn_screen):

    dyn_screen.gui("loc__gh_background").full().put(screen) # background sprite

    put_text(screen, text=dyn_screen.journey.get("data.toml | name"),                                                                        font_cat="menu", size=38, align_x="left", pos_x=10, pos_y=10, colour=fCol.ENABLED.value)
    put_text(screen, text=langstring("ccrt__gen_race")     + ": " + getRace(dyn_screen.journey.get("data.toml | race")).langstr(),           font_cat="menu", size=32, align_x="left", pos_x=10, pos_y=18, colour=fCol.ENABLED.value)
    put_text(screen, text=langstring("ccrt__gen_class")    + ": " + getClass(dyn_screen.journey.get("data.toml | class")).langstr(),         font_cat="menu", size=32, align_x="left", pos_x=10, pos_y=24, colour=fCol.ENABLED.value)
    put_text(screen, text=langstring("ccrt__gen_religion") + ": " + getReligion(dyn_screen.journey.get("player.toml | religion")).langstr(), font_cat="menu", size=32, align_x="left", pos_x=10, pos_y=30, colour=fCol.ENABLED.value)

    agl = put_text(screen,     text=langstring("char__av_gall"),  font_cat="menu", size=35, align_x="right", pos_x=av_spacing, pos_y=10, colour=fCol.DISABLED.value)
    if dyn_screen.cache.char_he == 0: # history edit switch
        hsw = put_text(screen, text=langstring("char__his_edit"), font_cat="menu", size=35, align_x="right", pos_x=av_spacing, pos_y=18, colour=fCol.ENABLED.value)
    else:
        hsw = put_text(screen, text=langstring("char__his_save"), font_cat="menu", size=35, align_x="right", pos_x=av_spacing, pos_y=18, colour=fCol.ENABLED.value)

    bog = put_text(screen, text=langstring("ccrt__gen_origin"), font_cat="menu", size=32, pos_x=10, endpos_x=20, pos_y=44, colour=fCol.DISABLED.value) # origin switch
    bat = put_text(screen, text=langstring("char__attrs"),      font_cat="menu", size=32, pos_x=25, endpos_x=35, pos_y=44, colour=fCol.DISABLED.value) # attributes switch
    bsk = put_text(screen, text=langstring("char__skills"),     font_cat="menu", size=32, pos_x=40, endpos_x=50, pos_y=44, colour=fCol.DISABLED.value) # skills switch

    bex = put_text(screen,     text=langstring("game__gen_back"), font_cat="menu", size=35, align_x="center",                  pos_y=85, colour=fCol.ENABLED.value)

    dyn_screen.put_pgui("chmn__avatar")
    dyn_screen.put_pgui("chmn__history")

    if dyn_screen.cache.char_mn is None:
        dyn_screen.cache.char_mn = ""
        if exists(f"saves/{dyn_screen.journey.name}/buffer/avatar.png"):
            dyn_screen.set_pgui_element("chmn__avatar",  imgLoad(f"saves/{dyn_screen.journey.name}/buffer/avatar.png", alpha=True))
            dyn_screen.set_pgui_element("chmn__history", dyn_screen.journey.get("player.toml | history"))
        dyn_screen.set_pgui_element("chmn__origin", getOrigin(dyn_screen.journey.get("data.toml | origin")).descr())
        # TODO: attrs filling
        # TODO: skills filling
        dyn_screen.put_pgui("chmn__none")

    match dyn_screen.cache.char_bm:
        case 0: pass
        case 1: dyn_screen.put_pgui("chmn__origin"); put_text(screen, text=langstring("ccrt__gen_origin"), font_cat="menu", size=32, pos_x=10, endpos_x=20, pos_y=44, colour=fCol.ENABLED.value)
        case 2: dyn_screen.put_pgui("chmn__attrs");  put_text(screen, text=langstring("char__attrs"),      font_cat="menu", size=32, pos_x=25, endpos_x=35, pos_y=44, colour=fCol.ENABLED.value)
        case 3: dyn_screen.put_pgui("chmn__skills"); put_text(screen, text=langstring("char__skills"),     font_cat="menu", size=32, pos_x=40, endpos_x=50, pos_y=44, colour=fCol.ENABLED.value)
        case _: pass

    #===============================================================
    # EVENTS
    #===============================================================
    if mouseColliderPx(bog[0], bog[1], bog[2], bog[3]):
        put_text(screen, text=langstring("ccrt__gen_origin"), font_cat="menu", size=32, pos_x=10, endpos_x=20, pos_y=44, colour=fCol.HOVERED.value)
        if mouseRec(pg_events):
            dyn_screen.cache.char_bm = 1
            dyn_screen.clear_pgui()

    if mouseColliderPx(bat[0], bat[1], bat[2], bat[3]):
        put_text(screen, text=langstring("char__attrs"),      font_cat="menu", size=32, pos_x=25, endpos_x=35, pos_y=44, colour=fCol.HOVERED.value)
        if mouseRec(pg_events):
            dyn_screen.cache.char_bm = 2
            dyn_screen.clear_pgui()

    if mouseColliderPx(bsk[0], bsk[1], bsk[2], bsk[3]):
        put_text(screen, text=langstring("char__skills"),     font_cat="menu", size=32, pos_x=40, endpos_x=50, pos_y=44, colour=fCol.HOVERED.value)
        if mouseRec(pg_events):
            dyn_screen.cache.char_bm = 3
            dyn_screen.clear_pgui()

    elif mouseColliderPx(hsw[0], hsw[1], hsw[2], hsw[3]):
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
            dyn_screen.cache.char_bm = 0             # resets to default
