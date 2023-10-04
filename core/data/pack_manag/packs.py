from glob import glob as walkdir
from enum import Enum

class PackTypes(Enum):
    THEME_PACK  = "themes"
    WORLD_PACK  = "worlds"
    STAT_PACK   = "stats"
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
            ret.append(pack)
    return ret

def getGlobalPacks() -> list[str]:
    """Returns global pack type (which means both types having the same ID)"""
    return [p for p in getPacks(PackTypes.WORLD_PACK) if p in getPacks(PackTypes.STAT_PACK)]