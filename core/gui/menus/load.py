from core.file_system.theme_manag import FontColour as fCol
from core.data.pack_manag.packs import getPacksSimplified
from core.data.player.religion import getReligion
from core.data.player.profession import getClass
from core.data.player.gender import getGender
from core.data.player.origin import getOrigin
from core.data.player.race import getRace
from core.graphics.gh_manag import mouseColliderPx, mouseRec, switch_gscr
from core.graphics.text_manag import put_text
from core.gui.manag.langstr import langstring
from core.file_system.parsers import loadTOML
from logging import log, ERROR

def loadDescr(save: str) -> str:
    ret = ""
    try:
        sf             = loadTOML(f"saves/{save}/buffer/presave.toml")
        packs_required = getPacksSimplified(sf['mods'], False)
        # string creation
        ret += f"{'{:<15}'.format(langstring('ccrt__gen_name'))}"     + f"{sf['name']}"                            + "\n"
        ret += f"{'{:<15}'.format(langstring('ccrt__gen_gender'))}"   + f"{getGender(sf['gender']).langstr()}"     + "\n"
        ret += f"{'{:<15}'.format(langstring('ccrt__gen_race'))}"     + f"{getRace(sf['race']).langstr()}"         + "\n"
        ret += f"{'{:<15}'.format(langstring('ccrt__gen_class'))}"    + f"{getClass(sf['class']).langstr()}"       + "\n"
        ret += f"{'{:<15}'.format(langstring('ccrt__gen_religion'))}" + f"{getReligion(sf['religion']).langstr()}" + "\n"
        ret += f"{'{:<15}'.format(langstring('ccrt__gen_origin'))}"   + f"{getOrigin(sf['origin']).langstr()}"     + "\n"
        ret += f"{langstring('ccrt__gen_history')}"                                          + "\n"
        ret += f"{sf['history']}"                                                            + "\n"
        ret += f"{langstring('ccrt__load_packs_used')}"                                      + "\n"
        # set fixed length that adjusts to the longest mod ID
        maxlen = 0
        for pack in packs_required.keys():
            if len(pack) > maxlen:
                maxlen = len(pack)
        maxlen = '{:<' + str(maxlen + 1) + '}'
        for pack in packs_required.keys():
            ret += f"  - {maxlen.format(pack)} |"
            for p in packs_required[pack]:
                if p != "scripts":
                    ret += f" {langstring(f'pack__type_{p}')} |"
            ret += "\n"
    except:
        log(ERROR, f"Couldn't load informations about save -{save}-. The save may be corrupted or made with older version. Printing stacktrace:", exc_info=True)
        ret = langstring("system__text_load_fail")
    return ret

def loadGame(screen, guitype, fg_events, pg_events, tev, dyn_screen):
    # background sprite
    dyn_screen.gui("menu__gh_background").full().put(screen)

    put_text(      screen, text=langstring("menu__button_load"), font_cat="menu", size=35, align_x="center", pos_y=1,  colour=fCol.DISABLED.value)
    gtx = put_text(screen, text=langstring("menu__sett_back"),   font_cat="menu", size=30, align_x="center", pos_y=92, colour=fCol.ENABLED.value)

    dyn_screen.put_pgui("load__saves")
    dyn_screen.put_pgui("load__descr")

    game_loaded = dyn_screen.get_pgui_choice("load__saves")
    if game_loaded is not None:
        if dyn_screen.journey.name != game_loaded:
            dyn_screen.journey.name = game_loaded
            dyn_screen.set_pgui_element("load__descr", loadDescr(game_loaded))

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
        put_text(screen, text=langstring("menu__sett_back"), font_cat="menu", size=30, align_x="center", pos_y=92, colour=fCol.HOVERED.value)
        if mouseRec(pg_events):
            guitype[0] = switch_gscr(dyn_screen, screen, "menu")
            guitype[1] = None