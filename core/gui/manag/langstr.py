from core.decorators import Deprecated
from core.utils import *
import toml
#==========|========================================================
# LANGKEYS | Main part of langkey
#==========|========================================================
# Used to align text to specific part of the console
# Takes a bit different values if used with colours
#===================================================================
def langstring (key: str) -> str:
    lang = scx("lang")
    t = toml.load(f"{gpath}/core/lang/{lang}.toml")
    return t[key]

def langjstring (key: str, modtype: str, modid: str = "ansur") -> str:
    try:
        read = toml.load(f"{modtype}/{modid}/lang/{scx('lang')}.toml")
    except FileNotFoundError or KeyError:
        try:
            read = toml.load(f"{modtype}/{modid}/lang/english.toml")
        except KeyError:
            log.warning(
                f"Module {modid} does not have properly set language value for {key}. Please contact the developer of this module for help.")
            return langstring("system__text_load_fail")
    return read[key]

@Deprecated("langjstring")
def langjstringdepr (key: str, modtype: str, modid: str = "ansur"):
    try:
        read = json_read(f"{modtype}/{modid}/lang.json", scx("lang"))
    except KeyError:
        try:
            read = json_read(f"{modtype}/{modid}/lang.json", "english")
        except KeyError:
            log.warning(
                f"Module {modid} does not have properly set language value for {key}. Please contact the developer of this module for help.")
            return langstring("system__text_load_fail")
    return read[key]