from core.file_system.repo_manag import deep_file_lister
from system.json_manag import json_read
import os, logging

#===========|==================================================
# CONSTANTS | Used regularly in other parts of the code
#===========|==================================================
# path to game's folder
gpath = os.path.dirname(os.path.abspath("main.py"))
# settings
settings_data = json_read("settings.json") #dict
lang = settings_data["language"]
svx  = settings_data["res_x"]
svy  = settings_data["res_y"]
sndv = settings_data["sound"]

optv = settings_data["hunger_thirst"]
pdth = settings_data["permadeath"]
legu = settings_data["legacy_unpacking"]

def temp_remover():
    import shutil, os
    if os.path.exists(f"{gpath}/_temp/"):
        shutil.rmtree(f"{gpath}/_temp/")

def script_loader():
    for x in deep_file_lister(f"scripts/", ext="py"):  # | imports all modules from /scripts/ folder
        x1 = x.replace("\\", "."); x2 = x1.replace("\\", "."); x2 = x2.replace("//", "."); x2 = x2.replace("//", ".")
        logging.debug(f"Script is being imported: [{x2}]")
        __import__(x2)