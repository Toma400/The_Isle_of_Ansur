from core.graphics.text_manag import put_abstext, put_text, put_rectext, langstring
from core.file_system.set_manag import set_change, def_set
from core.file_system.repo_manag import logs_deleting
from core.graphics.gh_manag import *

#===========|==================================================================================================
# GUI       | Handles rendering of elements on the screen, putting out respective set of images and texts.
# HANDLER   |
#--------------------------------------------------------------------------------------------------------------
# ARGUMENTS:
#------------
# pg_events | Those used here should ONLY refer to their display functionalities related to actually used GUI
#==============================================================================================================
def gui_handler(screen, guitype, fg_events, pg_events, tev, bgs):

    match guitype[0]:

        #==============================================================================================================
        case "menu":

            imgFull(screen, folderpath=bgs[0], imgname=bgs[1])
            imgPut(screen, folderpath="core/assets/visuals/", imgname="logo.png", size_x=80, size_y=16, pos_x=10, pos_y=3, alpha=True)
            put_abstext(screen, text=f"{SysRef.status} {SysRef.version}", font_cat="menu", size=20, pos_x=0.5, pos_y=97, colour="#4F3920")

            gt1 = put_text(screen, text=langstring("menu__button_start"),    font_cat="menu", size=30, align_x="center", pos_y=28, colour="#4E3510")
            gt2 = put_text(screen, text=langstring("menu__button_load"),     font_cat="menu", size=30, align_x="center", pos_y=34, colour="#4E3510")
            gt3 = put_text(screen, text=langstring("menu__button_settings"), font_cat="menu", size=30, align_x="center", pos_y=40, colour="#4E3510")
            gt4 = put_text(screen, text=langstring("menu__button_packs"),    font_cat="menu", size=30, align_x="center", pos_y=46, colour="#4E3510")
            gt5 = put_text(screen, text=langstring("menu__button_exit"),     font_cat="menu", size=30, align_x="center", pos_y=52, colour="#4E3510")

            #==================================================
            # hovering & clicking events
            if mouseColliderPx(gt1[0], gt1[1], gt1[2], gt1[3]):
                put_text(screen, text=langstring("menu__button_start"), font_cat="menu", size=30, align_x="center", pos_y=28, colour="#7C613B")
            if mouseColliderPx(gt2[0], gt2[1], gt2[2], gt2[3]):
                put_text(screen, text=langstring("menu__button_load"), font_cat="menu", size=30, align_x="center", pos_y=34, colour="#7C613B")
            if mouseColliderPx(gt3[0], gt3[1], gt3[2], gt3[3]):
                put_text(screen, text=langstring("menu__button_settings"), font_cat="menu", size=30, align_x="center", pos_y=40, colour="#7C613B")
                if mouseRec(pg_events):
                    guitype[0] = switch_scr(screen, "settings")

            if mouseColliderPx(gt4[0], gt4[1], gt4[2], gt4[3]):
                put_text(screen, text=langstring("menu__button_packs"), font_cat="menu", size=30, align_x="center", pos_y=46, colour="#7C613B")
                if mouseRec(pg_events):
                    guitype[0] = switch_scr(screen, "pack_manag")

            if mouseColliderPx(gt5[0], gt5[1], gt5[2], gt5[3]):
                put_text(screen, text=langstring("menu__button_exit"), font_cat="menu", size=30, align_x="center", pos_y=52, colour="#7C613B")
                if mouseRec(pg_events):
                    tev.append("end")

        #==============================================================================================================
        case "settings":
            imgFull(screen, "core/assets/visuals/", "menu_background.jpg")

            put_text(screen, text=langstring("menu__button_settings"),    font_cat="menu", size=35, align_x="center", pos_y=1, colour="#4E3510")
            gt1 = put_text(screen, text=langstring("menu__sett_general"), font_cat="menu", size=30, pos_x=5, pos_y=12, colour="#4E3510")
            gt2 = put_text(screen, text=langstring("menu__sett_tech"),    font_cat="menu", size=30, pos_x=5, pos_y=22, colour="#4E3510")
            gtx = put_text(screen, text=langstring("menu__sett_back"),    font_cat="menu", size=30, pos_x=5, pos_y=92, colour="#4E3510")

            #==================================================
            # hovering & clicking events
            if mouseColliderPx(gt1[0], gt1[1], gt1[2], gt1[3]):
                put_text(screen, text=langstring("menu__sett_general"), font_cat="menu", size=30, pos_x=5, pos_y=12, colour="#7C613B")
                if mouseRec(pg_events):
                    guitype[1] = switch_scr(screen, "settings_general")

            if mouseColliderPx(gt2[0], gt2[1], gt2[2], gt2[3]):
                put_text(screen, text=langstring("menu__sett_tech"), font_cat="menu", size=30, pos_x=5, pos_y=22, colour="#7C613B")
                if mouseRec(pg_events):
                    guitype[1] = switch_scr(screen, "settings_tech")

            if mouseColliderPx(gtx[0], gtx[1], gtx[2], gtx[3]):
                put_text(screen, text=langstring("menu__sett_back"), font_cat="menu", size=30, pos_x=5, pos_y=92, colour="#7C613B")
                if mouseRec(pg_events):
                    guitype[0] = switch_scr(screen, "menu")
                    guitype[1] = None

            #==================================================
            # submenu handler
            match guitype[1]:
                case "settings_general":
                    gt1ln = put_text(screen, text=langstring("menu__sett_general_lang"),    font_cat="menu", size=30, align_x="right", pos_x=15, pos_y=12, colour="#4E3510")
                    gt1ms = put_text(screen, text=langstring("menu__sett_general_music"),   font_cat="menu", size=30, align_x="right", pos_x=15, pos_y=20, colour="#4E3510")

                    # settings values
                    put_text(screen, text=langstring("lang__name"), font_cat="menu", size=30, pos_x=87, pos_y=12, colour="#1A5856")  # language
                    put_text(screen, text=str(scx("sndv")),         font_cat="menu", size=30, pos_x=87, pos_y=20, colour="#1A5856")  # music volume

                    # ==================================================
                    # hovering & clicking events
                    if mouseColliderPx(gt1ln[0], gt1ln[1], gt1ln[2], gt1ln[3]):
                        put_text(screen, text=langstring("menu__sett_general_lang"), font_cat="menu", size=30, align_x="right", pos_x=15, pos_y=12, colour="#7C613B")
                        if mouseRec(pg_events):
                            set_change("language")
                        if mouseRec(pg_events, 3):
                            set_change("language", "rev")

                    if mouseColliderPx(gt1ms[0], gt1ms[1], gt1ms[2], gt1ms[3]):
                        put_text(screen, text=langstring("menu__sett_general_music"), font_cat="menu", size=30, align_x="right", pos_x=15, pos_y=20, colour="#7C613B")
                        if mouseRec(pg_events):
                            set_change("sound", 1); fg_events.append("SNDV_CHG")
                        if mouseRec(pg_events, 3):
                            if scx("sndv") > 0: set_change("sound", -1); fg_events.append("SNDV_CHG")
                        if mouseRec(pg_events, 2):
                            if scx("sndv") != 0: # turn off the music
                                set_change("sound", "set=0"); fg_events.append("SNDV_CHG")
                            else: # set volume to default
                                dfsd = def_set("sound")
                                set_change("sound", f"set={dfsd}"); fg_events.append("SNDV_CHG")

                case "settings_tech":
                    gt2lu = put_text(screen, text=langstring("menu__sett_tech_legacy"),    font_cat="menu", size=30, align_x="right", pos_x=15, pos_y=12, colour="#4E3510")
                    gt2gl = put_text(screen, text=langstring("menu__sett_tech_log_limit"), font_cat="menu", size=30, align_x="right", pos_x=15, pos_y=20, colour="#4E3510")
                    gt2gr = put_text(screen, text=langstring("menu__sett_tech_log_rv"),    font_cat="menu", size=30, align_x="right", pos_x=15, pos_y=28, colour="#4E3510")

                    # settings values
                    if scx("legu"): put_text(screen, text=langstring("gen__enabled"), font_cat="menu", size=30, pos_x=87, pos_y=12, colour="#1A5856") # legacy unpacking
                    else: put_text(screen,    text=langstring("gen__disabled"),       font_cat="menu", size=30, pos_x=87, pos_y=12, colour="#1A5856")
                    put_text(screen,          text=str(scx("lglm")),                  font_cat="menu", size=30, pos_x=87, pos_y=20, colour="#1A5856") # log limit number

                    #==================================================
                    # hovering & clicking events
                    if mouseColliderPx(gt2lu[0], gt2lu[1], gt2lu[2], gt2lu[3]):
                        put_text(screen, text=langstring("menu__sett_tech_legacy"), font_cat="menu", size=30, align_x="right", pos_x=15, pos_y=12, colour="#7C613B")
                        if mouseRec(pg_events):
                            set_change("legacy_unpacking")

                    if mouseColliderPx(gt2gl[0], gt2gl[1], gt2gl[2], gt2gl[3]):
                        put_text(screen, text=langstring("menu__sett_tech_log_limit"), font_cat="menu", size=30, align_x="right", pos_x=15, pos_y=20, colour="#7C613B")
                        if mouseRec(pg_events):
                            set_change("log_limit", 1)
                        if mouseRec(pg_events, 3):
                            if scx("lglm") > 1: set_change("log_limit", -1)

                    if mouseColliderPx(gt2gr[0], gt2gr[1], gt2gr[2], gt2gr[3]):
                        put_text(screen, text=langstring("menu__sett_tech_log_rv"), font_cat="menu", size=30, align_x="right", pos_x=15, pos_y=28, colour="#7C613B")
                        if mouseRec(pg_events):
                            logs_deleting()

        #==============================================================================================================
        case "pack_manag":
            imgFull(screen, "core/assets/visuals/", "menu_background.jpg")

            put_text(screen, text=langstring("menu__button_packs"),       font_cat="menu", size=35, align_x="center", pos_y=1, colour="#4E3510")
            #gt1 = put_text(screen, text=langstring("menu__sett_general"), font_cat="menu", size=30, pos_x=5, pos_y=12, colour="#4E3510")
            #gt2 = put_text(screen, text=langstring("menu__sett_tech"),    font_cat="menu", size=30, pos_x=5, pos_y=22, colour="#4E3510")
            gtx = put_text(screen, text=langstring("menu__sett_back"),    font_cat="menu", size=30, pos_x=5, pos_y=92, colour="#4E3510")

            #==================================================
            # hovering & clicking events
            #if mouseColliderPx(gt1[0], gt1[1], gt1[2], gt1[3]):
            #    put_text(screen, text=langstring("menu__sett_general"), font_cat="menu", size=30, pos_x=5, pos_y=12, colour="#7C613B")
            #    if mouseRec(pg_events):
            #        guitype[1] = switch_scr(screen, "settings_general")

            #if mouseColliderPx(gt2[0], gt2[1], gt2[2], gt2[3]):
            #    put_text(screen, text=langstring("menu__sett_tech"), font_cat="menu", size=30, pos_x=5, pos_y=22, colour="#7C613B")
            #    if mouseRec(pg_events):
            #        guitype[1] = switch_scr(screen, "settings_tech")

            if mouseColliderPx(gtx[0], gtx[1], gtx[2], gtx[3]):
                put_text(screen, text=langstring("menu__sett_back"), font_cat="menu", size=30, pos_x=5, pos_y=92, colour="#7C613B")
                if mouseRec(pg_events):
                    guitype[0] = switch_scr(screen, "menu")
                    guitype[1] = None