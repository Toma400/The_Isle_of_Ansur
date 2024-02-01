from core.gui.manag.langstr import langjstring, ErrorDummy
from core.decorators import Deprecated
from system.mod_manag import mod_lister
from os.path import exists
import json

class Gender:
    """Class defining shortcut for gender element"""

    def __init__(self, name: str, tr_key: str, mod_id: str):
        self.name   : str = name    # name ID (used for GID)
        self.key    : str = tr_key  # translation key
        self.mod_id : str = mod_id  # mod ID

    def gid(self) -> str:
        """Creates GID representation of gender, to export/import during game"""
        return f"{self.mod_id}:{self.name}"

    def langstr(self) -> str:
        """Returns langstring of object based on currently used language"""
        return langjstring(key=self.key, modtype="stats", modid=self.mod_id)

    def __repr__(self) -> str:
        return self.langstr()

    def __str__(self) -> str:
        return self.langstr()

def getGender(gid: str) -> Gender | ErrorDummy:
    """Gender constructor that uses GID instead of explicit __init__ constructor. Resource-heavy in iteration compared to getGenders()"""
    gid_ems = gid.split(":")

    if exists(f"stats/{gid_ems[0]}/genders.json"):
        def returnKey() -> str: # returns translation key
            with open(f"stats/{gid_ems[0]}/genders.json") as jf:
                pjf = json.load(jf)
                return pjf[gid_ems[1]]["key"]

        return Gender(name=gid_ems[1], tr_key=returnKey(), mod_id=gid_ems[0])
    return ErrorDummy()

def getGenders() -> list[Gender]:
    """Main gatherer of gender data during load/reload"""
    ret: list[Gender] = []
    for stat_pack in mod_lister("stats"):
        if exists(f"stats/{stat_pack}/genders.json"):
            with open(f"stats/{stat_pack}/genders.json") as jf:
                pjf = json.load(jf)
                for gender in pjf.keys():
                    ret.append(Gender(gender, pjf[gender]["key"], stat_pack))
    return ret

def getGendersTuple() -> list[(str, str)]:
    """PyGame_GUI - friendly variant of Gender getter, returning tuple of <translation, GID>"""
    ret: list[(str, Gender)] = []
    for gc in getGenders():
        ret.append((gc.langstr(), gc.gid()))
    return ret

@Deprecated("Use <getGendersTuple> and UISelectionBox instead.")
def getGendersStrings() -> list[str]:
    """PyGame_GUI - friendly variant of Gender comparison. Should be deprecated in the future."""
    ret: list[str] = []
    for gc in getGenders():
        ret.append(gc.langstr())
    return ret

@Deprecated("This serves more as an example on how to resolve issues with string-based identification. Use docstring way instead.")
def getGenderFromList(list_pos: int) -> Gender:
    """More of an example how to get Gender object from purely string"""
    # getGendersStrings[10] == getGenderFromList(10) == getGenders[10]
    return getGenders()[list_pos]