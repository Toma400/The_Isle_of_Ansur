from core.graphics.gh_manag import mouseColliderPx, mouseRec, switch_gscr, imgLoad
from core.file_system.theme_manag import FontColour as fCol
from core.data.world.location import getLocation
from core.graphics.text_manag import put_text
from core.gui.manag.langstr import langstring

def locationScreen(screen, guitype, fg_events, pg_events, tev, dyn_screen):
    loc = getLocation(dyn_screen.journey.location)

    dyn_screen.gui("loc__gh_background").full().put(screen) # background sprite

    # ---
    put_text(      screen, text=loc.langstr(),                    font_cat="menu", size=38, align_x="right",  pos_x=14, pos_y=50.5, colour=fCol.ENABLED.value)
    put_text(      screen, text="-" * 154,                        font_cat="menu", size=20, align_x="center",           pos_y=54,   colour=fCol.ENABLED.value)
    put_text(      screen, text=dyn_screen.journey.date.asStr(0), font_cat="menu", size=38, align_x="left",   pos_x=14, pos_y=50.5, colour=fCol.ENABLED.value)
    #put_text(      screen, text=dyn_screen.journey.date.asStr(1), font_cat="menu", size=38, align_x="left",   pos_x=14, pos_y=50.5, colour=fCol.ENABLED.value)
    # above TODO: uncomment once space is made
    bch = put_text(screen, text=langstring("loc__bt_character"), font_cat="menu", size=35,                   pos_x=14, pos_y=57.5, colour=fCol.ENABLED.value)  # character
    biv = put_text(screen, text=langstring("loc__bt_inventory"), font_cat="menu", size=35,                   pos_x=30, pos_y=57.5, colour=fCol.DISABLED.value) # inventory
    blc = put_text(screen, text=langstring("loc__bt_location"),  font_cat="menu", size=35, align_x="center",           pos_y=57.5, colour=fCol.DISABLED.value) # location
    bmp = put_text(screen, text=langstring("loc__bt_map"),       font_cat="menu", size=35, align_x="right",  pos_x=30, pos_y=57.5, colour=fCol.ENABLED.value)  # map
    bdr = put_text(screen, text=langstring("loc__bt_diary"),     font_cat="menu", size=35, align_x="right",  pos_x=14, pos_y=57.5, colour=fCol.ENABLED.value)  # diary

    dyn_screen.put_pgui("loc__image")
    dyn_screen.put_pgui("loc__frame_up")
    dyn_screen.put_pgui("loc__frame_down")
    dyn_screen.put_pgui("loc__frame_left")
    dyn_screen.put_pgui("loc__frame_right")
    dyn_screen.put_pgui("loc__frame_cr_lu")
    dyn_screen.put_pgui("loc__frame_cr_ld")
    dyn_screen.put_pgui("loc__frame_cr_ru")
    dyn_screen.put_pgui("loc__frame_cr_rd")
    dyn_screen.put_pgui("loc__clock")
    dyn_screen.put_pgui("loc__tb_descr")

    if dyn_screen.get_pgui_choice("loc__tb_descr") == "":
        dyn_screen.set_pgui_element("loc__tb_descr", loc.descr())
    if dyn_screen.cache.loc_img is None: # set to None to update the image
        dyn_screen.cache.loc_img = loc.img
        dyn_screen.set_pgui_element("loc__image", imgLoad(loc.img))

    #===============================================================
    # EVENTS
    #===============================================================
    if mouseColliderPx(bch[0], bch[1], bch[2], bch[3]):
        put_text(screen, text=langstring("loc__bt_character"), font_cat="menu", size=35, pos_x=14, pos_y=57.5, colour=fCol.HOVERED.value)
        if mouseRec(pg_events):
            guitype[0] = switch_gscr(dyn_screen, screen, "character")
            guitype[1] = None
            dyn_screen.set_pgui_element("loc__tb_descr", "") # resets description

    elif mouseColliderPx(bmp[0], bmp[1], bmp[2], bmp[3]):
        put_text(screen, text=langstring("loc__bt_map"), font_cat="menu", size=35, align_x="right", pos_x=30, pos_y=57.5, colour=fCol.HOVERED.value)
        if mouseRec(pg_events):
            guitype[0] = switch_gscr(dyn_screen, screen, "map")
            guitype[1] = None
            dyn_screen.set_pgui_element("loc__tb_descr", "") # resets description

    elif mouseColliderPx(bdr[0], bdr[1], bdr[2], bdr[3]):
        put_text(screen, text=langstring("loc__bt_diary"), font_cat="menu", size=35, align_x="right", pos_x=14, pos_y=57.5, colour=fCol.HOVERED.value)
        if mouseRec(pg_events):
            guitype[0] = switch_gscr(dyn_screen, screen, "diary")
            guitype[1] = None
            dyn_screen.set_pgui_element("loc__tb_descr", "") # resets description

    dyn_screen.journey.pass_time(dyn_screen.dtime) # let the time pass if game is running