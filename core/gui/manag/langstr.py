from core.file_system.parsers import loadYAML
from core.utils import *
import toml, os, re
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
            initial_text = re.sub(f"\\b{og}\\b",              rep,              initial_text)
            initial_text = re.sub(f"\\b{og.capitalize()}\\b", rep.capitalize(), initial_text)
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
        if read[0] == "!": # "!" at the beginning of the string marks requirement for replacement
            return parseGender(read[1:], gender) # removes "!"
        return read

class ErrorDummy:
    """Used in situations when `langstr()` is casted on object that would yield error string in langstr() phase, but its initialisation does that beforehand
    Solution to errors like this: https://github.com/Toma400/The_Isle_of_Ansur/issues/111"""

    @staticmethod
    def langstr() -> str:
        return langstring("system__text_load_fail")

    def get(self, attribute: str) -> None:
        return None

    def getc(self, category: str, attribute: str) -> None:
        return None