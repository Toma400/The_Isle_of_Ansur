from core.file_system.repo_manag import gpath
from core.utils import scx
import glob
import toml
#==================================================
# GENERAL
#==================================================
fallback_id = toml.load(f"core/system_ref.toml")["vanilla_modules"][0]
# 1. guide.toml for themes
# 2. theme.toml from theme searched

# prioritised = ID
#   -------------------> ID
# = ""
#   -------------------> ansur


# Checks for currently used theme (theme can be changed in settings or by mod)
def get_theme():
    tf = toml.load(f"themes/guide.toml")
    if tf["behaviour"]["prioritised_id"] == "": return fallback_id
    else:                                       return tf["behaviour"]["prioritised_id"]

def get_theme_file(id: str = get_theme()):
    return toml.load(f"themes/{id}/theme.toml")
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
    try:    return get_theme_file()["fonts"][context][language][0]
    except: return get_theme_file()["fonts"][context]["_"][0]
# Returns font size modifier (default to 1.0)
def font_size(context: str = None):
    if context is None: return get_theme_file()["fonts"]["general"]["font_size"]
    else:
        try:    return float(get_theme_file()["fonts"][context][scx("lang")][1])
        except: return float(get_theme_file()["fonts"][context]["_"][1])

# Returns address of image that will show up in menu backgrounds
def bg_handler(context: str, split=False):
    try:    bg_img = get_theme_file()["backgrounds"][context];            id = get_theme()
    except: bg_img = get_theme_file(fallback_id)["backgrounds"][context]; id = fallback_id
    if split is False: return f"themes/{id}/assets/{bg_img}"
    else:              return f"themes/{id}/assets/", bg_img