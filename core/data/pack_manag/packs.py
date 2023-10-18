from core.gui.manag.langstr import langstring
from glob import glob as walkdir
from enum import Enum

class PackTypes(Enum):
    WORLD_PACK  = "worlds"
    STAT_PACK   = "stats"
    THEME_PACK  = "themes"
    # those are loaded differently, so script below won't work
    # ANY
    # ALL
    # GLOBALPACK

pack_types = [PackTypes.THEME_PACK, PackTypes.STAT_PACK, PackTypes.WORLD_PACK]

def getScripts() -> list[str]:
    """Returns list of script names (as str value)"""
    ret = []
    for py in walkdir(f"scripts/*.py"):
        with open(py, "r") as pyf:
            if "(ioaScript):" in pyf.read():
                ret.append(py.replace("scripts", "").replace(".py", "").strip(r"\\"))
    return ret

def getPacks(kind: PackTypes = None) -> dict[list[str]] | list[str]:
    """Returns dictionary of pack lists, separated by type, or type if argument is filled"""
    if kind is None:
        ret = {"scripts": getScripts()}
        for pack_type in pack_types:
            packs = []
            for pack in walkdir(f"{pack_type.value}/*/"):
                packs.append(pack.replace(pack_type.value, "").strip(r"\\"))
            ret[pack_type.value] = packs
    else:
        ret = []
        for pack in walkdir(f"{kind.value}/*/"):
            ret.append(pack.replace(kind.value, "").strip(r"\\"))
    return ret

def getPacksSimplified(pack_list: dict[list[str]] = getPacks(), langstr: bool = True) -> dict[list[str]]:
    """Returns dictionary of pack IDs and list of types. Useful for situations where we want to know about connected packs
    - pack_list - list of packs that should be analysed (default: currently loaded ones)
    - langstr   - whether types of packs are raw (enums) or translated (GUI-friendly)
    """
    ret   = {}
    for kind in pack_list.keys():
        if kind != "scripts":
            for pack in pack_list[kind]:
                kindstr = langstring(f"pack__{kind}") if langstr else kind
                if pack in ret:
                    ret[pack] = ret[pack] + [kindstr]
                else:
                    ret[pack] = [kindstr]
    return ret

def getGlobalPacks() -> list[str]:
    """Returns global pack type (which means both types having the same ID)"""
    return [p for p in getPacks(PackTypes.WORLD_PACK) if p in getPacks(PackTypes.STAT_PACK)]