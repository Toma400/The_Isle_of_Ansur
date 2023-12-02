from core.data.save_system.req_data import SV_KIND
from core.data.pack_manag.packs import getPacksSimplified
from core.data.pack_manag.info import searchInfo
from core.file_system.parsers import loadTOML
from os.path import exists
import toml

def updateMods(name: str, data: dict = None):
    mod_list = {}   # dict of {'mod': 'ver'}
    packs    = getPacksSimplified()

    if exists(f"saves/{name}/{SV_KIND.BUFFER.value}/mods.toml"):
        mod_list = loadTOML(f"saves/{name}/{SV_KIND.BUFFER.value}/mods.toml")

    # checking removal of existing ones (verification)
    for mod_id, mod_ver in mod_list:
        pass

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