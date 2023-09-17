from core.graphics.text_manag import put_abstext, put_text, langstring, Text
from core.file_system.theme_manag import FontColour as fCol
from core.file_system.set_manag import set_change, def_set
from core.file_system.repo_manag import logs_deleting
from core.graphics.gh_manag import *

def upd_click(upd, pgv): return mouseColliderPx(upd[0], upd[1], upd[2], upd[3]) and mouseRec(pgv)
#===========|==================================================================================================
# GUI       | Handles rendering of elements on the screen, putting out respective set of images and texts.
# HANDLER   |
#--------------------------------------------------------------------------------------------------------------
# ARGUMENTS:
#------------
# pg_events | Those used here should ONLY refer to their display functionalities related to actually used GUI
#==============================================================================================================
def gui_handler(screen, guitype, fg_events, pg_events, tev, dyn_screen):

    match guitype[0]:

        #==============================================================================================================
        case "menu":

            dyn_screen.gui("menu__gh_panorama").put(screen, "full_")
            dyn_screen.gui("menu__gh_logo").put(screen)

            if dyn_screen.update and scx("vch"):
                upd = put_text(screen, text=langstring("menu__update"), font_cat="menu", size=22, align_x="center", pos_y=96, colour=fCol.OTHER.value)
                if upd_click(upd, pg_events): update() # GitHub repo
            put_abstext(screen, text=f"{sysref('status')} {sysref('version')}", font_cat="menu", size=22, pos_x=0.5, pos_y=96, colour=fCol.BACKGROUND.value)

            gt1 = put_text(screen, text=langstring("menu__button_start"),    font_cat="menu", size=30, align_x="center", pos_y=28, colour=fCol.ENABLED.value)
            gt2 = put_text(screen, text=langstring("menu__button_load"),     font_cat="menu", size=30, align_x="center", pos_y=34, colour=fCol.DISABLED.value)
            gt3 = put_text(screen, text=langstring("menu__button_arena"),    font_cat="menu", size=30, align_x="center", pos_y=40, colour=fCol.DISABLED.value)
            gt4 = put_text(screen, text=langstring("menu__button_settings"), font_cat="menu", size=30, align_x="center", pos_y=46, colour=fCol.ENABLED.value)
            gt5 = put_text(screen, text=langstring("menu__button_packs"),    font_cat="menu", size=30, align_x="center", pos_y=52, colour=fCol.DISABLED.value)
            gt6 = put_text(screen, text=langstring("menu__button_exit"),     font_cat="menu", size=30, align_x="center", pos_y=58, colour=fCol.ENABLED.value)

            #gt7 = Text(text=langstring("menu__button_exit"),     fonts="menu", size=30, pos=(50,64)).colour(tcol="#4E3510").put(screen)
            #gt7 = Text(text=langstring("menu__button_settings"), fonts="menu", size=30, pos=(50,70)).colour(tcol="#4E3510").put(screen)
            #gt7 = Text(text=langstring("menu__button_packs"),    fonts="menu", size=30, pos=(50,76)).colour(tcol="#4E3510").put(screen)

            #==================================================
            # hovering & clicking events
            if mouseColliderPx(gt1[0], gt1[1], gt1[2], gt1[3]):
                put_text(screen, text=langstring("menu__button_start"), font_cat="menu", size=30, align_x="center", pos_y=28, colour=fCol.HOVERED.value)
                if mouseRec(pg_events):
                    guitype[0] = switch_gscr(dyn_screen, screen, "new_game")
                    guitype[1] = switch_gscr(dyn_screen, screen, "gender")

            elif mouseColliderPx(gt2[0], gt2[1], gt2[2], gt2[3]):
                #put_text(screen, text=langstring("menu__button_load"), font_cat="menu", size=30, align_x="center", pos_y=34, colour="#7C613B")
                pass
            elif mouseColliderPx(gt3[0], gt3[1], gt3[2], gt3[3]):
                #put_text(screen, text=langstring("menu__button_arena"), font_cat="menu", size=30, align_x="center", pos_y=40, colour="#7C613B")
                pass

            elif mouseColliderPx(gt4[0], gt4[1], gt4[2], gt4[3]):
                put_text(screen, text=langstring("menu__button_settings"), font_cat="menu", size=30, align_x="center", pos_y=46, colour="#7C613B")
                if mouseRec(pg_events):
                    guitype[0] = switch_gscr(dyn_screen, screen, "settings")

            elif mouseColliderPx(gt5[0], gt5[1], gt5[2], gt5[3]):
                #put_text(screen, text=langstring("menu__button_packs"), font_cat="menu", size=30, align_x="center", pos_y=52, colour="#7C613B")
                #if mouseRec(pg_events):
                #    guitype[0] = switch_gscr(dyn_screen, screen, "pack_manag")
                pass

            elif mouseColliderPx(gt6[0], gt6[1], gt6[2], gt6[3]):
                put_text(screen, text=langstring("menu__button_exit"), font_cat="menu", size=30, align_x="center", pos_y=58, colour="#7C613B")
                if mouseRec(pg_events):
                    tev.append("end")

        #==============================================================================================================
        case "settings":
            dyn_screen.gui("menu__gh_background").full().put(screen)

            put_text(screen, text=langstring("menu__button_settings"),    font_cat="menu", size=35, align_x="center", pos_y=1, colour="#4E3510")
            gt1 = put_text(screen, text=langstring("menu__sett_general"), font_cat="menu", size=30, pos_x=5, pos_y=12, colour="#4E3510")
            gt2 = put_text(screen, text=langstring("menu__sett_tech"),    font_cat="menu", size=30, pos_x=5, pos_y=22, colour="#4E3510")
            gtx = put_text(screen, text=langstring("menu__sett_back"),    font_cat="menu", size=30, pos_x=5, pos_y=92, colour="#4E3510")

            #==================================================
            # hovering & clicking events
            if mouseColliderPx(gt1[0], gt1[1], gt1[2], gt1[3]):
                put_text(screen, text=langstring("menu__sett_general"), font_cat="menu", size=30, pos_x=5, pos_y=12, colour="#7C613B")
                if mouseRec(pg_events):
                    guitype[1] = switch_gscr(dyn_screen, screen, "settings_general")

            elif mouseColliderPx(gt2[0], gt2[1], gt2[2], gt2[3]):
                put_text(screen, text=langstring("menu__sett_tech"), font_cat="menu", size=30, pos_x=5, pos_y=22, colour="#7C613B")
                if mouseRec(pg_events):
                    guitype[1] = switch_gscr(dyn_screen, screen, "settings_tech")

            elif mouseColliderPx(gtx[0], gtx[1], gtx[2], gtx[3]):
                put_text(screen, text=langstring("menu__sett_back"), font_cat="menu", size=30, pos_x=5, pos_y=92, colour="#7C613B")
                if mouseRec(pg_events):
                    guitype[0] = switch_gscr(dyn_screen, screen, "menu")
                    guitype[1] = None

            #==================================================
            # submenu handler
            match guitype[1]:
                case "settings_general":
                    put_text(screen, text=langstring("menu__sett_general"), font_cat="menu", size=30, pos_x=5, pos_y=12, colour="#7C613B")

                    gt1rs = put_text(screen, text=langstring("menu__sett_general_res"),     font_cat="menu", size=30, align_x="right", pos_x=20, pos_y=12, colour="#4E3510")
                    gt1ln = put_text(screen, text=langstring("menu__sett_general_lang"),    font_cat="menu", size=30, align_x="right", pos_x=20, pos_y=20, colour="#4E3510")
                    gt1ms = put_text(screen, text=langstring("menu__sett_general_music"),   font_cat="menu", size=30, align_x="right", pos_x=20, pos_y=28, colour="#4E3510")

                    # settings values
                    res_ratio = str(scx("svx")) + " : " + str(scx("svy"))
                    put_text(screen, text=res_ratio,                font_cat="menu", size=30, pos_x=82, pos_y=12, colour="#1A5856")  # resolution
                    put_text(screen, text=langstring("lang__name"), font_cat="menu", size=30, pos_x=82, pos_y=20, colour="#1A5856")  # language
                    put_text(screen, text=str(scx("sndv")),         font_cat="menu", size=30, pos_x=82, pos_y=28, colour="#1A5856")  # music volume

                    # ==================================================
                    # hovering & clicking events
                    if mouseColliderPx(gt1rs[0], gt1rs[1], gt1rs[2], gt1rs[3]):
                        put_text(screen, text=langstring("menu__sett_general_res"), font_cat="menu", size=30, align_x="right", pos_x=20, pos_y=12, colour="#7C613B")
                        if mouseRec(pg_events, 1):
                            from win32api import GetSystemMetrics
                            if scx("svx") < GetSystemMetrics(0): set_change("res_x", 100)       # if not full screen, increase x size by 100
                            else:                                set_change("res_x", "set=400") # if full screen reached, set x size to 0
                            screen = dyn_screen.reset() # resets the screen
                        elif mouseRec(pg_events, 3):
                            from win32api import GetSystemMetrics
                            if scx("svy") < GetSystemMetrics(1): set_change("res_y", 100)       # if not full screen, increase x size by 100
                            else:                                set_change("res_y", "set=400") # if full screen reached, set x size to 0
                            screen = dyn_screen.reset() # resets the screen
                        elif mouseRec(pg_events, 2):
                            from win32api import GetSystemMetrics
                            if res_ratio != "1000 : 700": set_change("res_x", "set=1000"); set_change("res_y", "set=700") # changes res to default
                            else:                         set_change("res_x", f"set={GetSystemMetrics(0)}"); set_change("res_y", f"set={GetSystemMetrics(1)}") # changes to full screen
                            screen = dyn_screen.reset() # resets the screen

                    elif mouseColliderPx(gt1ln[0], gt1ln[1], gt1ln[2], gt1ln[3]):
                        put_text(screen, text=langstring("menu__sett_general_lang"), font_cat="menu", size=30, align_x="right", pos_x=20, pos_y=20, colour="#7C613B")
                        if mouseRec(pg_events):
                            set_change("language")
                        elif mouseRec(pg_events, 3):
                            set_change("language", "rev")

                    elif mouseColliderPx(gt1ms[0], gt1ms[1], gt1ms[2], gt1ms[3]):
                        put_text(screen, text=langstring("menu__sett_general_music"), font_cat="menu", size=30, align_x="right", pos_x=20, pos_y=28, colour="#7C613B")
                        if mouseRec(pg_events):
                            set_change("sound", 1); fg_events.append("SNDV_CHG")
                        elif mouseRec(pg_events, 3):
                            if scx("sndv") > 0: set_change("sound", -1); fg_events.append("SNDV_CHG")
                        elif mouseRec(pg_events, 2):
                            if scx("sndv") != 0: # turn off the music
                                set_change("sound", "set=0"); fg_events.append("SNDV_CHG")
                            else: # set volume to default
                                dfsd = def_set("sound")
                                set_change("sound", f"set={dfsd}"); fg_events.append("SNDV_CHG")

                case "settings_tech":
                    put_text(screen, text=langstring("menu__sett_tech"), font_cat="menu", size=30, pos_x=5, pos_y=22, colour="#7C613B")
                    lbmode = scx("lbmd")
                    if lbmode == "sized": sm1col = "#4F4C49"; sm2col = "#4E3510"
                    else:                 sm1col = "#4E3510"; sm2col = "#4F4C49"

                    gt2lu = put_text(screen, text=langstring("menu__sett_tech_legacy"),    font_cat="menu", size=30, align_x="right", pos_x=20, pos_y=12, colour="#4E3510")
                    gt2gl = put_text(screen, text=langstring("menu__sett_tech_log_limit"), font_cat="menu", size=30, align_x="right", pos_x=20, pos_y=20, colour="#4E3510")
                    gt2gr = put_text(screen, text=langstring("menu__sett_tech_log_rv"),    font_cat="menu", size=30, align_x="right", pos_x=20, pos_y=28, colour="#4E3510")
                    gt2lb = put_text(screen, text=langstring("menu__sett_tech_listbox"),   font_cat="menu", size=30, align_x="right", pos_x=20, pos_y=36, colour="#4E3510")
                    gt2la = put_text(screen, text=langstring("menu__sett_tech_lb_amount"), font_cat="menu", size=30, align_x="right", pos_x=20, pos_y=44,    colour=sm1col)
                    gt2ls = put_text(screen, text=langstring("menu__sett_tech_lb_size"),   font_cat="menu", size=30, align_x="right", pos_x=20, pos_y=52,    colour=sm2col)
                    gt2ts = put_text(screen, text=langstring("menu__sett_tech_text_size"), font_cat="menu", size=30, align_x="right", pos_x=20, pos_y=60, colour="#4E3510")
                    gt2vn = put_text(screen, text=langstring("menu__sett_tech_ver_notif"), font_cat="menu", size=30, align_x="right", pos_x=20, pos_y=68, colour="#4E3510")

                    # settings values
                    if scx("legu"): put_text(screen, text=langstring("gen__enabled"), font_cat="menu", size=30, pos_x=82, pos_y=12, colour="#1A5856") # legacy unpacking
                    else: put_text(screen,    text=langstring("gen__disabled"),       font_cat="menu", size=30, pos_x=82, pos_y=12, colour="#1A5856")
                    if scx("vch"): put_text(screen, text=langstring("gen__enabled"),  font_cat="menu", size=30, pos_x=82, pos_y=68, colour="#1A5856") # version notification
                    else: put_text(screen,    text=langstring("gen__disabled"),       font_cat="menu", size=30, pos_x=82, pos_y=68, colour="#1A5856")
                    put_text(screen,          text=str(scx("lglm")),                  font_cat="menu", size=30, pos_x=82, pos_y=20, colour="#1A5856") # log limit number
                    put_text(screen,          text=langstring(f"gen__{lbmode}"),      font_cat="menu", size=30, pos_x=82, pos_y=36, colour="#1A5856") # listbox mode
                    put_text(screen,          text=str(scx("lbam")),                  font_cat="menu", size=30, pos_x=82, pos_y=44, colour="#1A5856") # listbox elements amount
                    put_text(screen,          text=str(scx("lbsz")),                  font_cat="menu", size=30, pos_x=82, pos_y=52, colour="#1A5856") # listbox elements size
                    put_text(screen,          text=str(scx("txts")),                  font_cat="menu", size=30, pos_x=82, pos_y=60, colour="#1A5856") # text size

                    #==================================================
                    # hovering & clicking events
                    if mouseColliderPx(gt2lu[0], gt2lu[1], gt2lu[2], gt2lu[3]):
                        put_text(screen, text=langstring("menu__sett_tech_legacy"), font_cat="menu", size=30, align_x="right", pos_x=20, pos_y=12, colour="#7C613B")
                        if mouseRec(pg_events):
                            set_change("legacy_unpacking")

                    elif mouseColliderPx(gt2gl[0], gt2gl[1], gt2gl[2], gt2gl[3]):
                        put_text(screen, text=langstring("menu__sett_tech_log_limit"), font_cat="menu", size=30, align_x="right", pos_x=20, pos_y=20, colour="#7C613B")
                        if mouseRec(pg_events):
                            set_change("log_limit", 1)
                        elif mouseRec(pg_events, 3):
                            if scx("lglm") > 1: set_change("log_limit", -1)

                    elif mouseColliderPx(gt2gr[0], gt2gr[1], gt2gr[2], gt2gr[3]):
                        put_text(screen, text=langstring("menu__sett_tech_log_rv"), font_cat="menu", size=30, align_x="right", pos_x=20, pos_y=28, colour="#7C613B")
                        if mouseRec(pg_events):
                            logs_deleting()

                    elif mouseColliderPx(gt2lb[0], gt2lb[1], gt2lb[2], gt2lb[3]):
                        put_text(screen, text=langstring(f"menu__sett_tech_listbox"), font_cat="menu", size=30, align_x="right", pos_x=20, pos_y=36, colour="#7C613B")
                        if mouseRec(pg_events):
                            set_change("listbox_mode")
                        if mouseRec(pg_events, 3):
                            set_change("listbox_mode", "rev")

                    elif mouseColliderPx(gt2la[0], gt2la[1], gt2la[2], gt2la[3]) and lbmode == "proportional":
                        put_text(screen, text=langstring("menu__sett_tech_lb_amount"), font_cat="menu", size=30, align_x="right", pos_x=20, pos_y=44, colour="#7C613B")
                        if mouseRec(pg_events):
                            set_change("listbox_amount", 1)
                        if mouseRec(pg_events, 3):
                            if scx("lbam") > 1: set_change("listbox_amount", -1)
                        if mouseRec(pg_events, 2):
                            set_change("listbox_amount", "set=5")

                    elif mouseColliderPx(gt2ls[0], gt2ls[1], gt2ls[2], gt2ls[3]) and lbmode == "sized":
                        put_text(screen, text=langstring("menu__sett_tech_lb_size"), font_cat="menu", size=30, align_x="right", pos_x=20, pos_y=52, colour="#7C613B")
                        if mouseRec(pg_events):
                            set_change("listbox_size", 0.1)
                        if mouseRec(pg_events, 3):
                            if scx("lbsz") > 0.5: set_change("listbox_size", -0.1)
                        if mouseRec(pg_events, 2):
                            set_change("listbox_size", "set=1.0")

                    elif mouseColliderPx(gt2ts[0], gt2ts[1], gt2ts[2], gt2ts[3]):
                        put_text(screen, text=langstring("menu__sett_tech_text_size"), font_cat="menu", size=30, align_x="right", pos_x=20, pos_y=60, colour="#7C613B")
                        if mouseRec(pg_events):
                            set_change("text_size", 0.1)
                        elif mouseRec(pg_events, 3):
                            if scx("txts") > 0.5: set_change("text_size", -0.1)
                        elif mouseRec(pg_events, 2):
                            set_change("text_size", "set=1.0")

                    elif mouseColliderPx(gt2vn[0], gt2vn[1], gt2vn[2], gt2vn[3]):
                        put_text(screen, text=langstring("menu__sett_tech_ver_notif"), font_cat="menu", size=30, align_x="right", pos_x=20, pos_y=68, colour="#7C613B")
                        if mouseRec(pg_events):
                            set_change("version_checker")

        #==============================================================================================================
        case "pack_manag":
            dyn_screen.gui("menu__gh_background").full().put(screen)

            put_text(screen, text=langstring("menu__button_packs"),       font_cat="menu", size=35, align_x="center", pos_y=1, colour="#4E3510")
            #gt1 = put_text(screen, text=langstring("menu__sett_general"), font_cat="menu", size=30, pos_x=5, pos_y=12, colour="#4E3510")
            #gt2 = put_text(screen, text=langstring("menu__sett_tech"),    font_cat="menu", size=30, pos_x=5, pos_y=22, colour="#4E3510")
            gtx = put_text(screen, text=langstring("menu__sett_back"),    font_cat="menu", size=30, pos_x=5, pos_y=92, colour="#4E3510")

            #==================================================
            # hovering & clicking events
            #if mouseColliderPx(gt1[0], gt1[1], gt1[2], gt1[3]):
            #    put_text(screen, text=langstring("menu__sett_general"), font_cat="menu", size=30, pos_x=5, pos_y=12, colour="#7C613B")
            #    if mouseRec(pg_events):
            #        guitype[1] = switch_gscr(dyn_screen, screen, "settings_general")

            #if mouseColliderPx(gt2[0], gt2[1], gt2[2], gt2[3]):
            #    put_text(screen, text=langstring("menu__sett_tech"), font_cat="menu", size=30, pos_x=5, pos_y=22, colour="#7C613B")
            #    if mouseRec(pg_events):
            #        guitype[1] = switch_gscr(dyn_screen, screen, "settings_tech")

            if mouseColliderPx(gtx[0], gtx[1], gtx[2], gtx[3]):
                put_text(screen, text=langstring("menu__sett_back"), font_cat="menu", size=30, pos_x=5, pos_y=92, colour="#7C613B")
                if mouseRec(pg_events):
                    guitype[0] = switch_gscr(dyn_screen, screen, "menu")
                    guitype[1] = None

        # ==============================================================================================================
        case "new_game":
            ccrt_col = {"active": "#354A07", "not_set": "#4F4C49"}
            dyn_screen.gui("menu__gh_background").full().put(screen)
            #Image("core/assets/visuals/", "menu_background.jpg", (0, 0)).full().put(screen) # probably to delete, as it doesn't work anymore w/ new theme system

            put_text(screen, text=langstring("menu__button_start"),        font_cat="menu", size=35, align_x="center", pos_y=1, colour="#4E3510")
            gtx = put_text(screen, text=langstring("menu__sett_back"),     font_cat="menu", size=30, align_x="center", pos_y=92, colour="#4E3510")

            mn1 = put_text(screen, text=langstring("ccrt__gen_category1"), font_cat="menu", size=30, align_x="left", pos_x=5, pos_y=10, colour=ccrt_col["active"])
            mn2 = put_text(screen, text=langstring("ccrt__gen_category2"), font_cat="menu", size=30, align_x="left", pos_x=5, pos_y=18, colour=ccrt_col["not_set"])
            mn3 = put_text(screen, text=langstring("ccrt__gen_category3"), font_cat="menu", size=30, align_x="left", pos_x=5, pos_y=26, colour=ccrt_col["not_set"])
            mn4 = put_text(screen, text=langstring("ccrt__gen_category4"), font_cat="menu", size=30, align_x="left", pos_x=5, pos_y=34, colour=ccrt_col["not_set"])
            mn5 = put_text(screen, text=langstring("ccrt__gen_category5"), font_cat="menu", size=30, align_x="left", pos_x=5, pos_y=42, colour=ccrt_col["not_set"])
            mn6 = put_text(screen, text=langstring("ccrt__gen_category6"), font_cat="menu", size=30, align_x="left", pos_x=5, pos_y=50, colour=ccrt_col["not_set"])
            mn7 = put_text(screen, text=langstring("ccrt__gen_category7"), font_cat="menu", size=30, align_x="left", pos_x=5, pos_y=58, colour=ccrt_col["not_set"])
            mn8 = put_text(screen, text=langstring("ccrt__gen_category8"), font_cat="menu", size=30, align_x="left", pos_x=5, pos_y=66, colour=ccrt_col["not_set"])
            mn9 = put_text(screen, text=langstring("ccrt__gen_category9"), font_cat="menu", size=30, align_x="left", pos_x=5, pos_y=74, colour=ccrt_col["not_set"])
            # ------------------------------
            # GENDER = male/female
            # RACE   = choice of races
            # CLASS  = choice of classes
            # NAME   = choice of name + avatar (based on race)
            # POINTS = manual
            # RELIG  = choice of religion
            # ORIGIN = choice of origin paths (appendable by mods, possible worldpack inits) + manual biography if you will
            # SETTINGS
            # SUMMARY

            # ==================================================
            # hovering & clicking events
            if mouseColliderPx(gtx[0], gtx[1], gtx[2], gtx[3]):
                put_text(screen, text=langstring("menu__sett_back"), font_cat="menu", size=30, align_x="center", pos_y=92, colour="#7C613B")
                if mouseRec(pg_events):
                    guitype[0] = switch_gscr(dyn_screen, screen, "menu")
                    guitype[1] = None