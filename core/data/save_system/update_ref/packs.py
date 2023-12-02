from core.data.pack_manag.versions import unifiedVersion, unifiedString, getVersion
from core.data.pack_manag.packs import getPacksSimplified
from core.data.pack_manag.info import searchInfo
from core.data.save_system.req_data import SV_KIND
from core.file_system.parsers import loadTOML
from os.path import exists
from enum import Enum
import logging as log
import toml

class ERR(Enum):
    NOT_FOUND = 0
    WRONG_VER = 1

def updateMods(name: str, data: dict = None):
    errs     = {}   # errors
    mod_list = {}   # dict of {'mod': 'ver'}
    packs    = getPacksSimplified()

    if exists(f"saves/{name}/{SV_KIND.BUFFER.value}/mods.toml"):
        mod_list = loadTOML(f"saves/{name}/{SV_KIND.BUFFER.value}/mods.toml")

    # checking removal of existing ones (verification)
    for mod_id, mod_ver in mod_list:
        print("""I'm in core.data.pack_manag.packs - I'm here to remind you to test this iteration I'm in. Once you test it on loading of game, thus seeing whether this works
                 correctly, my work will be done and you can remove me. Before that, don't you dare touching me! I do my duty fearlessly and will do unless you code all that
                 stupid functions. Good luck!""")
        if mod_id in packs:
            saved_ver = unifiedVersion(mod_ver)
            curr_ver  = getVersion(mod_id)
            if curr_ver is not None:
                if (saved_ver[0] > curr_ver[0]) or (saved_ver[1] > curr_ver[1]):
                    log.error(f"During mod checking for save -{name}- mod ID -{mod_id}- retained wrong version. Requested version: >={saved_ver}. Current version: {curr_ver}")
                    errs[mod_id] = ERR.WRONG_VER.value
                else:
                    mod_list[mod_id] = unifiedString(curr_ver) # overwrite in case newer version is made (also unifies it later)

        else:
            log.error(f"During mod checking for save -{name}- mod ID -{mod_id}- couldn't be found.")
            errs[mod_id] = ERR.NOT_FOUND.value

    # checking loaded ones (addition of new mods)
    for mod_id in packs.keys():
        if mod_id not in mod_list.keys():
            info = searchInfo(mod_id)
            if info is not None:
                if "version" in info:
                    mod_list[mod_id] = info["version"]
                else:
                    mod_list[mod_id] = "0.0.0"
            else:
                mod_list[mod_id] = "0.0.0"

    with open(f"saves/{name}/{SV_KIND.BUFFER.value}/mods.toml", "w") as f:
        toml.dump(mod_list, f)
        f.flush()

    return len(errs) > 0