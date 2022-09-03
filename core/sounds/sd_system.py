from core.file_system.repo_manag import dir_checker
from system.mod_manag import mod_lister
from core.utils import *
import os, random

# Background menu image handler
def bg_music():
    worldpacks = mod_lister("worlds"); bgm = []
    for i in worldpacks:
        tpath = f"{gpath}/worlds/{i}/music/backgrounds/"
        if os.path.isdir(tpath):
            files = dir_checker(tpath, "file")
            for j in files:
                if j.endswith(".mp3"): bgm.append(f"worlds/{i}/music/backgrounds/{j}")
                if j.endswith(".ogg"): bgm.append(f"worlds/{i}/music/backgrounds/{j}")
                if j.endswith(".wav"): bgm.append(f"worlds/{i}/music/backgrounds/{j}")
    if any("%PR_" in v for v in bgm):
        return bgp_music(bgm)
    return random.choice(bgm)

# Prioritised background menu image handler
def bgp_music(bgm: list):
    bgmp = []
    for m in bgm:
        if "%PR_" in m:
            bgmp.append(m)
    return random.choice(bgmp)