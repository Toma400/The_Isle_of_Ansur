from core.file_system.parsers import loadYAML
from core.utils import *
import toml, os
#==========|========================================================
# LANGKEYS | Main part of langkey
#==========|========================================================
# Used to align text to specific part of the console
# Takes a bit different values if used with colours
#===================================================================
def parseGender (string: str, gender_id: str) -> str:
    """Replaces all keywords into their respective gender variant"""
    initial_text        = string
    pack_id, gender_uid = gender_id.split(":")
    rule_path           = f"stats/{pack_id}/lang/rules/{scx('lang')}__{gender_uid}.yaml"
    if os.path.exists(rule_path):
        gender_dict = loadYAML(rule_path)
        for og, rep in gender_dict.items():
            initial_text = initial_text.replace(og, rep)
    print(initial_text)
    return initial_text

def langstring (key: str) -> str:
    try:
        return toml.load(f"{gpath}/core/lang/{scx('lang')}.toml")[key]
    except:
        log.warning(
            f"Internal language file does not have properly set language value for {key}.")
        return langstring("system__text_load_fail")

def langjstring (key: str, modtype: str, modid: str = "ansur", gender: str = None) -> str:
    try:
        read = toml.load(f"{modtype}/{modid}/lang/{scx('lang')}.toml")[key]
    except:
        try:
            read = toml.load(f"{modtype}/{modid}/lang/english.toml")[key]
        except:
            log.warning(
                f"Module {modid} does not have properly set language value for {key}. Please contact the developer of this module for help.")
            return langstring("system__text_load_fail")
    if gender is None:
        return read
    else:
        return parseGender(read, gender)
