from core.file_system.repo_manag import dir_checker
from utils.text_manag import text_splitter as tspl
from system.mod_manag import mod_lister
from core.utils import *
import os, random

# Background menu image handler
def bg_screen():
    worldpacks = mod_lister("worlds"); bgs = []
    for i in worldpacks:
        tpath = f"{gpath}/worlds/{i}/assets/backgrounds/"
        if os.path.isdir(tpath):
            files = dir_checker(tpath, "file")
            for j in files:
                if j.endswith(".jpg"): bgs.append(f"worlds/{i}/assets/backgrounds/{j}")
                if j.endswith(".png"): bgs.append(f"worlds/{i}/assets/backgrounds/{j}")
    if any("%PR_" in v for v in bgs):
        return tspl(bgp_screen(bgs), "/assets/backgrounds/", 0)
    return tspl(random.choice(bgs), "/assets/backgrounds/", 0)

# Prioritised background menu image handler
def bgp_screen(bgs: list):
    bgsp = []
    for m in bgs:
        if "%PR_" in m:
            bgsp.append(m)
    return random.choice(bgsp)
