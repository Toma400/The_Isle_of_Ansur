from core.file_system.repo_manag import gpath
from core.utils import scx
from enum import Enum
import logging as log
import glob
import toml
#=======================================================================================
# GENERAL
#=======================================================================================
class Fallback:
    id    = toml.load(f"core/system_ref.toml")["vanilla_modules"][0]
    fsize = 1.0
# 1. guide.toml for themes
# 2. theme.toml from theme searched

# prioritised = ID
#   -------------------> ID
# = ""
#   -------------------> ansur


# Checks for currently used theme (theme can be changed in settings or by mod)
def get_theme() -> str:
    """Returns ID of current theme"""
    tf = toml.load(f"themes/guide.toml")
    if tf["behaviour"]["prioritised_id"] == "": return Fallback.id
    else:                                       return tf["behaviour"]["prioritised_id"]

def get_theme_file(id: str = get_theme()):
    return toml.load(f"themes/{id}/theme.toml")
#=======================================================================================
# FONTS
#=======================================================================================
#
#=======================================================================================
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
#=======================================================================================
# Returns font required for current context and used language
def font_handler(context: str, language: str = scx("lang"), overwrite: str = None):
    try:
        if overwrite is not None:
            return overwrite
        #[ standard handling ]#
        try:    return get_theme_file()["fonts"][context][language][0]
        except: return get_theme_file()["fonts"][context]["_"][0]
    except KeyError:
        log.error(f"Couldn't find proper key for ID: {get_theme()}, context: {context}, language: {language}. Using fallback value.")
        return get_theme_file(Fallback.id)["fonts"][context]["_"][0]
# Returns font size modifier (default to 1.0)
def font_size(context: str = None):
    try:
        if context is None: return get_theme_file()["fonts"]["general"]["font_size"]
        else:
            try:    return float(get_theme_file()["fonts"][context][scx("lang")][1])
            except: return float(get_theme_file()["fonts"][context]["_"][1])
    except KeyError:
        log.error(f"Couldn't find font size value for ID: {get_theme()}, context: {context}. Using fallback value.")
        return Fallback.fsize
# Returns colour related to specific style of text requested. It is suggested to use FontColour enum instead of this function
def font_colour(style: str):
    try:    return get_theme_file()["fonts"]["colours"][style]
    except: return get_theme_file(Fallback.id)["fonts"]["colours"][style]

class FontColour(Enum):
    DISABLED   = font_colour("disabled")
    ENABLED    = font_colour("enabled")
    HOVERED    = font_colour("hovered")
    BACKGROUND = font_colour("background")
    ERROR      = font_colour("error")
    OTHER      = font_colour("other")
#=======================================================================================
# Returns address of image that will show up in menu backgrounds
def bg_handler(context: str, split=False):
    try:    bg_img = get_theme_file()["backgrounds"][context];            id = get_theme()
    except: bg_img = get_theme_file(Fallback.id)["backgrounds"][context]; id = Fallback.id
    if split is False: return f"themes/{id}/assets/{bg_img}"
    else:              return f"themes/{id}/assets/", bg_img