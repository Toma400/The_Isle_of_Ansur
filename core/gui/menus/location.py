from core.graphics.gh_manag import mouseColliderPx, mouseRec, switch_gscr, imgLoad
from core.file_system.theme_manag import FontColour as fCol
from core.data.world.location import getLocation
from core.graphics.text_manag import put_text
from core.gui.manag.langstr import langstring

def locationScreen(screen, guitype, fg_events, pg_events, tev, dyn_screen):
    loc = getLocation(dyn_screen.journey.location)

    dyn_screen.gui("loc__gh_background").full().put(screen) # background sprite

    # ---
    put_text(      screen, text=loc.langstr(),                 font_cat="menu", size=38, align_x="right",  pos_x=14, pos_y=49.5, colour=fCol.ENABLED.value)
    put_text(      screen, text="-" * 154,                     font_cat="menu", size=20, align_x="center",           pos_y=53,   colour=fCol.ENABLED.value)
    # buttons
    bch = put_text(screen, text=langstring("loc__bt_character"), font_cat="menu", size=35,                   pos_x=14, pos_y=56.5, colour=fCol.DISABLED.value) # character
    biv = put_text(screen, text=langstring("loc__bt_inventory"), font_cat="menu", size=35,                   pos_x=30, pos_y=56.5, colour=fCol.DISABLED.value) # inventory
    blc = put_text(screen, text=langstring("loc__bt_location"),  font_cat="menu", size=35, align_x="center",           pos_y=56.5, colour=fCol.DISABLED.value) # location
    bmp = put_text(screen, text=langstring("loc__bt_map"),       font_cat="menu", size=35, align_x="right",  pos_x=30, pos_y=56.5, colour=fCol.DISABLED.value) # map
    bdr = put_text(screen, text=langstring("loc__bt_diary"),     font_cat="menu", size=35, align_x="right",  pos_x=14, pos_y=56.5, colour=fCol.DISABLED.value) # diary

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
    dyn_screen.set_pgui_element("loc__image", imgLoad(loc.img))

    #===============================================================
    # EVENTS
    #===============================================================
    if mouseColliderPx(bdr[0], bdr[1], bdr[2], bdr[3]):
        if mouseRec(pg_events):
            guitype[0] = switch_gscr(dyn_screen, screen, "menu")
            guitype[1] = None