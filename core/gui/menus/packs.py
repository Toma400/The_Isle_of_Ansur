from core.graphics.gh_manag import mouseColliderPx, mouseRec, switch_gscr
from core.data.pack_manag.info import searchInfo
from core.data.pack_manag.id import zipToID
from core.graphics.text_manag import put_text
from core.gui.manag.langstr import langstring
from core.file_system.parsers import loadYAML
import os

def packOrder() -> list[(str, str)]:
    return [(pack.replace(".zip", "").replace("_", " ").upper(), pack) for pack in loadYAML("core/data/pack_manag/pack_order.yaml")]

def packDescr(pack_id: str) -> str:
    inf = searchInfo(pack_id)
    ret = ""
    if inf is not None:
        if "name" in inf:
            ret += f"{'{:<15}'.format(langstring('pack__name'))}"    + f"{inf['name']}"    + "\n"
        if "credits" in inf:
            ret += f"{'{:<15}'.format(langstring('pack__authors'))}" + f"{inf['credits']}" + "\n"
        if "version" in inf:
            ret += f"{'{:<15}'.format(langstring('pack__version'))}" + f"{inf['version']}" + "\n"
        if "description" in inf:
            ret += langstring('pack__descr')                                               + "\n"
            ret += inf["description"]                                                      + "\n"
        ret += langstring("pack__req")                                                     + "\n"
        if "requirements" in inf:
            maxlen = 0
            for mod_id in inf["requirements"].keys():
                if len(mod_id) > maxlen:
                    maxlen = len(mod_id)
            maxlen = '{:<' + str(maxlen + 1) + '}'
            for mod_id, mod_v in inf["requirements"].items():
                ret += f"{maxlen.format(f'- {mod_id}:')}" + f" {mod_v}"
    return ret

def packMenu(screen, guitype, fg_events, pg_events, tev, dyn_screen):
    dyn_screen.gui("menu__gh_background").full().put(screen)

    gtx = put_text(screen, text=langstring("menu__sett_back"),    font_cat="menu", size=30, pos_x=5, pos_y=92, colour="#4E3510")
    # pdb = put_text(screen, text=langstring("pack__disable"),      font_cat="menu", size=30, pos_x=5, pos_y=92, colour="#4E3510")
    # pmu = put_text(screen, text=langstring("pack__move_up"),      font_cat="menu", size=30, pos_x=5, pos_y=92, colour="#4E3510")
    # pmd = put_text(screen, text=langstring("pack__move_down"),    font_cat="menu", size=30, pos_x=5, pos_y=92, colour="#4E3510")

    dyn_screen.put_pgui("pack__zip_list")
    dyn_screen.put_pgui("pack__descr")
    if not dyn_screen.get_pgui_options("pack__zip_list"):
        if os.path.exists("core/data/pack_manag/pack_order.yaml"):
            dyn_screen.set_pgui_element("pack__zip_list", packOrder())

    pack_selected = dyn_screen.get_pgui_choice("pack__zip_list")
    if pack_selected is not None:
        dyn_screen.set_pgui_element("pack__descr", packDescr(zipToID(pack_selected)))

    #if [listbox] contents are []:
      # if [file storing packs] size is not 0:
        # listbox.contents = getPacks
    # (this way, we can once-load it here, and then to reload just change listbox to [], so it reloads next tick)
    # potential issue?
    #  -> pack_order should be able to be None if no packs are available (so second if is met)
    #     -> but None pack_order breaks things, as you know from yesterday, so please make it so pack registry clears the file, but won't break after that
    #        (possible workaround: if no mods exist, pack_order can be removed) and then second if above would only check for existence of it)

    #===============================================================
    # EVENTS
    #===============================================================
    if mouseColliderPx(gtx[0], gtx[1], gtx[2], gtx[3]):
        put_text(screen, text=langstring("menu__sett_back"), font_cat="menu", size=30, pos_x=5, pos_y=92, colour="#7C613B")
        if mouseRec(pg_events):
            guitype[0] = switch_gscr(dyn_screen, screen, "menu")
            guitype[1] = None