from core.graphics.text_manag import put_abstext, put_text, Text
from core.gui.menus.location import locationScreen
from core.gui.menus.packs import packMenu
from core.gui.menus.load import loadGame
from core.gui.manag.langstr import langstring
from core.file_system.save_manag import listSaves
from core.file_system.theme_manag import FontColour as fCol
from core.file_system.set_manag import set_change, def_set
from core.file_system.repo_manag import logs_deleting
from core.data.player.attributes import getAttributesTupleAdjusted, getAttribute
from core.data.player.skills import getSkillsTupleAdjusted, getSkill
from core.data.player.profession import getClassesTuple, getClass
from core.data.player.race import getRace, getRaceNames
from core.data.player.religion import getReligion
from core.data.player.origin import getOrigin
from core.data.journey import Journey
from core.graphics.gh_manag import *
from os.path import exists

def upd_click(upd, pgv): return mouseColliderPx(upd[0], upd[1], upd[2], upd[3]) and mouseRec(pgv)
developer_mode         = exists(".dev")
packs_err              = os.path.getsize("core/data/pack_manag/pack_errors.yaml") > 0
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
            if packs_err:
                put_text(screen, text=langstring("menu__pack_error"),            font_cat="menu", size=27, align_x="center", pos_y=90, colour=fCol.ERROR.value)
            put_abstext(screen,  text=f"{sysref('status')} {sysref('version')}", font_cat="menu", size=22, pos_x=0.5,        pos_y=96, colour=fCol.BACKGROUND.value)

            gt2c = fCol.DISABLED.value if len(listSaves()) == 0 or packs_err else fCol.ENABLED.value # handles whether button for 'load' is available or not...
            gt1c = fCol.DISABLED.value if packs_err                          else fCol.ENABLED.value # ...and the same while packs have error during verification

            gt1 = put_text(screen, text=langstring("menu__button_start"),    font_cat="menu", size=30, align_x="center", pos_y=28, colour=gt1c)
            gt2 = put_text(screen, text=langstring("menu__button_load"),     font_cat="menu", size=30, align_x="center", pos_y=34, colour=gt2c)
            gt3 = put_text(screen, text=langstring("menu__button_arena"),    font_cat="menu", size=30, align_x="center", pos_y=40, colour=fCol.DISABLED.value)
            gt4 = put_text(screen, text=langstring("menu__button_settings"), font_cat="menu", size=30, align_x="center", pos_y=46, colour=fCol.ENABLED.value)
            gt5 = put_text(screen, text=langstring("menu__button_packs"),    font_cat="menu", size=30, align_x="center", pos_y=52, colour=fCol.DISABLED.value)
            gt6 = put_text(screen, text=langstring("menu__button_exit"),     font_cat="menu", size=30, align_x="center", pos_y=58, colour=fCol.ENABLED.value)

            #gt7 = Text(text=langstring("menu__button_exit"),     fonts="menu", size=30, pos=(50,64)).colour(tcol="#4E3510").put(screen)
            #gt7 = Text(text=langstring("menu__button_settings"), fonts="menu", size=30, pos=(50,70)).colour(tcol="#4E3510").put(screen)
            #gt7 = Text(text=langstring("menu__button_packs"),    fonts="menu", size=30, pos=(50,76)).colour(tcol="#4E3510").put(screen)

            #==================================================
            # hovering & clicking events
            if mouseColliderPx(gt1[0], gt1[1], gt1[2], gt1[3]) and not packs_err:
                put_text(screen, text=langstring("menu__button_start"), font_cat="menu", size=30, align_x="center", pos_y=28, colour=fCol.HOVERED.value)
                if mouseRec(pg_events):
                    guitype[0] = switch_gscr(dyn_screen, screen, "new_game")
                    guitype[1] = switch_gscr(dyn_screen, screen, "gender")

            elif mouseColliderPx(gt2[0], gt2[1], gt2[2], gt2[3]) and not packs_err:
                if len(listSaves()) > 0:
                    put_text(screen, text=langstring("menu__button_load"), font_cat="menu", size=30, align_x="center", pos_y=34, colour="#7C613B")
                    if mouseRec(pg_events):
                        guitype[0] = switch_gscr(dyn_screen, screen, "load")
                        dyn_screen.set_pgui_element("load__saves", listSaves())

            elif mouseColliderPx(gt3[0], gt3[1], gt3[2], gt3[3]) and developer_mode:
                put_text(screen, text=langstring("menu__button_arena"), font_cat="menu", size=30, align_x="center", pos_y=40, colour="#7C613B")
                if mouseRec(pg_events):
                    # placeholder data to test
                    dyn_screen.journey.name     = "Test"
                    dyn_screen.journey.location = "ansur:tutorial"
                    guitype[0] = switch_gscr(dyn_screen, screen, "location")

            elif mouseColliderPx(gt4[0], gt4[1], gt4[2], gt4[3]):
                put_text(screen, text=langstring("menu__button_settings"), font_cat="menu", size=30, align_x="center", pos_y=46, colour="#7C613B")
                if mouseRec(pg_events):
                    guitype[0] = switch_gscr(dyn_screen, screen, "settings")

            elif mouseColliderPx(gt5[0], gt5[1], gt5[2], gt5[3]) and developer_mode:
                put_text(screen, text=langstring("menu__button_packs"), font_cat="menu", size=30, align_x="center", pos_y=52, colour="#7C613B")
                if mouseRec(pg_events):
                   guitype[0] = switch_gscr(dyn_screen, screen, "pack_manag")

            elif mouseColliderPx(gt6[0], gt6[1], gt6[2], gt6[3]):
                put_text(screen, text=langstring("menu__button_exit"), font_cat="menu", size=30, align_x="center", pos_y=58, colour="#7C613B")
                if mouseRec(pg_events):
                    tev.append("end")

        #==============================================================================================================
        case "load":
            loadGame(screen, guitype, fg_events, pg_events, tev, dyn_screen)

        case "location":
            if dyn_screen.journey.name is None or dyn_screen.journey.location is None:
                raise Exception("While entering -locationScreen-, some required player data is not reachable.")
            else:
                locationScreen(screen, guitype, fg_events, pg_events, tev, dyn_screen)

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
                            if res_ratio != "1000 : 700": # changes res to default
                                set_change("res_x", "set=1000"); set_change("res_y", "set=700"); set_change("text_size", "set=1.0")
                            else:                         # changes to full screen
                                set_change("res_x", f"set={GetSystemMetrics(0)}"); set_change("res_y", f"set={GetSystemMetrics(1)}"); set_change("text_size", "set=1.5")
                            screen = dyn_screen.reset() # resets the screen

                    elif mouseColliderPx(gt1ln[0], gt1ln[1], gt1ln[2], gt1ln[3]):
                        put_text(screen, text=langstring("menu__sett_general_lang"), font_cat="menu", size=30, align_x="right", pos_x=20, pos_y=20, colour="#7C613B")
                        if mouseRec(pg_events):
                            set_change("language")
                            dyn_screen.soft_reset()
                        elif mouseRec(pg_events, 3):
                            set_change("language", "rev")
                            dyn_screen.soft_reset()

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
                    if scx("legu"): put_text(screen, text=langstring("gen__enabled"),  font_cat="menu", size=30, pos_x=82, pos_y=12, colour="#1A5856") # legacy unpacking
                    else:           put_text(screen, text=langstring("gen__disabled"), font_cat="menu", size=30, pos_x=82, pos_y=12, colour="#1A5856")
                    if scx("vch"):  put_text(screen, text=langstring("gen__enabled"),  font_cat="menu", size=30, pos_x=82, pos_y=68, colour="#1A5856") # version notification
                    else:           put_text(screen, text=langstring("gen__disabled"), font_cat="menu", size=30, pos_x=82, pos_y=68, colour="#1A5856")
                    put_text(screen, text=str(scx("lglm")),             font_cat="menu", size=30, pos_x=82, pos_y=20, colour="#1A5856") # log limit number
                    put_text(screen, text=langstring(f"gen__{lbmode}"), font_cat="menu", size=30, pos_x=82, pos_y=36, colour="#1A5856") # listbox mode
                    put_text(screen, text=str(scx("lbam")),             font_cat="menu", size=30, pos_x=82, pos_y=44, colour="#1A5856") # listbox elements amount
                    put_text(screen, text=str(scx("lbsz")),             font_cat="menu", size=30, pos_x=82, pos_y=52, colour="#1A5856") # listbox elements size
                    put_text(screen, text=str(scx("txts")),             font_cat="menu", size=30, pos_x=82, pos_y=60, colour="#1A5856") # text size

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
            packMenu(screen, guitype, fg_events, pg_events, tev, dyn_screen)

        # ==============================================================================================================
        case "new_game":
            ccrt_col = {"active": "#354A07", "set": "", "not_set": fCol.DISABLED.value}
            dyn_screen.gui("menu__gh_background").full().put(screen)

            put_text(screen, text=langstring("menu__button_start"),        font_cat="menu", size=35, align_x="center", pos_y=1,  colour="#4E3510")
            gtx = put_text(screen, text=langstring("menu__sett_back"),     font_cat="menu", size=30, align_x="center", pos_y=92, colour="#4E3510")

            mn1 = put_text(screen, text=langstring("ccrt__gen_category1"), font_cat="menu", size=30, align_x="left", pos_x=5, pos_y=10, colour=fCol.ENABLED.value)
            mn2 = put_text(screen, text=langstring("ccrt__gen_category2"), font_cat="menu", size=30, align_x="left", pos_x=5, pos_y=18, colour=ccrt_col["not_set"])
            mn3 = put_text(screen, text=langstring("ccrt__gen_category3"), font_cat="menu", size=30, align_x="left", pos_x=5, pos_y=26, colour=ccrt_col["not_set"])
            mn4 = put_text(screen, text=langstring("ccrt__gen_category4"), font_cat="menu", size=30, align_x="left", pos_x=5, pos_y=34, colour=ccrt_col["not_set"])
            mn5 = put_text(screen, text=langstring("ccrt__gen_category5"), font_cat="menu", size=30, align_x="left", pos_x=5, pos_y=42, colour=ccrt_col["not_set"])
            mn6 = put_text(screen, text=langstring("ccrt__gen_category6"), font_cat="menu", size=30, align_x="left", pos_x=5, pos_y=50, colour=ccrt_col["not_set"])
            mn7 = put_text(screen, text=langstring("ccrt__gen_category7"), font_cat="menu", size=30, align_x="left", pos_x=5, pos_y=58, colour=ccrt_col["not_set"])
            mn8 = put_text(screen, text=langstring("ccrt__gen_category8"), font_cat="menu", size=30, align_x="left", pos_x=5, pos_y=66, colour=ccrt_col["not_set"])
            mn9 = put_text(screen, text=langstring("ccrt__gen_category9"), font_cat="menu", size=30, align_x="left", pos_x=5, pos_y=74, colour=ccrt_col["not_set"])
            # ------------------------------
            # GENDER = male/female/other
            # RACE   = choice of races
            # CLASS  = choice of classes
            # NAME   = choice of name + avatar (based on race)
            # POINTS = manual
            # RELIG  = choice of religion
            # ORIGIN = choice of origin paths (appendable by mods, possible worldpack inits) + manual biography if you will
            # SETTINGS
            # SUMMARY

            # ==================================================
            # visualisation of menu picked/active
            for nm in range(0, 9):
                # visualisation of whether option is possible to click
                if dyn_screen.journey.stages[nm] is True:
                    put_text(screen, text=langstring(f"ccrt__gen_category{nm+2}"), font_cat="menu", size=30, align_x="left", pos_x=5, pos_y=18+(8*nm), colour=fCol.ENABLED.value)
                # visualisation of which option is currently active
                if dyn_screen.journey.stage == nm:
                    if nm >= 1:
                        put_text(screen, text=langstring(f"ccrt__gen_category{nm}"),   font_cat="menu", size=30, align_x="left", pos_x=5, pos_y=2+(8*nm),  colour=fCol.ENABLED.value) # go back
                    put_text(    screen, text=langstring(f"ccrt__gen_category{nm+1}"), font_cat="menu", size=30, align_x="left", pos_x=5, pos_y=10+(8*nm), colour=ccrt_col["active"]) # current

            # https://github.com/Toma400/The_Isle_of_Ansur/commit/5305aef7e9b3b0cce483a30ade7cbc3f1e006e57 <- old (more manual) code for above ^

            #==================================================
            match guitype[1]:
                case "gender":
                    if dyn_screen.journey.stage != 0:
                        dyn_screen.journey.stage = 0
                        dyn_screen.put_pgui("char__lb_gender")
                        dyn_screen.put_pgui("char__tb_gender")

                    gender_choice = dyn_screen.get_pgui_choice("char__lb_gender")
                    if gender_choice is not None:
                        dyn_screen.journey.setInit("gender", gender_choice)
                        dyn_screen.journey.stages[0] = True
                    else:
                        dyn_screen.journey.stages[0] = False

                case "race":
                    if dyn_screen.journey.stage != 1:
                        dyn_screen.journey.stage = 1
                        dyn_screen.put_pgui("char__lb_race")
                        dyn_screen.put_pgui("char__tb_race")

                    race_choice = dyn_screen.get_pgui_choice("char__lb_race")
                    if race_choice is not None:
                        if dyn_screen.journey.inidata["race"] != race_choice: # this check allows for updating once per change (improves performance & get rid of render bug)
                            dyn_screen.journey.setInit("race", race_choice)
                            dyn_screen.set_pgui_element("char__tb_race",  getRace(race_choice).descr())                                    # sets infobox
                            dyn_screen.set_pgui_element("char__lb_class", getClassesTuple(race_choice))                                    # sets class listbox
                            dyn_screen.set_pgui_element("char__lb_name",  getRaceNames(race_choice, dyn_screen.journey.inidata["gender"])) # sets name listbox
                        dyn_screen.journey.stages[1] = True
                    else:
                        dyn_screen.journey.stages[1] = False

                case "class":
                    if dyn_screen.journey.stage != 2:
                        dyn_screen.journey.stage = 2
                        dyn_screen.put_pgui("char__lb_class")
                        dyn_screen.put_pgui("char__tb_class")

                    class_choice = dyn_screen.get_pgui_choice("char__lb_class")
                    if class_choice is not None:
                        if dyn_screen.journey.inidata["class"] != class_choice: # this check allows for updating once per change (improves performance & get rid of render bug)
                            dyn_screen.journey.setInit("class", class_choice)
                            dyn_screen.set_pgui_element("char__tb_class", getClass(class_choice).descr()) # sets infobox
                        dyn_screen.journey.stages[2] = True
                    else:
                        dyn_screen.journey.stages[2] = False

                case "name_avatar":
                    if dyn_screen.journey.stage != 3:
                        dyn_screen.journey.stage = 3
                        dyn_screen.put_pgui("char__ti_name")
                        dyn_screen.put_pgui("char__lb_name")

                    saves = listSaves()

                    name_choice = dyn_screen.get_pgui_choice("char__ti_name")
                    name_pick   = dyn_screen.get_pgui_choice("char__lb_name")
                    if name_pick is not None:
                        dyn_screen.set_pgui_element("char__ti_name", name_pick)
                        dyn_screen.reset_pgui()
                    if name_choice != "" and name_choice not in saves:
                        dyn_screen.journey.setInit("name", name_choice)
                        dyn_screen.journey.stages[3] = True
                    else:
                        dyn_screen.journey.stages[3] = False
                        if name_choice in saves:
                            put_text(screen, langstring("ccrt__name_exists"), font_cat="menu", size=30, pos_x=50, pos_y=55, colour=fCol.OTHER.value)

                case "point_distribution":
                    if dyn_screen.journey.stage != 4:
                        dyn_screen.journey.stage = 4
                        dyn_screen.set_pgui_element("char__lb_attrs",  getAttributesTupleAdjusted(dyn_screen.journey.inidata["class"], dyn_screen.journey.inidata["race"]))
                        dyn_screen.set_pgui_element("char__lb_skills", getSkillsTupleAdjusted    (dyn_screen.journey.inidata["class"], dyn_screen.journey.inidata["race"], manual_excl=True))
                        dyn_screen.put_pgui("char__lb_attrs")
                        dyn_screen.put_pgui("char__lb_skills")
                        dyn_screen.put_pgui("char__tb_attrs")
                        dyn_screen.put_pgui("char__tb_skills")

                    attr_choice  = dyn_screen.get_pgui_choice("char__lb_attrs")
                    skill_choice = dyn_screen.get_pgui_choice("char__lb_skills")
                    if attr_choice is not None:
                        if dyn_screen.journey.inidata["attr"] != attr_choice:
                            dyn_screen.journey.setInit("attr", attr_choice)
                            dyn_screen.set_pgui_element("char__tb_attrs", getAttribute(attr_choice).descr()) # sets infobox
                    if skill_choice is not None:
                        if dyn_screen.journey.inidata["skill"] != skill_choice:
                            dyn_screen.journey.setInit("skill", skill_choice)
                            dyn_screen.set_pgui_element("char__tb_skills", getSkill(skill_choice).descr()) # sets infobox
                        if attr_choice is not None: # 'are both selected?' (put here to minimise performance cost)
                            dyn_screen.journey.stages[4] = True
                    if (skill_choice is None) or (attr_choice is None):
                        dyn_screen.journey.stages[4] = False

                case "religion":
                    if dyn_screen.journey.stage != 5:
                        dyn_screen.journey.stage = 5
                        dyn_screen.put_pgui("char__lb_rel")
                        dyn_screen.put_pgui("char__tb_rel")

                    rl_choice = dyn_screen.get_pgui_choice("char__lb_rel")
                    if rl_choice is not None:
                        if dyn_screen.journey.inidata["religion"] != rl_choice: # this check allows for updating once per change (improves performance & get rid of render bug)
                            dyn_screen.journey.setInit("religion", rl_choice)
                            dyn_screen.set_pgui_element("char__tb_rel", getReligion(rl_choice).descr(gender=dyn_screen.journey.inidata["gender"])) # sets infobox
                        dyn_screen.journey.stages[5] = True
                    else:
                        dyn_screen.journey.stages[5] = False

                case "origin":
                    if dyn_screen.journey.stage != 6:
                        dyn_screen.journey.stage = 6
                        dyn_screen.put_pgui("char__lb_orig")
                        dyn_screen.put_pgui("char__tb_orig")
                        dyn_screen.put_pgui("char__ti_hist")

                    put_text(screen, text=langstring("ccrt__history"), font_cat="menu", size=30, pos_x=61, pos_y=30, colour=fCol.ENABLED.value)

                    orig_choice = dyn_screen.get_pgui_choice("char__lb_orig")
                    history_txt = dyn_screen.get_pgui_choice("char__ti_hist")
                    if history_txt is not None:
                        if dyn_screen.journey.inidata["history"] != history_txt: # sets history textbox
                            dyn_screen.journey.setInit("history", history_txt)
                    if orig_choice is not None:
                        if dyn_screen.journey.inidata["origin"] != orig_choice: # this check allows for updating once per change (improves performance & get rid of render bug)
                            dyn_screen.journey.setInit("origin", orig_choice)
                            dyn_screen.set_pgui_element("char__tb_orig", getOrigin(orig_choice).descr(gender=dyn_screen.journey.inidata["gender"])) # sets infobox
                        dyn_screen.journey.stages[6] = True
                    else:
                        dyn_screen.journey.stages[6] = False

                case "gameplay_settings":
                    if dyn_screen.journey.stage != 7:
                        dyn_screen.journey.stage     = 7
                        dyn_screen.journey.stages[7] = True
                        dyn_screen.put_pgui("char__tb_pdth")

                    match dyn_screen.journey.settings["permadeath"]:
                        case True: pdeath_col = fCol.ENABLED.value
                        case _:    pdeath_col = fCol.DISABLED.value
                    pdeath = put_text(screen, text=langstring("ccrt__sett_hardcore"), font_cat="menu", size=30, pos_x=30, pos_y=10, colour=pdeath_col)
                    if mouseColliderPx(pdeath[0], pdeath[1], pdeath[2], pdeath[3]):
                        if mouseRec(pg_events):
                            dyn_screen.journey.settings["permadeath"] = not dyn_screen.journey.settings["permadeath"]

                case "summary":
                    if dyn_screen.journey.stage != 8:
                        dyn_screen.journey.stage = 8
                        dyn_screen.put_pgui("char__temp_warn")

                    put_text(screen, text=langstring("ccrt__end_name"),                                  font_cat="menu", size=30, pos_x=40, pos_y=10, colour=fCol.ENABLED.value)
                    put_text(screen, text=dyn_screen.journey.inidata["name"],                            font_cat="menu", size=30, pos_x=50, pos_y=10, colour=fCol.DISABLED.value)
                    put_text(screen, text=langstring("ccrt__end_race"),                                  font_cat="menu", size=30, pos_x=40, pos_y=18, colour=fCol.ENABLED.value)
                    put_text(screen, text=getRace(dyn_screen.journey.inidata["race"]).langstr(),         font_cat="menu", size=30, pos_x=50, pos_y=18, colour=fCol.DISABLED.value)
                    put_text(screen, text=langstring("ccrt__end_class"),                                 font_cat="menu", size=30, pos_x=40, pos_y=26, colour=fCol.ENABLED.value)
                    put_text(screen, text=getClass(dyn_screen.journey.inidata["class"]).langstr(),       font_cat="menu", size=30, pos_x=50, pos_y=26, colour=fCol.DISABLED.value)
                    put_text(screen, text=langstring("ccrt__end_religion"),                              font_cat="menu", size=30, pos_x=40, pos_y=34, colour=fCol.ENABLED.value)
                    put_text(screen, text=getReligion(dyn_screen.journey.inidata["religion"]).langstr(), font_cat="menu", size=30, pos_x=50, pos_y=34, colour=fCol.DISABLED.value)
                    put_text(screen, text=langstring("ccrt__end_origin"),                                font_cat="menu", size=30, pos_x=40, pos_y=42, colour=fCol.ENABLED.value)
                    put_text(screen, text=getOrigin(dyn_screen.journey.inidata["origin"]).langstr(),     font_cat="menu", size=30, pos_x=50, pos_y=42, colour=fCol.DISABLED.value)
                    # save button
                    sv_bt = put_text(screen, text=langstring("ccrt__end_save"), font_cat="menu", size=30, pos_x=58, pos_y=65, colour=fCol.ENABLED.value)

                    # set variable later on and make new render when hovered && ifs for getting around
                    if mouseColliderPx(sv_bt[0], sv_bt[1], sv_bt[2], sv_bt[3]):
                        put_text(screen, text=langstring("ccrt__end_save"), font_cat="menu", size=30, pos_x=58, pos_y=65, colour=fCol.HOVERED.value)
                        if mouseRec(pg_events):
                            dyn_screen.journey.init()
                            dyn_screen.journey.reset()
                            guitype[0] = switch_gscr(dyn_screen, screen, "menu")
                            guitype[1] = None
                            dyn_screen.reset_pgui(True)

            # ==================================================
            # hovering & clicking events
            if mouseColliderPx(gtx[0], gtx[1], gtx[2], gtx[3]):
                put_text(screen, text=langstring("menu__sett_back"), font_cat="menu", size=30, align_x="center", pos_y=92, colour="#7C613B")
                if mouseRec(pg_events):
                    guitype[0] = switch_gscr(dyn_screen, screen, "menu")
                    guitype[1] = None
                    dyn_screen.reset_pgui(True)
                    dyn_screen.journey.reset()
                    dyn_screen.journey.stage = None

            elif mouseColliderPx(mn1[0], mn1[1], mn1[2], mn1[3]) and guitype[1] == "race":
                put_text(screen, text=langstring("ccrt__gen_category1"), font_cat="menu", size=30, align_x="left", pos_x=5, pos_y=10, colour=fCol.HOVERED.value)
                if mouseRec(pg_events):
                    dyn_screen.journey.stages[1] = False
                    guitype[1] = switch_gscr(dyn_screen, screen, "gender")
                    dyn_screen.reset_pgui()

            elif mouseColliderPx(mn2[0], mn2[1], mn2[2], mn2[3]):
                # go next
                if guitype[1] == "gender" and dyn_screen.journey.stages[0] is True:
                    put_text(screen, text=langstring("ccrt__gen_category2"), font_cat="menu", size=30, align_x="left", pos_x=5, pos_y=18, colour=fCol.HOVERED.value)
                    if mouseRec(pg_events):
                        guitype[1] = switch_gscr(dyn_screen, screen, "race")
                        dyn_screen.reset_pgui()
                # go back
                if guitype[1] == "class":
                    put_text(screen, text=langstring("ccrt__gen_category2"), font_cat="menu", size=30, align_x="left", pos_x=5, pos_y=18, colour=fCol.HOVERED.value)
                    if mouseRec(pg_events):
                        dyn_screen.journey.stages[2] = False
                        guitype[1] = switch_gscr(dyn_screen, screen, "race")
                        dyn_screen.reset_pgui()

            elif mouseColliderPx(mn3[0], mn3[1], mn3[2], mn3[3]):
                # go next
                if guitype[1] == "race" and dyn_screen.journey.stages[1] is True:
                    put_text(screen, text=langstring("ccrt__gen_category3"), font_cat="menu", size=30, align_x="left", pos_x=5, pos_y=26, colour=fCol.HOVERED.value)
                    if mouseRec(pg_events):
                        guitype[1] = switch_gscr(dyn_screen, screen, "class")
                        dyn_screen.reset_pgui()
                # go back
                if guitype[1] == "name_avatar":
                    put_text(screen, text=langstring("ccrt__gen_category3"), font_cat="menu", size=30, align_x="left", pos_x=5, pos_y=26, colour=fCol.HOVERED.value)
                    if mouseRec(pg_events):
                        dyn_screen.journey.stages[3] = False
                        guitype[1] = switch_gscr(dyn_screen, screen, "class")
                        dyn_screen.reset_pgui()

            elif mouseColliderPx(mn4[0], mn4[1], mn4[2], mn4[3]):
                # go next
                if guitype[1] == "class" and dyn_screen.journey.stages[2] is True:
                    put_text(screen, text=langstring("ccrt__gen_category4"), font_cat="menu", size=30, align_x="left", pos_x=5, pos_y=34, colour=fCol.HOVERED.value)
                    if mouseRec(pg_events):
                        guitype[1] = switch_gscr(dyn_screen, screen, "name_avatar")
                        dyn_screen.reset_pgui()
                # go back
                if guitype[1] == "point_distribution":
                    put_text(screen, text=langstring("ccrt__gen_category4"), font_cat="menu", size=30, align_x="left", pos_x=5, pos_y=34, colour=fCol.HOVERED.value)
                    if mouseRec(pg_events):
                        dyn_screen.journey.stages[4] = False
                        guitype[1] = switch_gscr(dyn_screen, screen, "name_avatar")
                        dyn_screen.reset_pgui()

            elif mouseColliderPx(mn5[0], mn5[1], mn5[2], mn5[3]):
                # go next
                if guitype[1] == "name_avatar" and dyn_screen.journey.stages[3] is True:
                    put_text(screen, text=langstring("ccrt__gen_category5"), font_cat="menu", size=30, align_x="left", pos_x=5, pos_y=42, colour=fCol.HOVERED.value)
                    if mouseRec(pg_events):
                        guitype[1] = switch_gscr(dyn_screen, screen, "point_distribution")
                        dyn_screen.reset_pgui()
                # go back
                if guitype[1] == "religion":
                    put_text(screen, text=langstring("ccrt__gen_category5"), font_cat="menu", size=30, align_x="left", pos_x=5, pos_y=42, colour=fCol.HOVERED.value)
                    if mouseRec(pg_events):
                        dyn_screen.journey.stages[5] = False
                        guitype[1] = switch_gscr(dyn_screen, screen, "point_distribution")
                        dyn_screen.reset_pgui()

            elif mouseColliderPx(mn6[0], mn6[1], mn6[2], mn6[3]):
                # go next
                if guitype[1] == "point_distribution" and dyn_screen.journey.stages[4] is True:
                    put_text(screen, text=langstring("ccrt__gen_category6"), font_cat="menu", size=30, align_x="left", pos_x=5, pos_y=50, colour=fCol.HOVERED.value)
                    if mouseRec(pg_events):
                        guitype[1] = switch_gscr(dyn_screen, screen, "religion")
                        dyn_screen.reset_pgui()
                # go back
                if guitype[1] == "origin":
                    put_text(screen, text=langstring("ccrt__gen_category6"), font_cat="menu", size=30, align_x="left", pos_x=5, pos_y=50, colour=fCol.HOVERED.value)
                    if mouseRec(pg_events):
                        dyn_screen.journey.stages[6] = False
                        guitype[1] = switch_gscr(dyn_screen, screen, "religion")
                        dyn_screen.reset_pgui()

            elif mouseColliderPx(mn7[0], mn7[1], mn7[2], mn7[3]):
                # go next
                if guitype[1] == "religion" and dyn_screen.journey.stages[5] is True:
                    put_text(screen, text=langstring("ccrt__gen_category7"), font_cat="menu", size=30, align_x="left", pos_x=5, pos_y=58, colour=fCol.HOVERED.value)
                    if mouseRec(pg_events):
                        guitype[1] = switch_gscr(dyn_screen, screen, "origin")
                        dyn_screen.reset_pgui()
                # go back
                if guitype[1] == "gameplay_settings":
                    put_text(screen, text=langstring("ccrt__gen_category7"), font_cat="menu", size=30, align_x="left", pos_x=5, pos_y=58, colour=fCol.HOVERED.value)
                    if mouseRec(pg_events):
                        dyn_screen.journey.stages[7] = False
                        guitype[1] = switch_gscr(dyn_screen, screen, "origin")
                        dyn_screen.reset_pgui()

            elif mouseColliderPx(mn8[0], mn8[1], mn8[2], mn8[3]):
                # go next
                if guitype[1] == "origin" and dyn_screen.journey.stages[6] is True:
                    put_text(screen, text=langstring("ccrt__gen_category8"), font_cat="menu", size=30, align_x="left", pos_x=5, pos_y=66, colour=fCol.HOVERED.value)
                    if mouseRec(pg_events):
                        guitype[1] = switch_gscr(dyn_screen, screen, "gameplay_settings")
                        dyn_screen.reset_pgui()
                # go back
                if guitype[1] == "summary":
                    put_text(screen, text=langstring("ccrt__gen_category8"), font_cat="menu", size=30, align_x="left", pos_x=5, pos_y=66, colour=fCol.HOVERED.value)
                    if mouseRec(pg_events):
                        dyn_screen.journey.stages[8] = False
                        guitype[1] = switch_gscr(dyn_screen, screen, "gameplay_settings")
                        dyn_screen.reset_pgui()

            elif mouseColliderPx(mn9[0], mn9[1], mn9[2], mn9[3]) and guitype[1] == "gameplay_settings" and dyn_screen.journey.stages[7] is True:
                put_text(screen, text=langstring("ccrt__gen_category9"), font_cat="menu", size=30, align_x="left", pos_x=5, pos_y=74, colour=fCol.HOVERED.value)
                if mouseRec(pg_events):
                    dyn_screen.journey.setInit("settings", dyn_screen.journey.settings) # saving current game settings in 'inidata'
                    guitype[1] = switch_gscr(dyn_screen, screen, "summary")
                    dyn_screen.reset_pgui()
