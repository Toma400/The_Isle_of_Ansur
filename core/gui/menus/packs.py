from core.graphics.gh_manag import mouseColliderPx, mouseRec, switch_gscr
from core.file_system.theme_manag import FontColour as fCol
from core.data.pack_manag.info import searchInfo
from core.data.pack_manag.id import zipToID
from core.graphics.text_manag import put_text
from core.gui.manag.langstr import langstring
from core.file_system.parsers import loadYAML
import os

def packOrder() -> list[(str, str)]:
    ret = []
    for pack in loadYAML("core/data/pack_manag/pack_order.yaml"):
        inf = searchInfo(zipToID(pack))
        if inf is not None:
            if "name" in inf:
                ret.append((inf["name"], pack))
                continue
        ret.append((pack.replace(".zip", "").replace("_", " ").title(), pack))
    return ret

def packDisabled() -> list[str]:
    if os.path.getsize("core/data/pack_manag/pack_disabled.yaml") > 0:
        return loadYAML("core/data/pack_manag/pack_disabled.yaml")
    return []

def packDescr(pack_id: str) -> str:
    inf = searchInfo(pack_id)
    ret = ""
    if inf is not None:
        if "name" in inf:
            ret += "<b>" + f"{'{:<15}'.format(langstring('pack__name'))}"    + f"</b>{inf['name']}"    + "\n"
        if "credits" in inf:
            ret += "<b>" + f"{'{:<15}'.format(langstring('pack__authors'))}" + f"</b>{inf['credits']}" + "\n"
        if "version" in inf:
            ret += "<b>" + f"{'{:<15}'.format(langstring('pack__version'))}" + f"</b>{inf['version']}" + "\n"
        if "description" in inf:
            ret += "<b>" + langstring('pack__descr') + "</b>"                                          + "\n"
            ret += inf["description"]                                                                  + "\n"
        ret += "<b>" + langstring("pack__req") + "</b>"                                                + "\n"
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

    put_text(screen,       text=langstring("menu__button_packs_manag"), font_cat="menu", size=35, align_x="center",           pos_y=1,  colour=fCol.ENABLED.value)
    gtx = put_text(screen, text=langstring("menu__sett_back"),          font_cat="menu", size=30,                   pos_x=5,  pos_y=92, colour=fCol.ENABLED.value)
    pdb = put_text(screen, text=langstring("pack__switch"),             font_cat="menu", size=30, align_x="right",  pos_x=10, pos_y=25, colour=fCol.DISABLED.value) # 'disable'
    # pmu = put_text(screen, text=langstring("pack__move_up"),      font_cat="menu", size=30, pos_x=5, pos_y=92, colour="#4E3510")
    # pmd = put_text(screen, text=langstring("pack__move_down"),    font_cat="menu", size=30, pos_x=5, pos_y=92, colour="#4E3510")
    # pmd = put_text(screen, text=langstring("pack__remove"),       font_cat="menu", size=30, pos_x=5, pos_y=92, colour="#4E3510")

    dyn_screen.put_pgui("pack__zip_list")
    dyn_screen.put_pgui("pack__descr")

    if not dyn_screen.get_pgui_options("pack__zip_list"): # initial set (to update, simply set pack__zip_list to [] again)
        if os.path.exists("core/data/pack_manag/pack_order.yaml"):
            dyn_screen.set_pgui_element("pack__zip_list", packOrder())

    pack_selected      = dyn_screen.get_pgui_choice("pack__zip_list")
    pack_disabled_list = packDisabled()

    if pack_selected is not None:
        dyn_screen.set_pgui_element("pack__descr", packDescr(zipToID(pack_selected)))
        put_text(screen, text=langstring("pack__switch"), font_cat="menu", size=30, align_x="right", pos_x=10, pos_y=25, colour=fCol.ENABLED.value)
        if pack_selected in pack_disabled_list:
            put_text(screen, text=langstring("pack__disabled"), font_cat="menu", size=30, align_x="right", pos_x=10, pos_y=35, colour=fCol.WARNING.value)

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
        put_text(screen, text=langstring("menu__sett_back"), font_cat="menu", size=30, pos_x=5, pos_y=92, colour=fCol.HOVERED.value)
        if mouseRec(pg_events):
            guitype[0] = switch_gscr(dyn_screen, screen, "menu")
            guitype[1] = None

    elif pack_selected is not None:
        # disabling/enabling pack
        if mouseColliderPx(pdb[0], pdb[1], pdb[2], pdb[3]):
            put_text(screen, text=langstring("pack__switch"), font_cat="menu", size=30, align_x="right", pos_x=10, pos_y=25, colour=fCol.HOVERED.value)
            if mouseRec(pg_events):
                if pack_selected not in pack_disabled_list:
                    with open("core/data/pack_manag/pack_disabled.yaml", "a") as yf:
                        yf.write(f"- {pack_selected}\n")
                else:
                    with open("core/data/pack_manag/pack_disabled.yaml", "r") as yf:
                        with open("core/data/pack_manag/pack_disabled.yaml", "w") as yf_out:
                            for line in yf:
                                if line.strip("\n") != f"- {pack_selected}":
                                    yf_out.write(line)