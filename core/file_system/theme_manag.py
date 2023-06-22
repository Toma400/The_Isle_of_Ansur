from core.file_system.repo_manag import gpath
from core.utils import scx
import glob
import toml
#==================================================
# GENERAL
#==================================================
# 1. guide.toml for themes
# 2. theme.toml from theme searched

# prioritised = ID
#   -------------------> ID
# = ""
#   -------------------> ansur

# Checks for currently used theme (theme can be changed in settings or by mod)
def get_theme():
    tf = toml.load(f"themes/guide.toml")
    if tf["behaviour"]["prioritised_id"] == "": return toml.load(f"core/system_ref.toml")["vanilla_modules"][0]
    else:                                       return tf["behaviour"]["prioritised_id"]

def get_theme_file():
    return toml.load(f"themes/{get_theme()}/theme.toml")
#==================================================
# FONTS
#==================================================
# --------------------------------------
# Utils
# --------------------------------------
# Makes list of fonts of the theme. Not sure about use of this, have a nice day
def font_list(theme_id: str):
    fl = []
    try:
        for font in glob.glob(f"{gpath}/themes/{theme_id}/fonts/*.*"): # should return pure file name, not full path
            if ".otf" in font or ".ttf" in font:
                fl.append(font)
    finally:
        return fl

# --------------------------------------
# Gives proper non-gpath file address
# --------------------------------------
# ID specific to current theme
def font_address_def(font_id: str):
    return font_address(get_theme(), font_id)
# Non-ID specific
def font_address(theme_id: str, font_id: str):
    return f"/themes/{theme_id}/fonts/{font_id}"
# Returns font required for current context and used language
def font_handler(context: str, language: str = scx("lang"), overwrite: str = None):
    if overwrite is not None:
        return overwrite
    #[ standard handling ]#
    try:    return get_theme_file()["fonts"][context][language]
    except: return get_theme_file()["fonts"][context]["_"]