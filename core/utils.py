from system.json_manag import json_read
import os

#===========|==================================================
# CONSTANTS | Used regularly in other parts of the code
#===========|==================================================
# path to game's folder
gpath = os.path.dirname(os.path.abspath("main.py"))
# settings
settings_data = json_read("system_settings.json") #dict
lang = settings_data["language"]
svx  = settings_data["res_x"]
svy  = settings_data["res_y"]
sndv = settings_data["sound"]

def temp_remover():
    import shutil, os
    if os.path.exists(f"{gpath}/_temp/"):
        shutil.rmtree(f"{gpath}/_temp/")