from system.ref_systems.system_ref import *
from core.file_system.repo_manag import deep_file_lister
from core.file_system.json_manag import *
import logging as log
import os, importlib

#===========|==================================================
# CONSTANTS | Used regularly in other parts of the code
#===========|==================================================
# path to game's folder
gpath = os.path.dirname(os.path.abspath("main.py"))
# settings
def scx(setn=None): # used for checking current settings status
    sdata = json_read("settings.json")
    match setn:
        case "lang": return sdata["language"]
        case "svx":  return sdata["res_x"]
        case "svy":  return sdata["res_y"]
        case "sndv": return sdata["sound"]
        case "lglm": return sdata["log_limit"]
        case "legu": return sdata["legacy_unpacking"]
        case other:  return sdata

# hunger_thirst and permadeath are marked as deprecated now (see https://github.com/Toma400/The_Isle_of_Ansur/issues/16#issuecomment-1247081222)
optv = json_read("settings.json")["hunger_thirst"]
pdth = json_read("settings.json")["permadeath"]

def temp_remover():
    import shutil, os
    if os.path.exists(f"{gpath}/_temp/"):
        shutil.rmtree(f"{gpath}/_temp/")

def script_loader():
    for x in deep_file_lister(f"scripts/", ext="py"):  # | imports all modules from /scripts/ folder
        x1 = x.replace("\\", "."); x2 = x1.replace("\\", "."); x2 = x2.replace("//", "."); x2 = x2.replace("//", ".")
        log.debug(f"Script is being imported: [{x2}]")
        __import__(x2)