from core.file_system.theme_manag import FontColour as fCol
from core.gui.registry.pgui_objects import PGUI_Helper
from core.data.save_system.verify import SaveVerifier
from core.data.save_system.walk import listSaves
from core.data.pack_manag.info import searchInfo
from core.data.player.religion import getReligion
from core.data.player.profession import getClass
from core.data.player.gender import getGender
from core.data.player.origin import getOrigin
from core.data.player.race import getRace
from core.graphics.gh_manag import mouseColliderPx, mouseRec, switch_gscr, imgLoad
from core.graphics.text_manag import put_text
from core.gui.manag.langstr import langstring
from core.file_system.parsers import loadTOML
from logging import log, ERROR, WARNING
from os.path import exists

def loadDescr(save: str, vr: SaveVerifier) -> str:
    ret = ""
    if vr.save_structure:
        sf             = loadTOML(f"saves/{save}/buffer/data.toml")
        packs_required = loadTOML(f"saves/{save}/buffer/mods.toml")
        packs_final    = {}
        # string creation
        ret += f"{'{:<15}'.format(langstring('ccrt__gen_name'))}"     + f"{sf['name']}"                            + "\n"
        ret += f"{'{:<15}'.format(langstring('ccrt__gen_gender'))}"   + f"{getGender(sf['gender']).langstr()}"     + "\n"
        ret += f"{'{:<15}'.format(langstring('ccrt__gen_race'))}"     + f"{getRace(sf['race']).langstr()}"         + "\n"
        ret += f"{'{:<15}'.format(langstring('ccrt__gen_class'))}"    + f"{getClass(sf['class']).langstr()}"       + "\n"
        # ret += f"{'{:<15}'.format(langstring('ccrt__gen_religion'))}" + f"{getReligion(sf['religion']).langstr()}" + "\n" << TODO
        ret += f"{'{:<15}'.format(langstring('ccrt__gen_origin'))}"   + f"{getOrigin(sf['origin']).langstr()}"     + "\n"
        ret += f"{langstring('ccrt__gen_history')}"                                          + "\n"
        # ret += f"{sf['history']}"                                                            + "\n"                       << TODO
        ret += f"{langstring('load__packs_used')}"                                           + "\n"
        # set fixed length that adjusts to the longest mod ID + set translation names
        maxlen = 0
        for pack, ver in packs_required.items():
            p_info = searchInfo(pack)
            p_name = pack
            if p_info is not None:
                if "name" in p_info:
                    p_name = p_info["name"]
            if len(p_name) > maxlen:
                maxlen = len(p_name)
            packs_final[p_name] = ver

        maxlen = '{:<' + str(maxlen + 1) + '}'
        for pack, ver in packs_final.items():
            ret += f"  - {maxlen.format(pack)} | " # name
            ret += f"{ver}"                        # version
            if pack in vr.mods_versions[3]:        # error: required version
                ret += f" * {langstring('system__text_mis')}"
            elif pack in vr.mods_versions[4]:
                ret += f" * {langstring('system__text_dif')}: {vr.mods_versions[3][pack]}"
            ret += "\n"

        if not vr.mods_versions[0]:
            log(WARNING, f'''
            Save -{save}- did not met its mods requirements.
            
            Required mods:
            {vr.mods_versions[1]}
            
            Loaded mods:
            {vr.mods_versions[2]}
            
            Missing:
            {vr.mods_versions[3]}
            
            Different versions:
            {vr.mods_versions[4]}
            ''')
    else:
        log(ERROR, f"Couldn't load informations about save -{save}-. The save may be corrupted or made with older version. Printing stacktrace:", exc_info=True)
        ret = langstring("load__error_longer")
    return ret

def removeSave(save: str):
    import shutil; shutil.rmtree(f"saves/{save}", ignore_errors=True)

def loadGame(screen, guitype, fg_events, pg_events, tev, dyn_screen):
    # background sprite
    is_active = {"false": fCol.DISABLED.value, "true": fCol.ENABLED.value}
    dyn_screen.gui("menu__gh_background").full().put(screen)

    put_text(screen,       text=langstring("menu__button_load"), font_cat="menu", size=35, align_x="center",          pos_y=1,  colour=fCol.ENABLED.value)
    lsv = put_text(screen, text=langstring("load__load"),        font_cat="menu", size=30, align_x="right",  pos_x=9, pos_y=10, colour=fCol.DISABLED.value)
    put_text(screen,       text=langstring("load__restore"),     font_cat="menu", size=30, align_x="right",  pos_x=9, pos_y=16, colour=fCol.DISABLED.value)
    rsv = put_text(screen, text=langstring("load__remove"),      font_cat="menu", size=30, align_x="right",  pos_x=9, pos_y=22, colour=fCol.DISABLED.value)
    gtx = put_text(screen, text=langstring("menu__back"),        font_cat="menu", size=30, align_x="center",          pos_y=92, colour=fCol.ENABLED.value)

    dyn_screen.put_pgui("load__saves")
    dyn_screen.put_pgui("load__descr")
    dyn_screen.put_pgui("load__avatar")

    game_loaded = dyn_screen.get_pgui_choice("load__saves")
    if game_loaded is not None:
        if dyn_screen.journey.name != game_loaded:
            dyn_screen.journey.name   = game_loaded
            dyn_screen.journey.verify = SaveVerifier(game_loaded)
            dyn_screen.set_pgui_element("load__descr", loadDescr(game_loaded, dyn_screen.journey.verify))
            if dyn_screen.journey.verify.correct: # see comment for this var
                dyn_screen.tooltip = ""
            else:
                dyn_screen.tooltip = "menu__tp_load_load"
            if exists(f"saves/{game_loaded}/buffer/avatar.png"):
                dyn_screen.set_pgui_element("load__avatar", imgLoad(f"saves/{game_loaded}/buffer/avatar.png", alpha=True))
            else:
                dyn_screen.set_pgui_element("load__avatar", imgLoad(PGUI_Helper.def_img, alpha=True))
        put_text(screen, text=langstring("load__remove"), font_cat="menu", size=30, align_x="right", pos_x=9, pos_y=22, colour=fCol.ENABLED.value)
        if dyn_screen.journey.verify.correct is True: # see comment for this var
            put_text(screen, text=langstring("load__load"), font_cat="menu", size=30, align_x="right", pos_x=9, pos_y=10, colour=fCol.ENABLED.value)

    # GUI EXPECTED
    # - Image                            | I guess location image? Currently placeholder maybe
    # - Basic data                       | Name, race, class, location, etc.
    # - List of mods                     | It explains itself
    #
    # BUTTONS EXPECTED
    # - Load game                        | Checks integrity and loads if correct
    # - Overwrite from cache             | Writes from cached save
    # - Delete game                      | Deletes the folder

    #===============================================================
    # EVENTS
    #===============================================================
    if mouseColliderPx(gtx[0], gtx[1], gtx[2], gtx[3]):
        put_text(screen, text=langstring("menu__back"), font_cat="menu", size=30, align_x="center", pos_y=92, colour=fCol.HOVERED.value)
        if mouseRec(pg_events):
            guitype[0] = switch_gscr(dyn_screen, screen, "menu")
            guitype[1] = None

    elif mouseColliderPx(lsv[0], lsv[1], lsv[2], lsv[3]):
        if game_loaded is not None:
            if dyn_screen.journey.verify.correct: # see comment for this var
                put_text(screen, text=langstring("load__load"), font_cat="menu", size=30, align_x="right", pos_x=9, pos_y=10, colour=fCol.HOVERED.value)
                if mouseRec(pg_events):
                    dyn_screen.journey.name     = game_loaded
                    dyn_screen.journey.location = dyn_screen.journey.readLocation(game_loaded)
                    guitype[0] = switch_gscr(dyn_screen, screen, "location")
            else:
                dyn_screen.tooltip = "menu__tp_load_load"

    elif mouseColliderPx(rsv[0], rsv[1], rsv[2], rsv[3]) and game_loaded is not None:
        put_text(screen, text=langstring("load__remove"), font_cat="menu", size=30, align_x="right", pos_x=9, pos_y=22, colour=fCol.HOVERED.value)
        if mouseRec(pg_events):
            removeSave(game_loaded)
            dyn_screen.set_pgui_element("load__saves", listSaves())
            dyn_screen.set_pgui_element("load__descr", "")

    else:
        dyn_screen.tooltip = ""