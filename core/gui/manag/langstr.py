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
    try:
        t = toml.load(f"{gpath}/core/lang/{scx('lang')}.toml")
    except:
        log.warning(
            f"Internal language file does not have properly set language value for {key}.")
        return langstring("system__text_load_fail")
    return t[key]

def langjstring (key: str, modtype: str, modid: str = "ansur") -> str:
    try:
        read = toml.load(f"{modtype}/{modid}/lang/{scx('lang')}.toml")[key]
    except:
        try:
            read = toml.load(f"{modtype}/{modid}/lang/english.toml")[key]
        except:
            log.warning(
                f"Module {modid} does not have properly set language value for {key}. Please contact the developer of this module for help.")
            return langstring("system__text_load_fail")
    return read