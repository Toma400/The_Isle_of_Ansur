from core.file_system.repo_manag import deep_file_lister
from core.file_system.json_manag import *
from core.decorators import Deprecated
import os, sys, shutil, toml, re
import logging as log
import requests

#===========|==================================================
# CONSTANTS | Used regularly in other parts of the code
#===========|==================================================
# path to game's folder
gpath          = os.path.dirname(os.path.abspath("main.py"))
developer_mode = os.path.exists(".dev")
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
        case "lbmd": return sdata["listbox_mode"]
        case "lbam": return sdata["listbox_amount"]
        case "lbsz": return sdata["listbox_size"]
        case "vch":  return sdata["version_checker"]
        case "txts": return sdata["text_size"]
        case "tltp": return sdata["tooltip"]
        case other:  return sdata

def sysref(refn): # reads value from system reference file
    sdata = toml.load("core/system_ref.toml")
    return sdata[refn]

@Deprecated("hunger_thirst and permadeath are marked as deprecated now (see https://github.com/Toma400/The_Isle_of_Ansur/issues/16#issuecomment-1247081222)")
class DeprecatedSettings:
    optv = json_read("settings.json")["hunger_thirst"]
    pdth = json_read("settings.json")["permadeath"]

def temp_remover():
    if os.path.exists(f"{gpath}/_temp/"):
        shutil.rmtree(f"{gpath}/_temp/")
    if os.path.exists(f"{gpath}/__pycache__/"):
        shutil.rmtree(f"{gpath}/__pycache__/")

def script_loader():
    for x in deep_file_lister(f"scripts/", ext="py"):  # | imports all modules from /scripts/ folder
        x1 = x.replace("\\", "."); x2 = x1.replace("\\", "."); x2 = x2.replace("//", "."); x2 = x2.replace("//", ".")
        log.debug(f"Script is being imported: [{x2}]")
        __import__(x2)

def version_checker():
    """Checks game if its version is the latest, comparing it with GitHub repository"""

    def stcomp(status): # simplifies status type comparisons
        return ["pre alpha", "alpha", "pre beta", "beta", "release"].index(status)

    def sbv(ver): # tells if version is major (1, 2) or minor (1b, 1c)
        if any(not char.isdigit() for char in ver):
            chars = re.sub("[0-9]+", "", ver)
            nums  = re.sub("[^0-9]", "", ver)
            ver = f"{nums}.{ord(chars)-97}"
        return float(ver)

    gitfile = requests.get("https://raw.githubusercontent.com/Toma400/The_Isle_of_Ansur/Alpha/core/system_ref.toml?ref=Alpha")
    if gitfile.status_code == 200:
        gitfile = toml.loads(gitfile.text)
        if stcomp(gitfile["release_status"]) > stcomp(sysref("release_status")): return True
        elif sbv(gitfile["release_version"]) > sbv(sysref("release_version")):   return True
        else:                                                                    log.info(f"Running actual version: [{sysref('release_status')} {sysref('release_version')}]")
    else: log.info(f"Attempted to request version checking, but the status of request was {gitfile.status_code}.")
    return False

def update():
    """Currently redirects to the website"""
    import webbrowser; url = "https://github.com/Toma400/The_Isle_of_Ansur/releases"
    webbrowser.open(url, new=0, autoraise=True)

def refunc(*funcs): # does all functions in sequential order (non-return ones)
    for i in funcs:
        i